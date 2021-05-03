import unittest
import average_list

class testList(unittest.TestCase):
        def test_list(self):
            result = average_list.average_list(1, 2, 3)
            self.assertEqual(result,2)

        def test_list_2(self):
            result = average_list.average_list(1, 1, 1)
            self.assertEqual(result,1)

        def test_list_fail(self):
            result = average_list.average_list(0, 1, -2)
            self.assertEqual(result,1)