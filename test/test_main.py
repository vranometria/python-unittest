import unittest
from main import add,deg

class AddTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_add(self):
        self.assertEqual( 3 , add(1,2))

    def test_deg(self):
        self.assertEqual( 4, deg(10,6) )