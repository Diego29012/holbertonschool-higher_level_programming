#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        the result = a / b
    except ZeroDivisionError:
        the result = None
    finally:
        print("Inside result: {}".format(theresult))
    return the result
