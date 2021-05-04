import unittest
import average_list

class testList(unittest.TestCase):
        def test_list(self):
            result = average_list.average_list(av_list = [1, 2, 3])
            self.assertEqual(result,2)

        def test_list_fail(self):
            result = average_list.average_list(av_list = [])
            self.assertEqual(result,0)

        def test_list_fail_2(self):
            result = average_list.average_list(av_list = [0, 1, -2])
            self.assertEqual(result,1)