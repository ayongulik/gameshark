import io
import unittest
from unittest.mock import patch
from challenge import main


class TestExercisePart1(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main(True, True, 2, 200, 'UHasselt')
        expected_out = 'Diterima!\n'
        self.assertEqual(stdout.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main(True, True, 2, 200, 'BSI')
        expected_out = 'Diterima!\n'
        self.assertEqual(stdout.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main(True, True, 2, 100, 'Unpar')
        expected_out = 'Diterima!\n'
        self.assertEqual(stdout.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_four(self, stdout):
        main(True, False, 2, 200, 'Unpar')
        expected_out = 'Ditolak~\n'
        self.assertEqual(stdout.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_five(self, stdout):
        main(True, True, 5, 200, 'Unpar')
        expected_out = 'Diterima!\n'
        self.assertEqual(stdout.getvalue(), expected_out)


if __name__ == '__main__':
    unittest.main(exit=False)