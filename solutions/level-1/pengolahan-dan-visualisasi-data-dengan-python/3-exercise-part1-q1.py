import unittest
import pandas as pd
from challenge import get_stat_by_album


class TestExercisePart1(unittest.TestCase):
    data = pd.read_csv('spotify_taylorswift.csv', delimiter = ',')

    def test_one(self):
        columns =  ['popularity', 'danceability', 'acousticness', 'energy',
                    'instrumentalness', 'speechiness', 'valence', 'tempo']
        expected = pd.melt(self.data, id_vars=['album'], value_vars=columns, var_name='indicator') \
            .groupby(['album', 'indicator']) \
            .agg(mean = ('value', 'mean'), min = ('value', 'min'), median = ('value', 'median'), max = ('value', 'max')) \
            .reset_index()
        pd.testing.assert_frame_equal(get_stat_by_album(self.data), expected) 


if __name__ == '__main__':
    unittest.main(exit=False)