def get_menu_input(prompt, options_list):
    while True:
        response = input(prompt + " >>> ")
        if response in options_list:
            return response
