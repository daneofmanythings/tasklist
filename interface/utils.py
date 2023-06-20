import os
from config.globals import HEADER_PADDING, PROMPT
from config.theme import HOTKEY, CURRENT_MENU


def header_string(header_list):
    return HEADER_PADDING + " / ".join(header for header in header_list)


def color_text(text: str, hex_str: str) -> str:
    r, g, b = int(hex_str[1:3], 16), int(
        hex_str[3:5], 16), int(hex_str[5:7], 16)

    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


def hotkey(hotkey: str):
    return f"[{color_text(hotkey, HOTKEY)}]"


def current_menu(header_list):
    header_list[-1] = color_text(header_list[-1], CURRENT_MENU)
    return header_list


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
        response = input(prompt + PROMPT)
        if response in options_list:
            return options_list[response]


def table_to_string(table, offset):
    padding = '\n' + ' ' * offset
    result = str()
    result += padding
    result += padding.join(s for s in table)
    result += padding
    return result
