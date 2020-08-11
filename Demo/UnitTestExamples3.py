import unittest
from Examples import Example

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(Example):
        print("setUpClass executed")

    def setUp(self) -> None:
        print("setUp executed")

    def test_add(self):
        self.assertEqual(Example.add(self, 10, 20), 30)
        self.assertEqual(Example.add(self, 10, 20), 30)
        print("test_add executed")

    def test_sub(self):
        self.assertEqual(Example.sub(self, 50, 20), 30)
        self.assertEqual(Example.sub(self, 50, 20), 30)
        print("test_sub executed")

    def test_mix(self):
        print("test_mix executed")

    def tearDown(self):
        print("tearDown executed")

    @classmethod
    def tearDownClass(Example):
        print("tearDownClass executed")

#if __name__ == '__main__':
#    unittest.main()
