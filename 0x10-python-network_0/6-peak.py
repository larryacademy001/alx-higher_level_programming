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
    m_elem = list_size
    mid = list_size // 2

    if list_size == 0:
        return None

    while True:
        m_elem = m_elem // 2
        if (mid < list_size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if m_elem // 2 == 0:
                m_elem = 2
            mid = mid + m_elem // 2
        elif m_elem > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if m_elem // 2 == 0:
                m_elem = 2
            mid = mid - m_elem // 2
        else:
            return list_of_integers[mid]
