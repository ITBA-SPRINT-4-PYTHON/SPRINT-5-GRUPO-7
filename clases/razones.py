class Razon():
    def __init__(self, type):
        self.type = type

class RazonAltaChequera(Razon):
    def __init__(self, type):
        super().__init__(type)
        
class RazonAltaTarjCredito(Razon):
    def __init__(self, type):
        super().__init__(type)
        
class RazonCompraDolar(Razon):
    def __init__(self, type):
        super().__init__(type)
        
class RazonRetiroEfectivo(Razon):
    def __init__(self, type):
        super().__init__(type)
        
class RazonTransEnviada(Razon):
    def __init__(self, type):
        super().__init__(type)
        
class RazonTransRecibida(Razon):
    def __init__(self, type):
        super().__init__(type)