class GetHTML():
    def __init__(self,misDatos):
        self.misDatos = misDatos

    def get_html(self):
        html = '<html>'
        html += '<head>'
        html += '<link rel="stylesheet" href="style.css">'
        html += '</head>'
        html += '<body>'
        
        html += '<p>'+ 'Nombre: ' + str(self.misDatos['nombre']) +'</p>'
        html += '<p>'+ 'Numero: ' + str(self.misDatos['numero']) +'</p>'
        html += '<p>'+ 'DNI: ' + str(self.misDatos['dni']) +'</p>'
        html += '<p>'+ 'Calle: ' + str(self.misDatos['direccion']['calle']) +'</p>'
        html += '<p>'+ 'Ciudad: ' + str(self.misDatos['direccion']['ciudad']) +'</p>'
        html += '<p>'+ 'Provincia: ' + str(self.misDatos['direccion']['provincia']) +'</p>'
        html += '<p>'+ 'Pais: ' + str(self.misDatos['direccion']['pais']) +'</p>'
        html += '<table>'
        html += '<thead>'
        html += '<tr>'
        html += '<th> Fecha </th>'
        html += '<th> Tipo </th>'
        html += '<th> Estado </th>'
        html += '<th> Monto </th>'
        html += '<th> Razon </th>'
        html += '</tr>'
        html += '</thead>'
        html += '<tbody>'
        
        for estado in self.misDatos['transferencias']:
            row = '<tr>'
            
            row += '<td>' + 'Fecha: ' + estado['fecha'] + '</td>'
            row += '<td>' + ' Tipo: ' + estado['tipo'] + '</td>'
            row += '<td>' + ' Estado: ' + estado['estado'] + '</td>'
            row += '<td>' + ' Monto: $' + str(estado['monto']) + '</td>'
            row += '<td>' + ' Razon: ' + estado['razon'] + '</td>'
            
            row += '</tr>'
            
            html+=row
        
        html += '</tbody>'
        html += '</table>'
        html += '</body>'
        html += '</html>'

        self.html = html
        with open("output.html", "w") as text_file:
            text_file.write(self.html)