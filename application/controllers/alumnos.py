import web  # pip install web.py
import csv  # CSV parser
import json  # json parser
import app

render = web.template('application/views/')

class Alumnos:
    def GET(self):
        try:
            data = web.input()
            if(data['token'] == '1234'): #hhtp://localhost:8080/alumnos?action=get&token=1234
                if(data['action'] == "get"):
                    inf = {}
                    inf['version'] == "1.0"
                    inf['status'] == "200 ok"
                    result = "matricula,nombre,primer_apellido,segundo_apellido,carrera\n"
                    with open('static/csv/alumnos.csv', 'r') as csvfile:
                        reader =  csv.DictReader(csvfile)
                        result = []
                        for row in reader:
                            resultado = {}
                            resultado['matricula'] = str(row['matricula'])
                            resultado['nombre'] = str(row['nombre'])
                            resultado['primer_apellido'] = str(row['primer_apellido'])
                            resultado['segundo_apellido'] = str(row['segundo_apellido'])
                            resultado['carrera'] = str(row['carrera'])
                            result.append(resultado)
                        inf['alumno'] = result
                        return json.dumps(inf)

                # http://localhost:8080/alumnos?action=insert&token=1234&matricula=171600&nombre=Adrian&primer_apellido=Leon&segundo_apellido=Ortega&carrera=TIC
                if(data['action'] == 'insert'):
                    inf={}
                    inf['version'] = "1.0"
                    inf['status'] = "200 ok"  
                    matricula = str(data['matricula'])
                    nombre = str(data['nombre'])
                    primer_apellido = str(data['primer_apellido'])
                    segundo_apellido = str(data['segundo_apellido'])
                    carrera = str(data['carrera'])
                    res = []
                    res.append(matricula)
                    res.append(nombre)
                    res.append(primer_apellido)
                    res.append(segundo_apellido)
                    res.append(carrera)
                    resulta = {}
                    resultado['matricula'] = matricula
                    resultado['nombre'] = nombre
                    resultado['primer_apellido'] = primer_apellido
                    resultado['segundo_apellido'] = segundo_apellido
                    resultado['carrera'] = carrera
                    result = []
                    result.append(resultado)
                    inf['alumno'] = result

                    with open('static/csv/alumnos.csv','a+', newline = '') as cualquier_variable:
                        writer = csv.writer(cualquier_variable)
                        writer.writerow(res)
                    return json.dumps(inf)

                # http://localhost:8080/alumnos?action=buscar&token=1234&matricula171602
                if(data['action'] == 'buscar'):
                    inf = {}
                    inf['version'] = "1.0"
                    inf['status'] = "200 ok"
                    result = "matricula,nombre,primer_apellido,segundo_apellido,carrera\n"
                    matricula = str(data['matricula'])
                    with open('static/csv/alumnos.csv', 'r') as csvfile:
                        reader = csv.DictReader(csvfile)
                        result = []
                        for row in reader:
                            if(row['matricula'] == matricula):
                                resultado = {}
                                resultado['matricula']=str(row['matricula'])
                                resultado['nombre'] = str(row['nombre'])
                                resultado['primer_apellido'] = str(row['primer_apellido'])
                                resultado['segundo_apellido'] = str(row['segundo_apellido'])
                                resultado['carrera'] = str(row['carrera'])
                                result.append(resultado)
                            inf['alumno'] = result
                    return json.dumps(inf)

                    # http://localhost:8080/alumnos?action=actualizar&token=1234&matricula=171601&nombre=Dejah&primer_apellido=Thoris&segundo_apellido=Barsoon&carrera=TIC
                    if(data['action'] == 'actualizar'):
                        inf = {}
                        inf['version'] = "1.0"
                        inf['status'] = "200 ok"  
                        result = "matricula,nombre,primer_apellido,segundo_apellido,carrera"
                        matricula2 = str(data['matricula'])
                        nombre2 = str(data['nombre'])
                        primer_apellido2 = str(data['primer_apellido'])
                        segundo_apellido2 = str(data['segundo_apellido'])
                        carrera2 = str(data['carrera'])

                        with open('static/csv/alumnos.csv', 'r') as csvfile:
                            reader = csv.DictReader(csvfile)
                            result = [] # se utilizará este arreglo para modificar los registros del CSV (obtiene una fila, si es necesario la modifica y al final envía al archivo)
                            for row in reader:
                                resulta={}
                                # comprueba que la fila sea la indicada para modificar, en base a la matricula dada como parametro en la URL
                                if (row['matricula'] == matricula2):
                                    resultado['matricula']=str(row['matricula'])
                                    resultado['nombre'] = nombre2
                                    resultado['primer_apellido'] = primer_apellido2
                                    resultado['segundo_apellido'] = segundo_apellido2
                                    resultado['carrera'] = carrera2
                                else:
                                    resultado['matricula'] = str(row['matricula'])
                                    resultado['nombre'] = str(row['nombre'])
                                    resultado['primer_apellido'] = str(row['primer_apellido'])
                                    resultado['segundo_apellido'] = str(row['segundo_apellido'])
                                    resultado['carrera'] = str(row['carrera'])
                                result.append(resultado)
                            inf['alumno'] = result
                            
                            # sobreescribe el archivo CSV con los valores modificados
                            with open('static/csv/alumnos.csv', 'w') as csvfile:
                                nombres_campos = ['matricula','nombre','primer_apellido','segundo_apellido','carrera']
                                writer = csv.DictWriter(csvfile, fieldnames=nombres_campos)
                                
                                writer.writeheader() # escribe los nombres de los campos en el encabezado del CSV
                                for i in range(0, len(result)):
                                    # writer.writerow({'field1': 'A', 'field2': 'B', 'field3': 'C'})
                                    writer.writerow(result[i])
                                    print(result[i]) # print de prueba...
                            
                            return json.dumps(result)
                    
        
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result