#!/usr/bin/python3
"""Creates Mylist class thath inherits from list"""


class MyList(list):
    """this class that defines a list"""
    def print_sorted(self):
        """method prints the list"""
	print(sorted(self))
