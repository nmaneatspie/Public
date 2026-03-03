"""

Practice with class/OOP

Creates a "container" that houses an integer array.
Manipulation of the array through the class's methods.

Returns:
    None:
"""

import sys


class Container:
    def __init__(self):
        self.num_arr: list[int] = []

    def add(self, value: str) -> str:
        # add a value to the container and return empty string
        self.num_arr.append(int(value))
        return ""

    def exists(self, value: str) -> str:
        #  return "true" if value exists in container else "false"
        if int(value) in self.num_arr:
            return "true"
        else:
            return "false"

    def remove(self, value: str) -> str:
        # remove only a single occurence of the value from the container
        try:
            idx = self.num_arr.index(int(value))

            del self.num_arr[idx]

            return "true"
        except Exception:
            return "false"

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


def translate_query(cont: Container, query: list) -> str:
    match query[0]:
        case "ADD":
            return cont.add(query[1])
        case "EXISTS":
            return cont.exists(query[1])
        case "REMOVE":
            return cont.remove(query[1])
        case "GET_NEXT":
            return cont.get_next(query[1])
        case _:
            raise Exception


def solution(queries) -> list[str]:

    c1 = Container()

    results = []

    for i in queries:
        results.append(translate_query(c1, i))

    return results


def main() -> None:
    queries = [
        ["ADD", "0"],
        ["ADD", "1"],
        ["ADD", "1"],
        ["ADD", "11"],
        ["ADD", "22"],
        ["ADD", "3"],
        ["ADD", "5"],
        ["GET_NEXT", "0"],
        ["GET_NEXT", "1"],
        ["REMOVE", "1"],
        ["GET_NEXT", "1"],
        ["ADD", "0"],
        ["ADD", "1"],
        ["ADD", "2"],
        ["ADD", "1"],
        ["GET_NEXT", "1"],
        ["GET_NEXT", "2"],
        ["GET_NEXT", "3"],
        ["GET_NEXT", "5"],
    ]

    expected_results = [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "1",
        "3",
        "true",
        "3",
        "",
        "",
        "",
        "",
        "2",
        "3",
        "5",
        "11",
    ]

    results = solution(queries)

    # testing
    for i in results:
        if i != expected_results[results.index(i)]:
            raise Exception


if __name__ == "__main__":
    main()
