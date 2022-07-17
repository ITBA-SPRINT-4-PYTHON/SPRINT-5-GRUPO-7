class GetHTML():
    def __init__(self,misDatos):
        self.misDatos = misDatos

    def get_html(self):
        html = '<html>'
        html += '<head>'
        html += '<link rel="stylesheet" href="style.css">'
        html += '</head>'
        
        '''  'nombre': str(cliente.nombre, ' ', cliente.apellido),
            'numero': str(cliente.numero),
            'dni': str(cliente.dni),
            'direccion':{
                'calle': cliente.direccion.calle,
                'ciudad': cliente.direccion.ciudad,
                'provincia': cliente.direccion.provincia,
                'pais': cliente.direccion.pais,
            },
            'transferencias':[]
            
            '''
            
        html += '<body>'
        html += '<p>'+ 'Nombre: ' + str(self.misDatos['nombre']) +'</p>'
        html += '<p>'+ 'Numero: ' + str(self.misDatos['numero']) +'</p>'
        html += '<p>'+ 'DNI: ' + str(self.misDatos['dni']) +'</p>'
        html += '<p>'+ 'Calle: ' + str(self.misDatos['direccion']['calle']) +'</p>'
        html += '<p>'+ 'Ciudad: ' + str(self.misDatos['direccion']['ciudad']) +'</p>'
        html += '<p>'+ 'Provincia: ' + str(self.misDatos['direccion']['provincia']) +'</p>'
        html += '<p>'+ 'Pais: ' + str(self.misDatos['direccion']['pais']) +'</p>'
        html += '<ol>'
        
        for estado in self.misDatos['transferencias']:
            # resultado = 'Estado: ', estado['estado'],'Razon: ', estado['tipo'], 'NroCuenta: ',estado['cuentaNumero']
            row="<li>"+ str(estado) +"</li>"
            html+=row
            
        html +='</ol>'
        
        html += '</body>'
        html += '</html>'

        self.html = html
        with open("output.html", "w") as text_file:
            text_file.write(self.html)