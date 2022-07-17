class Direccion():
    def __init__(self, data):
        self.calle = data['direccion']['calle']
        self.nro= data['direccion']['numero']
        self.ciudad= data['direccion']['ciudad']
        self.provincia= data['direccion']['provincia']
        self.pais= data['direccion']['pais']