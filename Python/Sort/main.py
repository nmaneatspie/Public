"""

Simple sorting practice using python in-built sort and practice integrating C code.

"""
from functools import wraps
import time
import random
from py_csort import csort


# Timing decorator
def time_process(func):
    @wraps(func)
    def timed(*args, **kwargs) -> None:

        start = time.process_time()
        result = func(*args, **kwargs)
        end = time.process_time()

        print(
            "{:e} seconds to complete function: {}".format(end - start, func.__name__)
        )

        return result

    return timed


def sort_list_int(
    to_sort: list[int],
    order: int = 0,
    keep_orig: bool = False,
    method: int = 0,
) -> list[int]:
    # order 0 = ascending, otherwise descending
    # method 0 = python in-built sort, 1 = custom code, otherwise = in-built

    match keep_orig:
        case False:
            new_list = to_sort
        case True:
            new_list = []
            new_list.extend(to_sort)

    match method:
        case 0:
            sort(new_list, order)
        case 1:
            mysort(new_list, order)
        case _:
            sort(new_list, order)
            
    return new_list


@time_process
def sort(
    to_sort: list[int],
    order: int = 0,
) -> None:  # accept only list or sets too? for now sort list
    # order 0 = ascending, otherwise descending
    if order == 0:
        to_sort.sort()
    else:
        to_sort.sort(reverse=True)

@time_process
def mysort(
    to_sort: list[int],
    order: int = 0,
) -> None:

    csort(to_sort, order)

def main(arg1) -> None:
    # print("List: ", arg1)
    m0 = sort_list_int(arg1, keep_orig=True)
    m1 = sort_list_int(arg1, keep_orig=True, method=1)

    # print("Sorted method 0: ", m0)
    # print("Sorted method 1: ", m1)

    if m0 == m1:
        print("Sorted lists are the same")
    else:
        raise Exception("Sorted lists are NOT the same")


num_test = 2

for i in range(0, num_test):
    test_list: list[int] = random.sample(range(-1000, 1000), 50)

    if __name__ == "__main__":
        main(test_list)
