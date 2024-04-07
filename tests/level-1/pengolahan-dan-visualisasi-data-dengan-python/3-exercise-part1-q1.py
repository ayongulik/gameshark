import unittest
import pandas as pd
from challenge import get_stat_by_album


class TestExercisePart1(unittest.TestCase):
    def __init__(self):
        self.data = pd.read_csv('https://raw.githubusercontent.com/ayongulik/gameshark/master/data/spotify_taylorswift.csv', delimiter = ',')
        super(self)

    def test_one(self):
        result = get_stat_by_album(self.data)
        expected = pd.melt(self.data, id_vars=['album'], value_vars=self.data.columns, var_name='indicator') \
            .groupby(['album', 'indicator']) \
            .agg(mean = ('value', 'mean'), min = ('value', 'min'), median = ('value', 'median'), max = ('value', 'max')) \
            .reset_index()
        pd.testing.assert_frame_equal(result, expected) 


if __name__ == '__main__':
    unittest.main(exit=False)