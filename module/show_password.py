from SinCity.colors import RED, RESET, YELLOW, GREEN, BLUE
from manifest import dir_password
import os, json

def ListCategory():
    list_category = []
    list_other = []
    for category in os.listdir(dir_password):
        category = f'{dir_password}/{category}'
        if os.path.isdir(category):list_category.append(category)
        else:list_other.append(category)

    return list_category, list_other

def ShowPasswords():
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
                print(f'\t{GREEN}[{number_service}] {service}{RESET}')

    if len(other_pass) > 0:
        number_other = 0
        for other in other_pass:
            number_other+=1
            other_split = other.split('/')[1]
            print(f'{GREEN}[{number_other}] {other_split}{RESET}')
    
    if len(categories) == 0 and len(other_pass) == 0:
        print(f'{RED}Список паролей пуст!{RED}')
