import unittest
import random

from main import Node, ModuloForceCalculator, ScprForceCalculator

# TESTING PHI1 < PHI2

class TestForceCalculationQ1VA(unittest.TestCase):
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
    
        self.msg_suffix = "Q1VA"

    def test_lx_is_same(self):
        """ Check that calculators agree on lx """
        mod_lx = self.mod_calculator.lx()
        scpr_lx = self.scpr_calculator.lx()
        self.assertEqual(mod_lx, scpr_lx, msg=self.msg_suffix)

    def test_ly_is_same(self):
        """ Check that calculators agree on ly """
        mod_ly = self.mod_calculator.ly()
        scpr_ly = self.scpr_calculator.ly()
        self.assertEqual(mod_ly, scpr_ly, msg=self.msg_suffix)
    
    def test_lphi_is_same(self):
        """ Check that calculators agree on lphi """
        mod_lphi = self.mod_calculator.lphi()
        scpr_lphi = self.scpr_calculator.lphi()
        self.assertEqual(mod_lphi, scpr_lphi, msg=self.msg_suffix)

class TestForceCalculationQ2VA(unittest.TestCase):
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
    
        self.msg_suffix = "Q2VB"

    def test_lx_is_same(self):
        """ Check that calculators agree on lx """
        mod_lx = self.mod_calculator.lx()
        scpr_lx = self.scpr_calculator.lx()
        self.assertEqual(mod_lx, scpr_lx, msg=self.msg_suffix)

    def test_ly_is_same(self):
        """ Check that calculators agree on ly """
        mod_ly = self.mod_calculator.ly()
        scpr_ly = self.scpr_calculator.ly()
        self.assertEqual(mod_ly, scpr_ly, msg=self.msg_suffix)
    
    def test_lphi_is_same(self):
        """ Check that calculators agree on lphi """
        mod_lphi = self.mod_calculator.lphi()
        scpr_lphi = self.scpr_calculator.lphi()
        self.assertEqual(mod_lphi, scpr_lphi, msg=self.msg_suffix)

class TestForceCalculationQ3VA(unittest.TestCase):
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

        self.msg_suffix = "Q3VB"

    def test_lx_is_same(self):
        """ Check that calculators agree on lx """
        mod_lx = self.mod_calculator.lx()
        scpr_lx = self.scpr_calculator.lx()
        self.assertEqual(mod_lx, scpr_lx, msg=self.msg_suffix)

    def test_ly_is_same(self):
        """ Check that calculators agree on ly """
        mod_ly = self.mod_calculator.ly()
        scpr_ly = self.scpr_calculator.ly()
        self.assertEqual(mod_ly, scpr_ly, msg=self.msg_suffix)
    
    def test_lphi_is_same(self):
        """ Check that calculators agree on lphi """
        mod_lphi = self.mod_calculator.lphi()
        scpr_lphi = self.scpr_calculator.lphi()
        self.assertEqual(mod_lphi, scpr_lphi, msg=self.msg_suffix)

class TestForceCalculationQ4VA(unittest.TestCase):
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

        self.msg_suffix = "Q4VB"
    
    def test_lx_is_same(self):
        """ Check that calculators agree on lx """
        mod_lx = self.mod_calculator.lx()
        scpr_lx = self.scpr_calculator.lx()
        self.assertEqual(mod_lx, scpr_lx, msg=self.msg_suffix)

    def test_ly_is_same(self):
        """ Check that calculators agree on ly """
        mod_ly = self.mod_calculator.ly()
        scpr_ly = self.scpr_calculator.ly()
        self.assertEqual(mod_ly, scpr_ly, msg=self.msg_suffix)
    
    def test_lphi_is_same(self):
        """ Check that calculators agree on lphi """
        mod_lphi = self.mod_calculator.lphi()
        scpr_lphi = self.scpr_calculator.lphi()
        self.assertEqual(mod_lphi, scpr_lphi, msg=self.msg_suffix)

# TESTING PHI2 - PHI1 > PI (>= 0)

class TestForceCalculationQ1VB(unittest.TestCase):
    """ Test that the two different calculation methods are identical """

    # Tests for quadrant 1:
        # x1 < x2
        # y1 > y2
        # 0 < phi_1 < phi_2
        # phi_2 - phi1 > PI
    
    def setUp(self):
        self.random_node = Node(random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 360))
        self.node_1 = Node(2, 8, 40)
        self.node_2 = Node(8, 2, 240)

        self.r = 0.15
        self.fmyo = 4

        self.mod_calculator = ModuloForceCalculator(self.node_1, self.node_2, self.r, self.fmyo)
        self.scpr_calculator = ScprForceCalculator(self.node_1, self.node_2, self.r, self.fmyo)
        self.msg_suffix = "Q1VB"
    
    def test_lx_is_same(self):
        """ Check that calculators agree on lx """
        mod_lx = self.mod_calculator.lx()
        scpr_lx = self.scpr_calculator.lx()
        self.assertEqual(mod_lx, scpr_lx, msg=self.msg_suffix)

    def test_ly_is_same(self):
        """ Check that calculators agree on ly """
        mod_ly = self.mod_calculator.ly()
        scpr_ly = self.scpr_calculator.ly()
        self.assertEqual(mod_ly, scpr_ly, msg=self.msg_suffix)
    
    def test_lphi_is_same(self):
        """ Check that calculators agree on lphi """
        mod_lphi = self.mod_calculator.lphi()
        scpr_lphi = self.scpr_calculator.lphi()
        self.assertEqual(mod_lphi, scpr_lphi, msg=self.msg_suffix)

