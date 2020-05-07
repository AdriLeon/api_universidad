import web
import app
import json
import csv

render=web.template.render('application/views/')

class Alumnos:
    def GET(self):
        try:
            data=web.input()
            if(data['token']=='1234'): 
                # http://localhost:8080/alumnos?action=get&token=1234
                if(data['action']=="get"):
                    inf={}
                    inf['version']="0.01"
                    inf['status']="200 ok"  
                    result="matricula,nombre,primer_apellido,segundo_apellido,carrera\n"
                    with open('static/csv/alumnos.csv', 'r') as csvfile:
                        reader = csv.DictReader(csvfile)
                        result=[]
                        for row in reader:
                            resulta={}
                            resulta['matricula']=str(row['matricula'])
                            resulta['nombre']=str(row['nombre'])
                            resulta['primer_apellido']=str(row['primer_apellido'])
                            resulta['segundo_apellido']=str(row['segundo_apellido'])
                            resulta['carrera']=str(row['carrera'])
                            result.append(resulta)
                        inf['alumno']=result
                        return json.dumps(inf)

                # http://localhost:8080/alumnos?action=insert&token=1234&matricula=171604&nombre=Robin&primer_apellido=Van&segundo_apellido=Persie&carrera=TIC
                if(data['action']=="insert"):
                    inf={}
                    inf['version']="0.01"
                    inf['status']="200 ok"  
                    matricula=str(data['matricula'])
                    nombre=str(data['nombre'])
                    primer_apellido=str(data['primer_apellido'])
                    segundo_apellido=str(data['segundo_apellido'])
                    carrera=str(data['carrera'])
                    res=[]
                    res.append(matricula)
                    res.append(nombre)
                    res.append(primer_apellido)
                    res.append(segundo_apellido)
                    res.append(carrera)
                    resulta={}
                    resulta['matricula']=matricula
                    resulta['nombre']=nombre
                    resulta['primer_apellido']=primer_apellido
                    resulta['segundo_apellido']=segundo_apellido
                    resulta['carrera']=carrera
                    result=[]
                    result.append(resulta)
                    inf['alumno']=result
                    
                    with open('static/csv/alumnos.csv','a+', newline='') as variable_cualquiera:
                        writer=csv.writer(variable_cualquiera)
                        writer.writerow(res)
                    return json.dumps(inf)

                # http://localhost:8080/alumnos?action=buscar&token=1234&matricula=171601
                if(data['action']=='buscar'):
                    inf={}
                    inf['version']="0.01"
                    inf['status']="200 ok"
                    result="matricula,nombre,primer_apellido,segundo_apellido,carrera\n"
                    matricula=str(data['matricula'])
                    with open('static/csv/alumnos.csv', 'r') as csvfile:
                        reader = csv.DictReader(csvfile)
                        result=[]
                        for row in reader:
                            if(row['matricula'] == matricula):
                                resulta={}
                                resulta['matricula']=str(row['matricula'])
                                resulta['nombre']=str(row['nombre'])
                                resulta['primer_apellido']=str(row['primer_apellido'])
                                resulta['segundo_apellido']=str(row['segundo_apellido'])
                                resulta['carrera']=str(row['carrera'])
                                result.append(resulta)
                            inf['alumno']=result
                    return json.dumps(inf)
                
                # http://localhost:8080/alumnos?action=actualizar&token=1234&matricula=171601&nombre=Eliazar&primer_apellido=Rodriguez&segundo_apellido=Velasco&carrera=TIC
                if(data['action']=='actualizar'):
                    inf={}
                    inf['version']="0.01"
                    inf['status']="200 ok"  
                    result="matricula,nombre,primer_apellido,segundo_apellido,carrera"
                    matricula_2=str(data['matricula'])
                    nombre_2=str(data['nombre'])
                    primer_apellido_2=str(data['primer_apellido'])
                    segundo_apellido_2=str(data['segundo_apellido'])
                    carrera_2=str(data['carrera'])

                    with open('static/csv/alumnos.csv', 'r') as csvfile:
                        reader = csv.DictReader(csvfile)
                        result=[] # se utilizará este arreglo para modificar los registros del CSV (obtiene una fila, si es necesario la modifica y al final envía al archivo)
                        for row in reader:
                            resulta={}
                            # comprueba que la fila sea la indicada para modificar, en base a la matricula dada como parametro en la URL
                            if (row['matricula'] == matricula_2):
                                resulta['matricula']=str(row['matricula'])
                                resulta['nombre']=nombre_2
                                resulta['primer_apellido']=primer_apellido_2
                                resulta['segundo_apellido']=segundo_apellido_2
                                resulta['carrera']=carrera_2
                            else:
                                resulta['matricula']=str(row['matricula'])
                                resulta['nombre']=str(row['nombre'])
                                resulta['primer_apellido']=str(row['primer_apellido'])
                                resulta['segundo_apellido']=str(row['segundo_apellido'])
                                resulta['carrera']=str(row['carrera'])
                            result.append(resulta)
                        inf['alumno']=result
                        
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