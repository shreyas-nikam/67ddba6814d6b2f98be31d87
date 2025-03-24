import unittest
from pages.bond_pricing import calculate_bond_price

class TestBondPricing(unittest.TestCase):
    def test_bond_price(self):
        # With coupon_rate=0.05, maturity=10, face_value=1000, ytm=0.05, the bond price should be near par.
        price = calculate_bond_price(0.05, 10, 1000, 0.05)
        # Expected value is approximately 1000 (allowing for numerical tolerance)
        self.assertAlmostEqual(price, 1000, delta=50)

if __name__ == '__main__':
    unittest.main()
