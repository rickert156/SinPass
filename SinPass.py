from SinCity.colors import RED, RESET, GREEN, BLUE
from manifest import version 
from module.new_password import GetNewPassword, SavePassword
from module.show_password import ShowPasswords
from module.miniTools import StartSinPass

import json, os


def menuSinPass():
    StartSinPass()
    print(f'{RED}SinPass{RESET} - {GREEN}Version {version}\n{RESET}')
    select_task = int(input(
        f'{BLUE}[1]{RESET} Create new password\n'
        f'{BLUE}[2]{RESET} Save password\n'
        f'{BLUE}[3]{RESET} Show Passwords\n'
        f'{BLUE}[4]{RESET} Update password\n'
        f'{BLUE}[5]{RESET} Delete password\n'
        f'{RED}>>> {RESET}'
            ))

    if select_task == 1:print(GetNewPassword())
    if select_task == 2:SavePassword()
    if select_task == 3:ShowPasswords()

try:
    menuSinPass()
except Exception as err:print(f'{RED}{err}{RESET}')
except KeyboardInterrupt:print(f'{RED}\nExit...{RESET}')

