from SinCity.DataGenerate.text_generator import generator 
from SinCity.colors import RED, RESET
from module.miniTools import CurrentState
from global_var import dir_password 
import json, os

# Генерируем пароль, но не сохраняем
def GetNewPassword():
    len_password = int(input("Len Password: "))
    if len_password <= 8:
        print("Short Password!")
        GetNewPassword()
    else:
        password = generator(max_count_char=len_password, max_word=1)[0]
        return password


def SavePassword():
    try:
        current_data = CurrentState()
        create_category = CreateNewCategory()
        service = input('Service Domain/Name: ')
        user_name = input('User/Email: ')
        password = input('Password: ')
        if create_category:path_dir = create_category
        else:path_dir = dir_password
        RecordingNewPassword(
                path_dir=path_dir, 
                service=service, 
                user_name=user_name,
                password=password
                )
        
    except Exception as err:print(f'{RED}{err}{RESET}')

def RecordingNewPassword(path_dir:str, service:str, password:str, user_name:str):
    path_password = f'{path_dir}/{service}.json'
    data = {
            service:{
                "user":user_name,
                "password":password
                     }
            }
    with open(path_password, 'w') as file:
        json.dump(data, file, indent=4)


def CreateNewCategory():
    category_state = True
    category = input('Create new category?(y/n) ')
    if category == 'y':
        category_name = input('Category: ')
        if ' ' in category_name:category_name = category_name.replace(' ', '_')
        if ',' in category_name:category_name = category_name.replace(',', '_')
        category_path = f'{dir_password}/{category_name}'
        if not os.path.exists(category_path):os.makedirs(category_path)
        category_name = f'{dir_password}/{category_name}'
        return category_name
    else:
        list_category = CurrentState() 
        if len(list_category) > 0:
            print('All Category: ')
            number_category = 0
            for category in list_category:
                number_category+=1
                print(f'[{number_category}] {category}')
            try:
                select_category = int(input("Select Category: "))
                select_category = select_category-1
                category = list_category[select_category]
                category_path = f'{dir_password}/{category}'
                return category_path 
            except IndexError:print(f'{RED}Incorrect select!{RESET}')
            
        else: 
            category_state = False
            category_name = category_state
            return category_name
