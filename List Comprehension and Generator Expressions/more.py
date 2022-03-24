"""More comprehension exercises"""
from lists import get_factors

def flip_dict(dictionary):
    """Return a new dictionary that maps the original values to the keys."""
    return {
        value:key
        for key, value in dictionary.items()
    }


def get_ascii_codes(str_list):
    """Return a dictionary mapping the strings to ASCII codes."""
    return {
        word:[ord(letter) for letter in word]
        for word in str_list
    }

def dict_from_truple(tuple_list):
    """Turn three-item tuples into a dictionary of two-valued tuples."""
    return {
        tup[0]:tup[1:]
        for tup in tuple_list
    }


def dict_from_tuple(tuple_list):
    """Turn multi-item tuples into a dictionary of two-valued tuples."""
    return dict_from_truple(tuple_list)


def get_all_factors(set_numbers):
    """Return a dictionary mapping numbers to their factors."""
    return {
        number:get_factors(number)
        for number in set_numbers
        }
    
