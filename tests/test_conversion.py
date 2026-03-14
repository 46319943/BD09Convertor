import unittest

from bd09convertor import (
    convertMC2LL,
    convertLL2MC,
    convertBD09LL2WGS84,
    convertWGS842BD09LL,
    convertBD09MC2WGS84,
    convertWGS842BD09MC,
)


class ConversionTests(unittest.TestCase):
    def assertClosePair(self, a, b, tol=1e-5):
        self.assertAlmostEqual(a[0], b[0], delta=tol)
        self.assertAlmostEqual(a[1], b[1], delta=tol)

    def test_bd09ll_bd09mc_roundtrip(self):
        ll = (116.274625, 39.961627)
        mc = convertLL2MC(*ll)
        ll_back = convertMC2LL(*mc)
        self.assertClosePair(ll, ll_back, tol=1e-6)

    def test_wgs84_bd09ll_roundtrip(self):
        wgs = (116.274625, 39.961627)
        bd = convertWGS842BD09LL(*wgs)
        wgs_back = convertBD09LL2WGS84(*bd)
        self.assertClosePair(wgs, wgs_back)

    def test_wgs84_bd09mc_roundtrip(self):
        wgs = (116.274625, 39.961627)
        mc = convertWGS842BD09MC(*wgs)
        wgs_back = convertBD09MC2WGS84(*mc)
        self.assertClosePair(wgs, wgs_back)

    def test_bd09ll_bd09mc_roundtrip_negative(self):
        # Negative longitude and latitude to exercise sign handling in BD09LL<->BD09MC
        ll = (-73.985428, -40.748817)
        mc = convertLL2MC(*ll)
        ll_back = convertMC2LL(*mc)
        self.assertClosePair(ll, ll_back, tol=1e-6)

    def test_wgs84_bd09mc_roundtrip_negative(self):
        # Negative longitude and latitude to exercise sign handling in WGS84<->BD09MC
        wgs = (-73.985428, -40.748817)
        mc = convertWGS842BD09MC(*wgs)
        wgs_back = convertBD09MC2WGS84(*mc)
        self.assertClosePair(wgs, wgs_back)


if __name__ == '__main__':
    unittest.main()
