import unittest
from Calculadora import restaFraccion, sumaFraccion, multiplicacionFraccion, divisionFraccion

class TestFraccion(unittest.TestCase):
    
    def test_suma(self):
        self.assertAlmostEqual(sumaFraccion(3,4,5,5), [35,20])

    def test_resta(self):
        self.assertAlmostEqual(restaFraccion(5,5,5,5), [25,25])
    
    def test_multiplicacionFraccion(self):
        self.assertAlmostEqual(multiplicacionFraccion(5,5,5,5), [25,25])
    
    def test_divisionFraccion(self):
        self.assertAlmostEqual(divisionFraccion(5,5,5,5), (25,25))