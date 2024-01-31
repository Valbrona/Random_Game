import unittest
import randgame

class TestGame(unittest.TestCase):
    def test_input(self):
        result = randgame.run_guess(5,5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = randgame.run_guess(5,1)
        self.assertFalse(result)

    def test_input_wrong_answer(self):
        result = randgame.run_guess(5,11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = randgame.run_guess(5,"11")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()