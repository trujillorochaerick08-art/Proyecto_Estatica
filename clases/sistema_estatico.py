import math

class SistemaEstatico:
    def __init__(self):
        self.fuerzas = []

    def agregar(self, fuerza):
        self.fuerzas.append(fuerza)

    def resultante(self):
        sx = sz = 0.0
        for fuerza in self.fuerzas:
            fx, fz = fuerza.componentes()
            sx += fx
            sz += fz
        return sx, sz, math.hypot(sx, sz)

    def momento_total(self):
        return sum(f.momento() for f in self.fuerzas)

    def equilibrio(self):
        sx, sz, _ = self.resultante()
        return bool(self.fuerzas) and abs(sx) <= 1e-6 and abs(sz) <= 1e-6 and abs(self.momento_total()) <= 1e-6

    def eliminar(self, indice):
        if not 1 <= indice <= len(self.fuerzas):
            raise ValueError('Número de fuerza inexistente.')
        self.fuerzas.pop(indice - 1)
