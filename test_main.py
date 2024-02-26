import unittest
import random

from main import Node, ModuloForceCalculator, ScprForceCalculator

class TestForceCalculationQuadrant1(unittest.TestCase):
    """ Test that the two different calculation methods are identical """

    # Tests for quadrant 1:
        # x1 < x2
        # y1 > y2
        # 0 < phi_1 < phi_2 < PI
    
    def setUp(self):
        self.random_node = Node(random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 360))
        self.node_1 = Node(2, 8, 45)
        self.node_2 = Node(8, 2, 80)

        self.r = 0.15
        self.fmyo = 4

        self.mod_calculator = ModuloForceCalculator(self.node_1, self.node_2, self.r, self.fmyo)
        self.scpr_calculator = ScprForceCalculator(self.node_1, self.node_2, self.r, self.fmyo)
    
    def test_lx_is_same(self):
        """ Check that calculators agree on lx """
        mod_lx = self.mod_calculator.lx()
        scpr_lx = self.scpr_calculator.lx()
        self.assertEqual(mod_lx, scpr_lx)

    def test_ly_is_same(self):
        """ Check that calculators agree on ly """
        mod_ly = self.mod_calculator.ly()
        scpr_ly = self.scpr_calculator.ly()
        self.assertEqual(mod_ly, scpr_ly)
    
    def test_lphi_is_same(self):
        """ Check that calculators agree on lphi """
        mod_lphi = self.mod_calculator.lphi()
        scpr_lphi = self.scpr_calculator.lphi()
        self.assertEqual(mod_lphi, scpr_lphi)

class TestForceCalculationQuadrant2(unittest.TestCase):
    """ Test that the two different calculation methods are identical """

    # Tests for quadrant 2:
        # x1 < x2
        # y1 < y2
        # 0 < phi_1 < phi_2 < PI
    
    def setUp(self):
        self.random_node = Node(random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 360))
        self.node_1 = Node(2, 6, 45)
        self.node_2 = Node(4, 8, 80)

        self.r = 0.15
        self.fmyo = 4

        self.mod_calculator = ModuloForceCalculator(self.node_1, self.node_2, self.r, self.fmyo)
        self.scpr_calculator = ScprForceCalculator(self.node_1, self.node_2, self.r, self.fmyo)
    
    def test_lx_is_same(self):
        """ Check that calculators agree on lx """
        mod_lx = self.mod_calculator.lx()
        scpr_lx = self.scpr_calculator.lx()
        self.assertEqual(mod_lx, scpr_lx)

    def test_ly_is_same(self):
        """ Check that calculators agree on ly """
        mod_ly = self.mod_calculator.ly()
        scpr_ly = self.scpr_calculator.ly()
        self.assertEqual(mod_ly, scpr_ly)
    
    def test_lphi_is_same(self):
        """ Check that calculators agree on lphi """
        mod_lphi = self.mod_calculator.lphi()
        scpr_lphi = self.scpr_calculator.lphi()
        self.assertEqual(mod_lphi, scpr_lphi)

class TestForceCalculationQuadrant3(unittest.TestCase):
    """ Test that the two different calculation methods are identical """

    # Tests for quadrant 1:
        # x1 > x2
        # y1 > y2
        # 0 < phi_1 < phi_2 < PI
    
    def setUp(self):
        self.random_node = Node(random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 360))
        self.node_1 = Node(8, 8, 45)
        self.node_2 = Node(2, 2, 80)

        self.r = 0.15
        self.fmyo = 4

        self.mod_calculator = ModuloForceCalculator(self.node_1, self.node_2, self.r, self.fmyo)
        self.scpr_calculator = ScprForceCalculator(self.node_1, self.node_2, self.r, self.fmyo)
    
    def test_lx_is_same(self):
        """ Check that calculators agree on lx """
        mod_lx = self.mod_calculator.lx()
        scpr_lx = self.scpr_calculator.lx()
        self.assertEqual(mod_lx, scpr_lx)

    def test_ly_is_same(self):
        """ Check that calculators agree on ly """
        mod_ly = self.mod_calculator.ly()
        scpr_ly = self.scpr_calculator.ly()
        self.assertEqual(mod_ly, scpr_ly)
    
    def test_lphi_is_same(self):
        """ Check that calculators agree on lphi """
        mod_lphi = self.mod_calculator.lphi()
        scpr_lphi = self.scpr_calculator.lphi()
        self.assertEqual(mod_lphi, scpr_lphi)

class TestForceCalculationQuadrant4(unittest.TestCase):
    """ Test that the two different calculation methods are identical """

    # Tests for quadrant 1:
        # x1 > x2
        # y1 < y2
        # 0 < phi_1 < phi_2 < PI
    
    def setUp(self):
        self.random_node = Node(random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 360))
        self.node_1 = Node(8, 2, 45)
        self.node_2 = Node(2, 8, 80)

        self.r = 0.15
        self.fmyo = 4

        self.mod_calculator = ModuloForceCalculator(self.node_1, self.node_2, self.r, self.fmyo)
        self.scpr_calculator = ScprForceCalculator(self.node_1, self.node_2, self.r, self.fmyo)
    
    def test_lx_is_same(self):
        """ Check that calculators agree on lx """
        mod_lx = self.mod_calculator.lx()
        scpr_lx = self.scpr_calculator.lx()
        self.assertEqual(mod_lx, scpr_lx)

    def test_ly_is_same(self):
        """ Check that calculators agree on ly """
        mod_ly = self.mod_calculator.ly()
        scpr_ly = self.scpr_calculator.ly()
        self.assertEqual(mod_ly, scpr_ly)
    
    def test_lphi_is_same(self):
        """ Check that calculators agree on lphi """
        mod_lphi = self.mod_calculator.lphi()
        scpr_lphi = self.scpr_calculator.lphi()
        self.assertEqual(mod_lphi, scpr_lphi)

if __name__ == "__main__":
    unittest.main()