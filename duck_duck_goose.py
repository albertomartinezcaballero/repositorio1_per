class producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return self.precio
class medicamento(producto):
    def __init__(self,nombre,precio,sustancia,porcentaje):
        self.sustancia = sustancia
        self.porcentaje = porcentaje

    def get_sustancia(self):
        return self.sustancia

    def get_porcentaje(self):
        return self.porcentaje
producto1 = producto(nombre="gasas",precio =21)
producto2 = medicamento(nombre = "aspirina",precio =2,sustancia = "ácido clavulánico", porcentaje = 0)
producto3 = medicamento(nombre = "paracetamol",precio =45,sustancia = "opio", porcentaje = 30)
producto4 = medicamento(nombre = "dalsy",precio = 30,sustancia = "cítrico", porcentaje = 40)
class laboratorio():
    def __init__(self,nombre,inventario):
        self.nombre = nombre
        self.inventario = inventario
        self.producto1 = producto1
        self.producto2=  producto2
        self.producto3 = producto3
        self.producto4 = producto4
    def get_nombre(self):
        return self.get_nombre
    def get_inventario(self):
        return self.inventario
lab =("Bayern",)

print("El laboratorio"lab.get_nombre() "tiene")
