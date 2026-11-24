import unittest
from clases.fuerza import Fuerza
from clases.sistema_estatico import SistemaEstatico

class Pruebas(unittest.TestCase):
    def test_01_original(self):
        f = Fuerza(700,20,4,0)
        self.assertAlmostEqual(f.componentes()[0],657.7848,places=3)
        self.assertAlmostEqual(f.componentes()[1],239.4141,places=3)
        self.assertAlmostEqual(f.momento(),-957.6564,places=3)
    def test_02_normal(self):
        f = Fuerza(100,90,2,0)
        self.assertAlmostEqual(f.momento(),-200)
    def test_03_limite(self):
        f = Fuerza(0,360,0,0)
        self.assertEqual(f.momento(),0)
    def test_04_invalido(self):
        with self.assertRaises(ValueError): Fuerza(-100,90,2,0)
    def test_05_equilibrio(self):
        s = SistemaEstatico()
        s.agregar(Fuerza(100,90,2,0))
        s.agregar(Fuerza(100,270,2,0))
        self.assertTrue(s.equilibrio())
        self.assertAlmostEqual(s.resultante()[2],0)
        s.eliminar(2)
        self.assertFalse(s.equilibrio())

if __name__ == '__main__': unittest.main(verbosity=2)
