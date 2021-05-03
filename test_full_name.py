import unittest
import full_name

class testName(unittest.TestCase):
        def test_name(self):
            result = full_name.full_name("Snoop", "Dogg")
            self.assertEqual(result, "Snoop Dogg")

        def test_name_fail(self):
            result = full_name.full_name("Snoop", "Dogg")
            self.assertEqual(result, "SnoopDogg")

        def test_name_fail_2(self):
            result = full_name.full_name("Snoop", "Dogg")
            self.assertEqual(result, "Dogg Snoop")