import unittest
import cube_volume

class testVol(unittest.TestCase):
        def test_vol(self):
            result = cube_volume.volume(3)
            self.assertEqual(result,27)

        def test_vol_2(self):
            result = cube_volume.volume(0)
            self.assertEqual(result,0)

        def test_vol_fail(self):
            result = cube_volume.volume(3)
            self.assertEqual(result,9)