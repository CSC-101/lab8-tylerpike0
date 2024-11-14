import unittest
import group

class MyTestCase(unittest.TestCase):
    def test_groups_of_3_1(self):
        input = [1,2,3,4,5,6,7,8,9]
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        actual = group.groups_of_3(input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_groups_of_3_2(self):
        input = [1,2,3,4,5,6,7,8]
        expected = [[1, 2, 3], [4, 5, 6], [7, 8]]
        actual = group.groups_of_3(input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_groups_of_3_3(self):
        input = []
        expected = []
        actual = group.groups_of_3(input)
        self.assertEqual(expected, actual)  # add assertion here

if __name__ == '__main__':
    unittest.main()
