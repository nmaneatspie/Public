"""
Norman TXXXX
Date created: 23/10/2020
Last Modified: 14/02/2026

Code used to complete mission 1 of the programming challenge on hackthissite.com
Essentially recieves input strings in file and tries to unjumble them to one of the words
in the included dictionary file. Code assumes the jumbled word has unjumbled solution
in the file.

sys.exit code 1 should log error to file
sys.exit code 2 has issues logging error
"""

# Library imports
import sys
import datetime
from functools import wraps
import time
import argparse


# Functions
def time_process(func):
    """Decorator for timing how long it takes a function to run"""

    @wraps(func)
    def timed(*args, **kwargs) -> None:

        start = time.process_time()
        func(*args, **kwargs)
        end = time.process_time()

        print(
            "{:e} seconds to complete function: {}".format(end - start, func.__name__),
            "\n",
        )

    return timed


def error_log(
    err_num: int,
    filename: str = "",
) -> None:
    """Error logging code: file related"""

    if err_num == -1:  # Prevent looping when writing error to log
        sys.exit([2])

    err_msg = {
        1: "Error opening file {}".format(filename),
        2: "Error with reading from {}".format(filename),
        3: "Error with closing {}".format(filename),  # no longer used
        4: "Error writing to file {}".format(filename),
    }

    try:
        with open(filename, -1) as file:
            file.write("{} ".format(datetime.datetime.now()))
            file.write("{}\n".format(err_msg.get(err_num)))
    except Exception:
        sys.exit([2])
    sys.exit([1])


def load_dictionary(dictionary_file: str) -> list[str]:
    """Load dictionary words from file"""

    dictionary_list: list[str] = []
    try:
        with open(dictionary_file, "r") as file:
            try:
                for x in file:  # Dictionary file has each word on it's own line
                    dictionary_list.append(x.rstrip())
            except Exception:
                error_log(2, dictionary_file)
    except Exception:
        error_log(1, dictionary_file)

    return dictionary_list


def load_jumbled(jumbled_file: str) -> list[str]:
    """Load jumbled words from file"""

    jumbled_list: list[str] = []
    try:
        with open(jumbled_file, "r") as file:
            try:
                for x in file:
                    jumbled_list.append(x.rstrip())
            except Exception:
                print("here")
                error_log(2, jumbled_file)
    except Exception:
        error_log(1, jumbled_file)

    if len(jumbled_list) == 0:
        print("No jumbled words inputted")

    return jumbled_list


def unjumble(
    search_type: int,
    jumbled_list: list[str],
    dictionary_list: list[str],
) -> None:
    """Process for unjumbling words"""

    match search_type:
        case 0:
            simple_search(
                jumbled_list,
                dictionary_list,
            )  # default
        case 1:
            other_search(
                jumbled_list,
                dictionary_list,
            )
        case 2:  # both methods
            simple_search(
                jumbled_list,
                dictionary_list,
            )
            other_search(
                jumbled_list,
                dictionary_list,
            )
        case _:
            simple_search(
                jumbled_list,
                dictionary_list,
            )


@time_process
def other_search(
    jumbled_list: list[str],
    dict_list: list[str],
) -> None:
    """
    1.Find equal length words
    2.Sort words and check if equal
    """

    for x in jumbled_list:
        sorted_word = sorted(x)
        len_x = len(x)
        found: bool = False
        for y in dict_list:
            if len(y) == len_x:
                temp = sorted(y)
                if temp == sorted_word:
                    print("{}, Found: {}".format(x, y))
                    found = True
                    break
            else:
                continue
        if not found:
            print("{}, Not Found".format(x))

    print("\n")


@time_process
def simple_search(
    jumbled_list: list[str],
    dict_list: list[str],
) -> None:
    """go through each letter and compare"""

    for jumbled_word in jumbled_list:
        found_word: bool = False
        len_jumbled = len(jumbled_word)
        for dict_word in dict_list:
            same_word: bool = True
            if len_jumbled != len(dict_word):
                same_word = False
                continue

            for j_letter in jumbled_word:
                found_letter = False
                for d_letter in dict_word:
                    if d_letter == j_letter:
                        found_letter = True
                        break
                    else:
                        continue
                if found_letter:
                    continue
                else:
                    same_word = False
                    break

            if same_word:
                found_word = True
                break
        if found_word:
            print("{}, Found: {}".format(jumbled_word, dict_word))
        else:
            print("{}, Not Found".format(jumbled_word))

    print("\n")


@time_process
def main(search_type: int = 0) -> None:
    """Main Code"""

    dictionary_file: str = "dictionary.txt"
    jumbled_file: str = "jumbled.txt"
    # results_file: str = "results.txt"
    jumbled_list: list[str] = []

    dictionary_list: list[str] = load_dictionary(dictionary_file)
    jumbled_list: list[str] = load_jumbled(jumbled_file)

    if len(jumbled_list) == 0:
        return
    else:
        unjumble(search_type, jumbled_list, dictionary_list)


# Setup Parsing arguments to this file
parser = argparse.ArgumentParser("findfromlist")
parser.add_argument(
    "search_type",
    help="Integer to select search type. 0: simple search, 1: other search",
    type=int,
    default=0,
)
args = parser.parse_args()


if __name__ == "__main__":
    main(args.search_type)
