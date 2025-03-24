import unittest
from pages import bond_pricing, yield_curve, explanation

class TestIntegration(unittest.TestCase):
    def test_pages_exist(self):
        self.assertTrue(hasattr(bond_pricing, 'app'))
        self.assertTrue(hasattr(yield_curve, 'app'))
        self.assertTrue(hasattr(explanation, 'app'))

if __name__ == '__main__':
    unittest.main()