class TestForceCalculationQ2VB(unittest.TestCase):
    """ Test that the two different calculation methods are identical """

    # Tests for quadrant 2:
        # x1 < x2
        # y1 < y2
        # 0 < phi_1 < phi_2
        # phi_2 - phi1 > PI
    
    def setUp(self):
        self.random_node = Node(random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 360))
        self.node_1 = Node(2, 6, 40)
        self.node_2 = Node(4, 8, 240)

        self.r = 0.15
        self.fmyo = 4

        self.mod_calculator = ModuloForceCalculator(self.node_1, self.node_2, self.r, self.fmyo)
        self.scpr_calculator = ScprForceCalculator(self.node_1, self.node_2, self.r, self.fmyo)
        self.msg_suffix = "Q2VB"

    def test_lx_is_same(self):
        """ Check that calculators agree on lx """
        mod_lx = self.mod_calculator.lx()
        scpr_lx = self.scpr_calculator.lx()
        self.assertEqual(mod_lx, scpr_lx, msg=self.msg_suffix)

    def test_ly_is_same(self):
        """ Check that calculators agree on ly """
        mod_ly = self.mod_calculator.ly()
        scpr_ly = self.scpr_calculator.ly()
        self.assertEqual(mod_ly, scpr_ly, msg=self.msg_suffix)
    
    def test_lphi_is_same(self):
        """ Check that calculators agree on lphi """
        mod_lphi = self.mod_calculator.lphi()
        scpr_lphi = self.scpr_calculator.lphi()
        self.assertEqual(mod_lphi, scpr_lphi, msg=self.msg_suffix)

class TestForceCalculationQ3VB(unittest.TestCase):
    """ Test that the two different calculation methods are identical """

    # Tests for quadrant 1:
        # x1 > x2
        # y1 > y2
        # 0 < phi_1 < phi_2
        # phi_2 - phi1 > PI
    
    def setUp(self):
        self.random_node = Node(random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 360))
        self.node_1 = Node(8, 8, 40)
        self.node_2 = Node(2, 2, 240)

        self.r = 0.15
        self.fmyo = 4

        self.mod_calculator = ModuloForceCalculator(self.node_1, self.node_2, self.r, self.fmyo)
        self.scpr_calculator = ScprForceCalculator(self.node_1, self.node_2, self.r, self.fmyo)
        
        self.msg_suffix = "Q3VB"
    
    def test_lx_is_same(self):
        """ Check that calculators agree on lx """
        mod_lx = self.mod_calculator.lx()
        scpr_lx = self.scpr_calculator.lx()
        self.assertEqual(mod_lx, scpr_lx, msg=self.msg_suffix)

    def test_ly_is_same(self):
        """ Check that calculators agree on ly """
        mod_ly = self.mod_calculator.ly()
        scpr_ly = self.scpr_calculator.ly()
        self.assertEqual(mod_ly, scpr_ly, msg=self.msg_suffix)
    
    def test_lphi_is_same(self):
        """ Check that calculators agree on lphi """
        mod_lphi = self.mod_calculator.lphi()
        scpr_lphi = self.scpr_calculator.lphi()
        self.assertEqual(mod_lphi, scpr_lphi, msg=self.msg_suffix)

class TestForceCalculationQ4VB(unittest.TestCase):
    """ Test that the two different calculation methods are identical """

    # Tests for quadrant 1:
        # x1 > x2
        # y1 < y2
        # 0 < phi_1 < phi_2
        # phi_2 - phi1 > PI
    
    def setUp(self):
        self.random_node = Node(random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 360))
        self.node_1 = Node(8, 2, 40)
        self.node_2 = Node(2, 8, 240)

        self.r = 0.15
        self.fmyo = 4

        self.mod_calculator = ModuloForceCalculator(self.node_1, self.node_2, self.r, self.fmyo)
        self.scpr_calculator = ScprForceCalculator(self.node_1, self.node_2, self.r, self.fmyo)
    
        self.msg_suffix = "(Q4VB)"

    def test_lx_is_same(self):
        """ Check that calculators agree on lx """
        mod_lx = self.mod_calculator.lx()
        scpr_lx = self.scpr_calculator.lx()
        self.assertEqual(mod_lx, scpr_lx, msg=self.msg_suffix)

    def test_ly_is_same(self):
        """ Check that calculators agree on ly """
        mod_ly = self.mod_calculator.ly()
        scpr_ly = self.scpr_calculator.ly()
        self.assertEqual(mod_ly, scpr_ly, msg=self.msg_suffix)
    
    def test_lphi_is_same(self):
        """ Check that calculators agree on lphi """
        mod_lphi = self.mod_calculator.lphi()
        scpr_lphi = self.scpr_calculator.lphi()
        self.assertEqual(mod_lphi, scpr_lphi, msg=self.msg_suffix)

if __name__ == "__main__":
    unittest.main()