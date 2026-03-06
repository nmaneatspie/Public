"""

Simple searching via two different methods. one method is an iterative binary search.

"""

from functools import wraps
import time
import random


# Timing decorator
def time_process(func):
    @wraps(func)
    def timed(*args, **kwargs) -> None:

        start = time.process_time()
        result = func(*args, **kwargs)
        end = time.process_time()

        exec_time = end - start
        print("{:e} seconds to complete function: {}".format(exec_time, func.__name__))

        return result, exec_time

    return timed


@time_process
def pysearch(search_term: int, search_list: list[int]) -> int:

    try:
        search_term in search_list
        return search_list.index(search_term)

    except ValueError:
        return -1


@time_process
def binary_search(search_term: int, search_list: list[int]) -> int:

    left: int = 0
    right: int = len(search_list) - 1

    while right > left:
        pointer = (left + right) // 2

        if search_list[pointer] == search_term:
            return pointer
        elif search_list[pointer] > search_term:
            right = pointer
        else:
            left = pointer + 1

    return -1


def main(search_term: int, search_list: list, search_method: str = "binary") -> int:

    index: int = -1

    search_list.sort()

    match search_method:
        case "binary":
            index, _ = binary_search(search_term, search_list)
        case "pysearch":
            index, _ = pysearch(search_term, search_list)
        case _:
            raise Exception("Invalid search method")

    if index == -1:
        print("{} is not in the list.".format(search_term))
    else:
        print("{} exists in the list.".format(search_term))

    return index


search_term = 50
search_list: list[int] = random.sample(range(-10, 1000), 500)

if __name__ == "__main__":
    main(search_term, search_list, "binary")
    main(search_term, search_list, "pysearch")
    main(search_term, search_list, "binary")
    main(search_term, search_list, "pysearch")
