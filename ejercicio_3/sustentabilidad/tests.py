import unittest

from .emisiones import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_normal(self):
        resultado = calcular_emisiones_carbono(100)
        self.assertEqual(resultado, 40)

    def test_calculo_con_otro_valor(self):
        resultado = calcular_emisiones_carbono(250)
        self.assertEqual(resultado, 100)

    def test_consumo_cero(self):
        resultado = calcular_emisiones_carbono(0)
        self.assertEqual(resultado, 0)

    def test_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50)