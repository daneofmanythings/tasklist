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


def table_to_string(header, offset):
    padding = '\n' + ' ' * offset
    result = str()
    result += padding
    result += padding.join(s for s in header)
    result += padding
    return result


def main():
    menu1 = (
        'a',
        'b'
    )
    menu2 = (
        'c',
        'd',
    )

    string = ''
    string += table_to_string(menu1, 10)
    string += table_to_string(menu2, 4)
    print(string)


if __name__ == "__main__":
    main()
