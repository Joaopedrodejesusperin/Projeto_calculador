import unittest
from Calculadora import Calculadora
 
class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculadora()
    
    def test_soma(self):
        self.assertEqual(self.calc.soma(2, 3), 5)
    
    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(5, 2), 3)
    
    def test_multiplicacao(self):
        self.assertEqual(self.calc.multiplicacao(4, 3), 12)
    
    def test_divisao(self):
        self.assertEqual(self.calc.divisao(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calc.divisao(10, 0)
    
if __name__ == '__main__':
    unittest.main()