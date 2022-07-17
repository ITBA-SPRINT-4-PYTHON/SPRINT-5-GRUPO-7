from . import direccion
from . import cuenta

class Cliente:
    
    def __init__(self,data):
        self.nro = data['numero']
        self.tipo=data['tipo']
        self.dni=data['dni']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.direccion = direccion.Direccion(data)
        print('Se creo cliente: '+self.dni)
        
    def baja(self):
        self.tipo='baja'

class ClienteClassic(Cliente):
    
    def puede_comprar_dolar(self):
        return False
    
    def puede_tener_chequera(self):
        return False
    
    def puede_crear_tarjCredito(self):
        return False
    
    def __init__(self, data):
        print('Se creo classic')
        super().__init__(data)
        saldoEnCuenta = data['transacciones'][0]['saldoEnCuenta']
        self.cajaAhorro = cuenta.Cuenta(10000, 150000, saldoEnCuenta, 0.1, 0)
    
class ClienteGold(Cliente):
    
    def puede_comprar_dolar(self):
        return True
    
    def puede_tener_chequera(self):
        return self.cantCheq < 1
    
    def puede_crear_tarjCredito(self):
        return self.cantTarjCred < 1
    
    def __init__(self, data):
        print('Se creo gold')  
        super().__init__(data)
        saldoEnCuenta = data['transacciones'][0]['saldoEnCuenta']
        self.cajaAhorro = cuenta.Cuenta(20000, 500000, saldoEnCuenta, 0.05, 0)
        self.cantTarjCred = data['transacciones'][0]['totalTarjetasDeCreditoActualmente']
        self.cantCheq = data['transacciones'][0]['totalChequerasActualmente']


class ClienteBlack(Cliente):
    
    def puede_comprar_dolar(self):
        return True
    
    def puede_tener_chequera(self):
        return self.cantCheq < 2
    
    def puede_crear_tarjCredito(self):
        return self.cantTarjCred < 5
    
    def __init__(self, data):
        print('Se creo black')
        super().__init__(data)
        saldoEnCuenta = data['transacciones'][0]['saldoEnCuenta']
        self.cajaAhorro = cuenta.Cuenta(100000, -1, saldoEnCuenta, 0, 0)
        self.cantTarjCred = data['transacciones'][0]['totalTarjetasDeCreditoActualmente']
        self.cantCheq = data['transacciones'][0]['totalChequerasActualmente']
        


