from time import sleep


class Telefono():
    def __init__(self, fabricante, modelo, camara, pantalla):
        self.fabricante = fabricante
        self.modelo = modelo
        self.camara = camara
        self.pantalla = pantalla

    def get_fabricante(self):
        return self.fabricante

    def get_modelo(self):
        return self.modelo

    def get_camara(self):
        return self.camara

