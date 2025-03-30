from SinCity.colors import RED, RESET, YELLOW, GREEN, BLUE
from manifest import dir_password
import os, json, shutil

def ListCategory():
    list_category = []
    list_other = []
    for category in os.listdir(dir_password):
        category = f'{dir_password}/{category}'
        if os.path.isdir(category):list_category.append(category)
        else:list_other.append(category)

    return list_category, list_other

# Первичная обработка 
def ProcessingPasswords(mode:str):
    list_path = []
    categories, other_pass = ListCategory()
    if len(categories) > 0:
        number_category = 0
        for category in categories:
            number_category+=1
            number_service=0
            category_split = category.split('/')[1]

            print(f'{BLUE}[{number_category}] {category_split}{RESET}')
            for service in os.listdir(category):
                number_service+=1
                service_split = service
                if '.json' in service_split:service_split = service_split.split('.json')[0]
                print(f'\t{GREEN}[{number_service}] {service_split}{RESET}')
                
                list_path.append(f'{category}/{service}')

    if len(other_pass) > 0:
        number_other = 0
        for other in other_pass:
            number_other+=1
            other_split = other.split('/')[1]
            print(f'{GREEN}[{number_other}] {other_split}{RESET}')
            list_path.append(other)
    
    if len(categories) == 0 and len(other_pass) == 0:
        print(f'{RED}Список паролей пуст!{RED}')

    else:
        search_data = input("Enter user or email: ")
        print(f'Search by: {search_data}...')
        select_variant = ProcessingResult(
                search=search_data, 
                list_path=list_path, 
                mode=mode
                )

# Обрабатываем данные. В конце показываем/удаляем данные
def ProcessingResult(search:str, list_path:[], mode:str):
    sorted_list = []
    for full_path_json in list_path:
        if search in full_path_json:
            path_password = full_path_json
            sorted_list.append(full_path_json)
    
    if len(sorted_list) == 0:print(f'{RED}Совпадений не найдено{RESET}')
    if len(sorted_list) != 0:
        number_password=0
        for result in sorted_list:
            number_password+=1
            path_password = result.split(f'{dir_password}/')[1]
            category, service = path_password.split('/')
            if '.json' in service:service = service.split('.json')[0]

            print(f'[{number_password}] {category}:\t{BLUE}{service}{RESET}')

        try:
            show_select_data = int(input("Select number: "))
            select_data = sorted_list[show_select_data-1]
            if mode == 'show':
                service, user, password = showPass(select_data=select_data)
                print(
                        f'\nService:\t{service}\n'
                        f'User/Email:\t{user}\n'
                        f'Password:\t{password}\n'
                        )
            if mode == 'delete':
                service = select_data.split('/')[-1]
                approve = input(f'Remove data {RED}{service}?{RESET}(y/N) ')
                if approve == 'y':
                    os.remove(select_data)
                    print(f'Deleted {RED}{service}{RESET}!')
        except IndexError:print(f'{RED}Incorrect select!{RESET}')

# Показываем пароль
def showPass(select_data:str):
    user = None
    password = None
    with open(select_data, 'r') as file:
        data = json.load(file)
        for service, value in data.items():
            service = service
            user = value['user']
            password = value['password']
    return service, user, password

# Удаление целой категории
def DeleteCategory():
    list_category = os.listdir(dir_password)
    number_category = 0
    if len(list_category) > 0:
        print('All Category:')
        for category in list_category:
            number_category+=1
            print(f'{RED}[{number_category}] {category}{RESET}')
        
        try:
            select_category = int(input('Select Category: '))
            select_category = select_category-1
            target_category = list_category[select_category]
            approve = input(f'{RED}Delete dir: {target_category}?{RESET}(y/N) ')
            if approve == 'y':
                shutil.rmtree(f'{dir_password}/{target_category}')
                print(f'{RED}Delete dir: {target_category}{RESET}')
            else:print(f'{GREEN}Cancel{RESET}')
        except IndexError:print(f'{RED}Incorrect select!{RESET}')
    else:print(f'{RED}Нет категорий для удаления{RESET}')
