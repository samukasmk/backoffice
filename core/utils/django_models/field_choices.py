def create_choices_tuple(choices_list):
    return tuple((item_code.capitalize().replace('_', ' '),
                  item_code)
                 for item_code in choices_list)
