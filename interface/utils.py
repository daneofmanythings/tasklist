import os
from config.globals import MENU_PADDING, HEADER_PADDING, PROMPT, MENU_OFFSET
from config.theme import HOTKEY, CURRENT_MENU


def header_string(header_list):
    return HEADER_PADDING + " / ".join(header for header in header_list)


def paint_text(text: str, hex_str: str) -> str:
    r, g, b = int(hex_str[1:3], 16), int(
        hex_str[3:5], 16), int(hex_str[5:7], 16)

    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


def hotkey(hotkey: str):
    return f"[{paint_text(hotkey, HOTKEY)}]"


def paint_header(header_list):
    result = header_list.copy()
    result[-1] = paint_text(header_list[-1], CURRENT_MENU)
    return result


def table_to_string(table, offset):
    padding = "\n" + " " * offset
    result = padding
    result += padding.join(s for s in table)
    result += "\n"
    return result


def menu_string(table):
    return table_to_string(table, MENU_OFFSET)


def submenu_string(table):
    return MENU_PADDING + " | ".join(table)


def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def get_menu_input(options_list):
    while True:
        response = input(PROMPT)
        if response in options_list:
            return options_list[response]
