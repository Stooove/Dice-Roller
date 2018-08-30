import unittest
from unittest import mock
from io import StringIO
import New_Dice


class TestNewDice(unittest.TestCase):

    @mock.patch('builtins.input', side_effect=[5, 100, 'k', None, 0, -1, 1.2, 2])
    def test_dice_face_prompt(self, mock_input):
        self.assertIsNotNone(New_Dice.dice_face_prompt())
        self.assertIsInstance(New_Dice.dice_face_prompt(),int)
        self.assertIsInstance(New_Dice.dice_face_prompt(), int) # test invalids: 'k', none, 0, -1, 1.2, then positive test ends on 2. Should not accept 'k', None, 0, -1, or 1.2

    @mock.patch('builtins.input', side_effect=[5, 100, 'k', None, 0, -1, 1.2, 2])
    def test_number_of_dice_prompt(self, mock_input):
        self.assertIsNotNone(New_Dice.number_of_dice_prompt()) # test 5
        self.assertIsInstance(New_Dice.number_of_dice_prompt(),int) # test 100
        self.assertIsInstance(New_Dice.number_of_dice_prompt(), int)  # test invalids: 'k', none, 0, -1, 1.2, then positive test ends on 2. Should not accept 'k', None, 0, -1, or 1.2

    def test_roll(self):
        self.assertTrue(1 <= New_Dice.roll(5) <= 5)
        self.assertTrue(1 <= New_Dice.roll(100) <= 100)
        with self.assertRaises(TypeError):
            New_Dice.roll('k')
        with self.assertRaises(TypeError):
            New_Dice.roll(None)
        with self.assertRaises(ValueError):
            New_Dice.roll(0)
        with self.assertRaises(ValueError):
            New_Dice.roll(-1)
        with self.assertRaises(ValueError):
            New_Dice.roll(1.2)

    def test_show_roll(self):
        out_test = StringIO()
        New_Dice.show_roll(5, output=out_test)
        self.assertEqual('You rolled a 5', str(out_test.getvalue().strip()))#strip() default is removing whitespace characters \n

        out_test = StringIO()
        New_Dice.show_roll(100, output=out_test)
        self.assertEqual('You rolled a 100', str(out_test.getvalue().strip()))

        out_test = StringIO()
        New_Dice.show_roll('k', output=out_test)
        self.assertEqual('You rolled a k', str(out_test.getvalue().strip()))

        out_test = StringIO()
        New_Dice.show_roll(None, output=out_test)
        self.assertEqual('You rolled a None', str(out_test.getvalue().strip()))

        out_test = StringIO()
        New_Dice.show_roll(0, output=out_test)
        self.assertEqual('You rolled a 0', str(out_test.getvalue().strip()))

        out_test = StringIO()
        New_Dice.show_roll(-1, output=out_test)
        self.assertEqual('You rolled a -1', str(out_test.getvalue().strip()))

        out_test = StringIO()
        New_Dice.show_roll(1.2, output=out_test)
        self.assertEqual('You rolled a 1.2', str(out_test.getvalue().strip()))


if __name__ == '__main__':
    unittest.main()
