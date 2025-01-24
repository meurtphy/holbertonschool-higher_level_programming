#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Affiche 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): Le prénom.
        last_name (str): Le nom de famille (optionnel).

    Raises:
        TypeError: Si first_name ou last_name ne sont pas des chaînes
                   de caractères.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name == "" and last_name == "":
        print("My name is")
    else:
        print(f"My name is {first_name} {last_name}".strip())
