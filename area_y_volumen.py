import math
class figura():
    def __init__(self):
        pass

    def calc_area():
        pass

    def calc_perimetro():
        pass

class circulo(figura):
    def __init__(self,radio):

        self.radio = radio

    def calc_area(self):
        return 2*math.pi*self.radio**2
    def calc_perimetro(self):
        return 2*math.pi*self.radio

class cuadrado(figura):
    def __init__(self,lado):

        self.lado = lado

    def calc_area(self):
        return self.lado*self.lado
    def calc_perimetro(self):
        return 4*self.lado

class rectangulo(figura):
    def __init__(self,lado_M,lado_m):
        self.lado_M = lado_M
        self.lado_m = lado_m
    def calc_area(self):
        return self.lado_M*self.lado_m
    def calc_perimetro(self):
        return 2*self.lado_m + 2*self.lado_M
c=circulo(5)
print("El area del circulo es: ",c.calc_area())
print("El perimetro del circulo es: ",c.calc_perimetro())

p =cuadrado(3)
print("El area del cuadrado es: ",p.calc_area())
print("El perimetro del cuadrado es: ",p.calc_perimetro())

r =rectangulo(4,3)
print("El area del rectangulo es: ",r.calc_area())
print("El perimetro del rectangulo es: ",r.calc_perimetro())
