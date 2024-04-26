#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    list_size = len(list_of_integers)
    mid_elem = list_size
    mid = list_size // 2

    if list_size == 0:
        return None

    while True:
        mid_elem = mid_elem // 2
        if (mid < list_size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if mid_elem // 2 == 0:
                mid_elem = 2
            mid = mid + mid_elem // 2
        elif mid_elem > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if mid_elem // 2 == 0:
                mid_elem = 2
            mid = mid - mid_elem // 2
        else:
            return list_of_integers[mid]
