from tkinter import messagebox as messagebox

from variables import label_first_name, label_last_name, label_personal_id, label_ester_login, label_tht_code, \
    label_additional_info, label_phone_number


# Validation functions

def is_alpha(string: str):
    """
    The function checks if the string is literal characters.
    :param string: The string to validate entered by the user.
    :return: True or False
    """
    return string.isalpha()


def is_numeric(string: str):
    """
    The function checks if the string is numeric characters.
    :param string: The string to validate entered by the user.
    :return: True or False
    """
    return string.isnumeric() and len(string) == 11


def is_alnum(string: str):
    """
    The function checks if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
    :param string: The string to validate entered by the user
    :return: True or False
    """
    return string.isalnum()


def is_empty(string: str):
    """
    The function checks if the string is empty
    :param string: The string to validate entered by the user
    :return: True or False
    """
    return bool(string)


def string_check(string: str):
    """
    Checking variables label_first_name and label_last_name
    :param string: The string to validate entered by the user
    :return: return 0 if validation failed
    """
    if not is_alpha(string.strip()):
        messagebox.showerror("Error", f"{label_first_name}или {label_last_name}- cодержат ошибку!")
        return 0


def numeric_check(string: str):
    """
    Checking variables label_personal_id
    :param string: The string to validate entered by the user
    :return: return 0 if validation failed
    """
    if not is_numeric(string):
        messagebox.showerror("Error", f"{label_personal_id}- cодержит ошибку!")
        return 0


def login_tht_check(string: str):
    """
    Checking variables label_ester_login and label_tht_code
    :param string: The string to validate entered by the user
    :return: return 0 if validation failed
    """
    if not is_alnum(string):
        messagebox.showerror("Error", f"{label_ester_login}или {label_tht_code}- cодержат ошибку!")
        return 0


def checking_emty_string(string: str):
    """
    Checking variables label_additional_info and label_phone_number
    :param string: The string to validate entered by the user
    :return: return 0 if validation failed
    """
    if not is_empty(string):
        messagebox.showerror("Error", f"{label_additional_info}или {label_phone_number}- пустые!")
        return 0
