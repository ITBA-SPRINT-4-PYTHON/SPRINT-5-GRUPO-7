from pydoc import cli
from zipfile import LargeZipFile
from clases.razones import Razon, RazonAltaChequera, RazonAltaTarjCredito, RazonCompraDolar, RazonRetiroEfectivo, RazonTransEnviada, RazonTransRecibida


class Buscador():
    def __init__(self,eventos):
        self.errores = [ x for x in eventos if x['estado']== 'RECHAZADA']
        self.sinErrores = [x for x in eventos if x ['estado']== 'ACEPTADA']
        
    def tiposErrores(self, cliente):
        self.devolucion = {
            'nombre': str(cliente.nombre + cliente.apellido),
            'numero': str(cliente.nro),
            'dni': str(cliente.dni),
            'direccion':{
                'calle': cliente.direccion.calle,
                'ciudad': cliente.direccion.ciudad,
                'provincia': cliente.direccion.provincia,
                'pais': cliente.direccion.pais,
            },
            'transferencias':[]
            
        }
        
        i = 0
        
        for x in self.errores:
            laRazon = Razon('')
            self.devolucion['transferencias'].append({
                        'fecha': x['fecha'],
                        'tipo': x['tipo'],
                        'estado': x['estado'],
                        'monto': x['monto'],
                        'razon': ''
                    })
            if x['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                if cliente.cajaAhorro.monto > x['monto'] or x['cupoDiarioRestante'] < x['monto']:
                    laRazon = RazonRetiroEfectivo('El monto pedido, super su monto limite')
            elif x['tipo'] == 'ALTA_TARJETA_CREDITO':
                if not cliente.puede_crear_tarjCredito():
                    laRazon = RazonAltaTarjCredito('Ha Superado La Cantidad Maxima de Tarjetas de Credito')
            elif x['tipo'] == 'ALTA_CHEQUERA':
                if not cliente.puede_tener_chequera():
                    laRazon = RazonAltaChequera('Ha Superado La Cantidad Maxima de Chequeras')
                
            elif x['tipo'] == 'COMPRAR_DOLAR':
                if not cliente.puede_comprar_dolar():
                    laRazon = RazonCompraDolar('Usted no puede comprar dolares')
                
            elif x['tipo'] == 'TRANSFERENCIA_ENVIADA':
                if cliente.cajaAhorro.monto < (x['monto'] * (cliente.cajaAhorro.costoTrans + 1)):
                    laRazon = RazonTransEnviada('Su dinero no alcanza para realizar la transferencia')
                
            elif x['tipo'] == 'TRANSFERENCIA_RECIBIDA':
                if type(cliente) != 'ClienteBlack' and x['monto'] > cliente.cajaAhorro.limTrans:
                    laRazon = RazonTransRecibida('No puede recibir trasnferencias que superen su limite')
                    
            self.devolucion['transferencias'][i]['razon'] = laRazon.type
            
            i += 1

        for x in self.sinErrores:
            self.devolucion['transferencias'].append({
                        'fecha': x['fecha'],
                        'tipo': x['tipo'],
                        'estado': x['estado'],
                        'monto': x['monto'],
                        'razon': ''
                    })          
                        
                        

    def allErrores(self):
        for e in self.errores:
            print(e) 