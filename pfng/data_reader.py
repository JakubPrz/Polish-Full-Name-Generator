from typing import List
from csv import reader


def _read_from_csv(csv_path: str) -> List[str]:
    """
    Reads the data from a CSV file.

    Args:
        csv_path: The path of the CSV file.

    Returns:
        A list of rows from the CSV file.
    """
    with open(csv_path, encoding="utf-8") as file:
        csv_reader = reader(file)
        next(csv_reader)  # skip header
        rows = [r[0] for r in csv_reader]
    return rows


MALE_NAMES = _read_from_csv(r'./data/male_names.csv')
FEMALE_NAMES = _read_from_csv(r'./data/female_names.csv')
MALE_SURNAMES = _read_from_csv(r'./data/male_surnames.csv')
FEMALE_SURNAMES = _read_from_csv(r'./data/female_surnames.csv')
