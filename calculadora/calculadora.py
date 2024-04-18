import unittest
import math
class Calculadora_cientifica:   
    def __init__(self):
        self.ultimo_resultado = None
    
    def seno(self, ang):
        self.ultimo_resultado = math.sin(math.radians(ang))
        return self.ultimo_resultado
    
    def coseno(self, ang):
        self.ultimo_resultado = math.cos(math.radians(ang))
        return self.ultimo_resultado
    
    def tangente(self, ang):
        self.ultimo_resultado = math.tan(math.radians(ang))
        if ang == 90:
            raise ValueError("ERRO a tangente não existe.")
        return self.ultimo_resultado


class Teste(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculadora_cientifica()

    def teste_seno(self):
        self.assertEqual(self.calc.seno(30),0.49999999999999994)
        

    def teste_coseno(self):
        self.assertEqual(self.calc.coseno(30),0.8660254037844387)


    def teste_tangente(self):
        self.assertEqual(self.calc.tangente(30),0.5773502691896257)        
        with self.assertRaises(ValueError):
            self.calc.tangente(90)   

if __name__ == '__main__':
    unittest.main()   