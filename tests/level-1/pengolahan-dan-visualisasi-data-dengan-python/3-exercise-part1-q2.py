import unittest
import pandas as pd
from challenge import top_song_by_indicators


class TestExercisePart2(unittest.TestCase):
    data = pd.read_csv('spotify_taylorswift.csv', delimiter = ',')
   
    def test_one(self):
        expected = pd.DataFrame({
            'name': ['It’s Nice To Have A Friend', 'I Think He Knows', 'Haunted', 'long story short', 'Blank Space', 
                     'I Wish You Would - Voice Memo', 'Soon You’ll Get Better (feat. The Chicks)', 'Shake It Off'],
            'indicator': ['acousticness', 'danceability', 'energy', 'instrumentalness', 'popularity', 'speechiness', 'tempo', 'valence'],
            'value': [0.971, 0.897, 0.944, 0.179, 82.0, 0.912, 207.476, 0.942]
        })
        pd.testing.assert_frame_equal(top_song_by_indicators(self.data), expected)


if __name__ == '__main__':
    unittest.main(exit=False)