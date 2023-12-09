import unittest
from day_2_problem_1 import is_game_possible, add_cubes_by_color

class TestCubeGame(unittest.TestCase):

    def test_is_game_possible(self):
        self.assertTrue(is_game_possible(10, 10, 10))
        self.assertTrue(is_game_possible(12, 13, 14))   # max values
        self.assertFalse(is_game_possible(15, 13, 14))  # r exceeds max
        self.assertFalse(is_game_possible(12, 14, 15))  # g exceeds max
        self.assertFalse(is_game_possible(12, 13, 15))  # b exceeds max

    def test_add_cubes_by_color(self):
        self.assertEqual(add_cubes_by_color("3 red, 4 green, 5 blue"), (3, 4, 5))
        self.assertEqual(add_cubes_by_color("12 red, 13 green, 14 blue"), (12, 13, 14))  # max values
        self.assertEqual(add_cubes_by_color("15 red, 13 green, 14 blue"), (15, 13, 14))  # red exceeds max
        self.assertEqual(add_cubes_by_color("12 red, 14 green, 14 blue"), (12, 14, 14))  # green exceeds max
        self.assertEqual(add_cubes_by_color("12 red, 13 green, 15 blue"), (12, 13, 15))  # blue exceeds max

if __name__ == '__main__':
    unittest.main()