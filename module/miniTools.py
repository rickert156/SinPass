import json, os
from global_var import dir_password 

# Инициализация утилиты
def StartSinPass():
    if not os.path.exists(dir_password):os.makedirs(dir_password)

# Определить текущее состояние парольного менеджера
def CurrentState():
    list_type = []
    for base in os.listdir(dir_password):
        list_type.append(base)

    return list_type
