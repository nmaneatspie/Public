import unittest
from Practice_OOP.src.container import IntContainer


class TestIntContainer(unittest.TestCase):
    def setUp(self):
        self.c1 = IntContainer()

    def test_add(self):
        self.assertEqual(self.c1.add("1"), "")
        self.assertEqual(self.c1.add("-1"), "")

        with self.assertRaises(ValueError):
            self.c1.add("1e3")

    def test_remove(self):
        self.c1.add("1")
        self.c1.add("2")
        self.c1.add("3")
        self.assertEqual(self.c1.remove("2"), "true")

        with self.assertRaises(ValueError):
            self.c1.add("#13")

    def test_exists(self):
        self.c1.add("1")
        self.assertEqual(self.c1.exists("1"), "true")
        self.assertEqual(self.c1.exists("0"), "false")

        with self.assertRaises(ValueError):
            self.c1.add("$20")

    def test_get_next(self):
        self.c1.add("1")
        self.c1.add("2")
        self.c1.add("3")
        self.assertEqual(self.c1.get_next("1"), "2")
        self.assertEqual(self.c1.get_next("2"), "3")
        self.assertEqual(self.c1.get_next("3"), "")

        with self.assertRaises(ValueError):
            self.c1.add("'13")


if __name__ == "__main__":
    unittest.main()
