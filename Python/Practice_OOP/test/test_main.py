import unittest
from Practice_OOP.src.main import translate_query, solution
from Practice_OOP.src.container import IntContainer

class TestTranslateQuery(unittest.TestCase):
    def setUp(self):
        self.c1 = IntContainer()

    def test_add(self):
        result = translate_query(self.c1, ["ADD", "0"])
        self.assertEqual(result, "")

        result = translate_query(self.c1, ["ADD", "-1"])
        self.assertEqual(result, "")

        with self.assertRaises(ValueError):
            result = translate_query(self.c1, ["ADD", "$1"])

    def test_remove(self):
        self.c1.add("0")
        self.c1.add("1")
        self.c1.add("2")
        result = translate_query(self.c1, ["REMOVE", "1"])
        self.assertEqual(result, "true")

        result = translate_query(self.c1, ["REMOVE", "1"])
        self.assertEqual(result, "false")

        with self.assertRaises(ValueError):
            result = translate_query(self.c1, ["ADD", "rs"])

    def test_exists(self):
        self.c1.add("0")
        result = translate_query(self.c1, ["EXISTS", "0"])
        self.assertEqual(result, "true")

        result = translate_query(self.c1, ["EXISTS", "1"])
        self.assertEqual(result, "false")

        with self.assertRaises(ValueError):
            result = translate_query(self.c1, ["ADD", "#'"])

    def test_get_next(self):
        self.c1.add("0")
        self.c1.add("1")
        self.c1.add("2")
        result = translate_query(self.c1, ["GET_NEXT", "0"])
        self.assertEqual(result, "1")

        result = translate_query(self.c1, ["GET_NEXT", "2"])
        self.assertEqual(result, "")

        with self.assertRaises(ValueError):
            result = translate_query(self.c1, ["ADD", "1u2"])

    def test_invalid_query(self):
        with self.assertRaises(Exception):
            translate_query(self.c1, ["INVALID", "0"])
        with self.assertRaises(Exception):
            translate_query(self.c1, ["INVALID", "$"])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.queries = [
            ["ADD", "0"],
            ["ADD", "1"],
            ["ADD", "2"],
            ["EXISTS", "0"],
            ["REMOVE", "0"],
            ["GET_NEXT", "1"],
        ]

    def test_solution(self):

        self.assertEqual(
            solution(self.queries),
            [
                "",
                "",
                "",
                "true",
                "true",
                "2",
            ],
        )


if __name__ == "__main__":
    unittest.main()
