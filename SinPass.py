#!/usr/bin/python3
# SinPass
# Copyright (C) 2025  Rickert156
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Full text of the GNU General Public License v3.0 is available at:
# http://www.gnu.org/licenses/gpl-3.0.txt
from SinCity.colors import RED, RESET, GREEN, BLUE
from manifest import version 
from module.new_password import GetNewPassword, SavePassword
from module.processing_password import ProcessingPasswords, DeleteCategory
from module.miniTools import StartSinPass

import json, os

def menuSinPass():
    StartSinPass()
    print(f'{RED}SinPass{RESET} - {GREEN}Version {version}\n{RESET}')
    select_task = int(input(
        f'{BLUE}[1]{RESET} Create new password\n'
        f'{BLUE}[2]{RESET} Save Password\n'
        f'{BLUE}[3]{RESET} Show Passwords\n'
        f'{BLUE}[4]{RESET} Update Password\n'
        f'{BLUE}[5]{RESET} Delete Password\n'
        f'{BLUE}[6]{RESET} Delete Category\n'
        f'{RED}>>> {RESET}'
            ))

    if select_task == 1:print(GetNewPassword())
    if select_task == 2:SavePassword()
    if select_task == 3:ProcessingPasswords(mode='show')
    if select_task == 4:ProcessingPasswords(mode='update')
    if select_task == 5:ProcessingPasswords(mode='delete')
    if select_task == 6:DeleteCategory()

try:
    menuSinPass()
except Exception as err:print(f'{RED}{err}{RESET}')
except KeyboardInterrupt:print(f'{RED}\nExit...{RESET}')

