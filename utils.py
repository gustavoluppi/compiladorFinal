import re
import constants


def is_special_caracter(caracter):
    """Verifica se o elemento é um separador dos numeros"""
    if (re.match(r"[\w]", caracter)):
        return 0
    else:
        return 1


def is_reserved_word(word):
    return word in constants.RESERVED_WORDS


def is_number(token):
    """Verifica se o elemento pertence ao grupo das constantes numericas"""
    if(re.match(r"[\d.]", token)):
        return 0
    else:
        """Se ele não pertence retorna 1"""
        return 1


def is_error(token):
    if not re.match(r"[\w]", token):
        if token not in constants.ALL_ELEMENTS:
            if not re.search(r"\s", token) or token == "\n" or token == " ":
                return True
    return False


