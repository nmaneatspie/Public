"""

Practice with class/OOP

Takes in string 2D string list, first value being the method/instruction, and second being the value.
The manipulated object is an integer container, though it accepts string values and outputs string values.

"""

from Practice_OOP.src.container import IntContainer
import argparse


def translate_query(cont: IntContainer, query: list) -> str:
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

    c1 = IntContainer()

    results = []

    for i in queries:
        results.append(translate_query(c1, i))

    return results


def main(in_queries) -> list[str]:

    queries = [eval(q) for q in in_queries]

    return solution(queries)


parser = argparse.ArgumentParser("OOP Practice")
parser.add_argument(
    "queries",
    help='Queries to process in the format \'["ADD", "0"]\' \'["ADD", "1"]\' ...',
    type=str,
    nargs="+",
    default=None,
)
args = parser.parse_args()

if __name__ == "__main__":
    main(args.queries)
