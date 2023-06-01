import os


def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


class NoCursor:
    def __enter__(self):
        print('\033[?25l', end="")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('\033[?25h', end="")


def get_menu_input(prompt, options_list):
    while True:
        response = input(prompt + " >>> ")
        if response in options_list:
            return options_list[response]
