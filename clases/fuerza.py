import math

class Fuerza:
    def __init__(self, magnitud, angulo, x, z):
        if not all(math.isfinite(v) for v in (magnitud, angulo, x, z)):
            raise ValueError('Los datos deben ser finitos.')
        if magnitud < 0 or not 0 <= angulo <= 360:
            raise ValueError('Magnitud no negativa y ángulo entre 0 y 360 grados.')
        self.magnitud = magnitud
        self.angulo = angulo
        self.x = x
        self.z = z

    def componentes(self):
        a = math.radians(self.angulo)
        return self.magnitud * math.cos(a), self.magnitud * math.sin(a)

    def momento(self):
        fx, fz = self.componentes()
        return self.z * fx - self.x * fz
