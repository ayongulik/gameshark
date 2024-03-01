import io
import unittest
from unittest.mock import patch
from challenge import main


class TestExercisePart1(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main(6)
        expected_out =  \
"""*
**
***
****
*****
******
"""
        self.assertEqual(stdout.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main(1)
        expected_out = '*\n'
        self.assertEqual(stdout.getvalue(), expected_out)

if __name__ == '__main__':
    unittest.main(exit=False)