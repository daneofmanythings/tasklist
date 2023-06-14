from interface.menu import Menu, MenuReturn
from interface.menu import MenuReturnState as state
from interface.menus.generate_tasklist import GenerateTasklist
from interface.menus.view_all_tasklists import ViewAllTasklists


class ManageTasklists(Menu):
    HEADER = (
        'MAIN / MANAGE_TASKLISTS /',
    )
    MENU = (
        "1) Generate new list",
        # "2) Create custom list",
        "2) View all lists",
        # "4) "
        "3) Go Back",
    )
    OPTIONS = {
        "1": MenuReturn(state.NEXT_MENU, GenerateTasklist),
        "2": MenuReturn(state.NEXT_MENU, ViewAllTasklists),
        "3": MenuReturn(state.PREVIOUS_MENU, None)
    }
