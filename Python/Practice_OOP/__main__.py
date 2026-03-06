from Practice_OOP.src.main import main as oop
import argparse


def main(in_queries):
    results = oop(in_queries)
    print(results)


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
