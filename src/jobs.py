from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, 'r') as file:
        csv_to_object = csv.DictReader(file)
        result = [job for job in csv_to_object]

    return result
