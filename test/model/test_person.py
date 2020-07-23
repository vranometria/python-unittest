import unittest
from model.person import Person

class ModelTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_age(self):
        m = Person('takasi',18)

        self.assertEqual(18,m.age)