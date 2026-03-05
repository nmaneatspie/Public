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

        print(
            "{:e} seconds to complete function: {}".format(end - start, func.__name__)
        )

        return result

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
    right: int = len(search_list)

    while right > left:
        pointer = (left + right) // 2
        
        subt = (search_list[pointer] > search_term) - (
            search_term > search_list[pointer]
        )

        match subt:
            case 0:
                return pointer
            case 1:
                right = pointer
            case -1:
                left = pointer + 1

    return -1



def main(search_term: int, search_list: list, search_method: str = "binary") -> int:

    index: int = -1
    
    search_list.sort()
    
    match search_method:
        case "binary":
            index = binary_search(search_term, search_list)
        case "pysearch":
            index = pysearch(search_term, search_list)
        case _:
            raise Exception("Invalid search method")

    if index == -1:
        print("{} is not in the list.".format(search_term))
    else:
        print("{} exists in the list.".format(search_term))

    return index


search_term = 30
search_list: list[int] = random.sample(range(-40, 40), 20)

if __name__ == "__main__":
    main(search_term, search_list, "pysearch")
    main(search_term, search_list, "binary")
    

