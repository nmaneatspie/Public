"""

Class file for an integer container with some simple methods. Input is in fact string values but the container houses integer values

"""

import sys
from functools import wraps


def check_value_is_int(func):
    @wraps(func)
    def funct(self, value):
        try:
            int(value)
        except Exception:
            raise ValueError("Not a valid integer")

        return func(self, value)

    return funct


class IntContainer:
    def __init__(self):
        self.num_arr: list[int] = []

    @check_value_is_int
    def add(self, value: str) -> str:
        # add a value to the container and return empty string
        self.num_arr.append(int(value))
        return ""

    @check_value_is_int
    def remove(self, value: str) -> str:
        # remove only a single occurence of the value from the container
        try:
            idx = self.num_arr.index(int(value))

            del self.num_arr[idx]

            return "true"
        except Exception:
            return "false"

    @check_value_is_int
    def exists(self, value: str) -> str:
        #  return "true" if value exists in container else "false"
        if int(value) in self.num_arr:
            return "true"
        else:
            return "false"

    @check_value_is_int
    def get_next(self, value: str) -> str:
        # return minimal integer strictly greater than value
        temp: int = sys.maxsize
        found: bool = False

        for i in self.num_arr:
            if int(i) > int(value) and int(i) < temp:
                found = True
                temp = int(i)

        if found:
            return str(temp)
        else:
            return ""
