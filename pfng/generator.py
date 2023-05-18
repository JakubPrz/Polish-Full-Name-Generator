from random import choice

from pfng.data_reader import *


def generate_full_names(number: int, gender: str = 'M&F') -> List[str]:
    """
    Generates full names.

    Args:
        number: The number of full names to generate.
        gender (optional): The gender of full names (M, F, M&F)

    Raises:
        ValueError: If number of full names is < 1
        TypeError: If invalid gender was given.

    Returns:
        full_names: A list of generated full names.
    """

    gender_map = {
        'M': (MALE_NAMES, MALE_SURNAMES),
        'F': (FEMALE_NAMES, FEMALE_SURNAMES),
        'M&F': None
    }

    if number < 1:
        raise ValueError('Number of full names must be > 0 !')

    if gender not in gender_map.keys():
        raise TypeError('Provide valid gender type !')

    full_names = []
    for i in range(number):
        if gender == 'M&F':
            name_list, surname_list = gender_map[choice(['M', 'F'])]
        else:
            name_list, surname_list = gender_map[gender]
        name = choice(name_list)
        surname = choice(surname_list)
        full_names.append(f"{name} {surname}")

    return full_names
