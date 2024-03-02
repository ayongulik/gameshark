import unittest
import functools
from challenge import get_sum

data = [
    {
        'id': 1,
        'product_name': 'Soft overcoat coat',
        'category': 'coat',
        'price': 65.95,
        'stock': 120,
        'sold': 30
    },
    {
        'id': 2,
        'product_name': 'High neck knit sweater',
        'category': 'sweater',
        'price': 39.95,
        'stock': 49,
        'sold': 0
    },
    {
        'id': 3,
        'product_name': 'Wide-leg jumpsuit with golden buttons',
        'category': 'pants',
        'price': 55.95,
        'stock': 100,
        'sold': 50
    },
    {
        'id': 4,
        'product_name': 'Wide-leg trousers with drawstring waistband',
        'category': 'pants',
        'price': 39.95,
        'stock': 83,
        'sold': 125
    },
    {
        'id': 5,
        'product_name': 'Mom Jeans',
        'category': 'pants',
        'price': 29.95,
        'stock': 5,
        'sold': 234
    },
    {
        'id': 6,
        'product_name': 'Soft oversize coat',
        'category': 'coat',
        'price': 69.95,
        'stock': 124,
        'sold': 12
    },
    {
        'id': 7,
        'product_name': 'ZW collection trench coat with belt',
        'category': 'coat',
        'price': 89.95,
        'stock': 95,
        'sold': 97
    },
    {
        'id': 8,
        'product_name': 'Contrast knit sweater',
        'category': 'sweater',
        'price': 39.95,
        'stock': 2,
        'sold': 55
    },
    {
        'id': 9,
        'product_name': 'Sweatshirt with rhinestone slogan',
        'category': 'sweater',
        'price': 39.95,
        'stock': 24,
        'sold': 135
    },
    {
        'id': 10,
        'product_name': 'High waist boot-cut jeans',
        'category': 'pants',
        'price': 39.95,
        'stock': 2,
        'sold': 143
    }
]


class TestExercisePart3(unittest.TestCase):

    def test_one(self):
        self.assertEqual(get_sum(data, 'sold'), 881)
    
    def test_two(self):
        self.assertEqual(get_sum(data, 'stock'), 604)
    
    def test_three(self):
        self.assertEqual(get_sum(data, 'price'), 511.49999999999994)
        

if __name__ == '__main__':
    unittest.main(exit=False)