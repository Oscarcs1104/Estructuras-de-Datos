import numpy as np
import random
class Estudiante:
    def __init__(self, nombre, codigo, codigocarrera , promacu, año):
        self.nombre = nombre
        self.codigo = codigo
        self.codigocarrera = codigocarrera
        self.promacu = promacu
        self.año = año
        
estudiantes = []


nombres = np.array(["Juan", "José", "David", "Miguel", "Jorge","María", "Daniela", "Sofía", "Lucía", "Paula" ])
codigosca = np.array([14, 40,11, 52])
promedios = np.random
for i in range (6500):
    n = random.choice(nombres)
    c = random.randint(1000000, 9999999)
    cc = random.choice(codigosca)
    pacu = round(random.uniform(0,5), 1)
    a = random.randint(1980, 2023)
    
    
    estu = Estudiante(n,c,cc,pacu,a)
    estudiantes.append(estu)

def estudianticos(carrera):
    contador = 0
    for estudiante in estudiantes:
        if estudiante.codigocarrera == carrera and estudiante.promacu >= 4:
            print(estudiante.codigo,"|", estudiante.nombre,"|", estudiante.promacu)
            contador += 1
    print("Los estudiantes con promedio 4 o mayor en la carrera son:", contador)


def condicionales():
    for estudiante in estudiantes:
        if estudiante.año >=1980 and estudiante.año <=1990:
            if estudiante.promacu >= 2.7 and estudiante.promacu <=3.2:
                print(estudiante.codigo,"|", estudiante.nombre,"|", estudiante.promacu)

    
for numero in codigosca:
    estudianticos(numero)
    print("Esos fueron los estudiantes en la carrera:",numero)

print("Los estudiantes condicionales son:")    
condicionales()
    

    
