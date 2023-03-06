def code_to_name(code_str):
    return code_str.capitalize().replace('_', ' ')


def create_choices_tuple(choices_list):
    return tuple((code_to_name(item_code), item_code)
                 for item_code in choices_list)
