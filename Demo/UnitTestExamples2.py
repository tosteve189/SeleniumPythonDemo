import unittest
from Examples import Example

class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Example.add(self, 10, 20), 30)
        self.assertEqual(Example.add(self, 0, 0), 0)
        self.assertEqual(Example.add(self, -1, 1), 0)

    def test_sub(self):
        self.assertEqual(Example.sub(self, 50, 20), 30)


# if __name__ == '__main__':
#    unittest.main()