#------------------------------------------------------------------------------
# Є текстовий файл з інформацією про зарплату розробника
#   у вигляді: Oleks Andr, 3000
# Розробити функцію total_salary(path), яка аналізує цей файл і повертає
#   загальну і середню плату всіх розробників
# Результат роботи функції - кортеж із двох чисел: загальної суми зарплат
#   і середньої плати розробників
#------------------------------------------------------------------------------
def load_data(filename: str) -> list[str]:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        return 'The file with such name or path doesn\'t exist'
def prepare_data(raw_data: list[str]) -> list[float]:
    return [float(raw_unit.split(', ')[1]) for raw_unit in raw_data]
def calculate_stats(salary_d: list[float]) -> tuple:
    return round(sum(salary_d), 2), round(sum(salary_d) / len(salary_d), 2)

def total_salary(path_sal:str) -> tuple:
    raw_list = load_data(path_sal)
    if type(raw_list) == list:
        salary_list = prepare_data(raw_list)
        return calculate_stats(salary_list)
    else:
        return raw_list

total, average = total_salary('salary.txt')
print(f'The total sum is {total}, the average salary is {average}')

#------------------------------------------------------------------------------
# Є текстовий файл з інформацією про котів у вигляді:
#   60b90c1c13067a15887d1df1, Tayson, 3
# Розробити функцію get_cats_info(path), яка читає цей файл і повертає список
#   словників з ключами 'id', 'name', 'age'
#------------------------------------------------------------------------------

def prepare_info(raw_data: list[str]) -> list[dict]:
    raw_list = [raw_unit.split(', ') for raw_unit in raw_data]
    cat_list = []
    for elem in raw_list:
        cat_list.append({
            'id': elem[0],
            'name': elem[1],
            'age': int(elem[2]),
        })
    return cat_list

def get_cats_info(path_cats: str) -> list[dict]:
    raw_list = load_data(path_cats)
    if type(raw_list) == list:
        return prepare_info(raw_list)
    else:
        return raw_list

print(get_cats_info('animals\domestic\cats.txt'))

#------------------------------------------------------------------------------
# Розробити скрипт, який приймає шлях до директорії і візуалізує структуру цієї
#   директорії і всіх піддиректорій (треба додати у проект)
#   Імена піддиректорій і файлів мають відрізнятися за кольором
#------------------------------------------------------------------------------

# Installing pack:
# PS:\example> python -m venv .venv
# PS:\example> .\.venv\Scripts\Activate.ps1
# (.venv) PS F:\example> pip install colorama
# Deactivating env:
# (.venv) PS F:\example> deactivate
# Activating env:
# PS:\example> .\.venv\Scripts\Activate.ps1

from colorama import Fore
from pathlib import Path

def take_structure(path_str: str) -> None:
    try:
        path_all = Path(path_str)
        try:
            for path_item in path_all.iterdir():
                if path_item.is_dir():
                    print(f'{Fore.YELLOW}{path_item}{Fore.RESET}')
                else:
                    print(f'{Fore.GREEN}{path_item}{Fore.RESET}')
                take_structure(str(path_item))
        except NotADirectoryError:
            return
    except FileNotFoundError:
        print('The path is invalid')
        return

take_structure('animals')

#------------------------------------------------------------------------------
# Бот-асистент повинен вміти:
#   зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям
#   змінювати номер, і виводити всі записи
#------------------------------------------------------------------------------

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added'

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact changed'

def get_number(args, contacts):
    name = args[0]
    return contacts[name]

def get_contacts(contacts):
    user_list = ['---- List of Users ----']
    for key, value in contacts.items():
        user_list.append(f'{key}: {value}')
    return '\n'.join(user_list)

def main():
    contacts = {}
    print('Welcome to the assistant bot')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)
        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(get_number(args, contacts))
        elif command == 'all':
            print(get_contacts(contacts))
        else:
            print('Invalid command')
if __name__ == '__main__':
    main()

#------------------------------------------------------------------------------