#TP 1 Paradigmas de la programación IFTS N°18
#Camila Gauna - Comisión A

from calculos_disparo import pitagoras, mejorDisparo, promedioDisparo
from podio import podio, podiotxt, participantes_hombres, edad_mujeres, promedio_todos_disparos, mejor_promedio_general

participantes = []
numero_id = ''
#Carga de participantes.
#El fin de ingreso de participantes se determina ingresando con número de participante igual a 999.
while numero_id != '999':
  numero_id = input("Ingrese el ID del participante: ")
  nombre = input("Ingrese nombre del participante: ")
  apellido = input("Ingrese apellido del participante: ")
  edad = int(input("Ingrese la edad del participante: "))
  sexo = input("Ingrese el sexo del participante (F/M): ")
  disparos = []
  for i in range(3):
    disparo = [input("Disparo. Eje x: "), input("Disparo. Eje y: ")]
    disparo = pitagoras(disparo[0], disparo[1])
    disparos.append(disparo)

  mejor_disparo = mejorDisparo(disparos[0], disparos[1], disparos[2])
  promedio_disparo = promedioDisparo(disparos[0], disparos[1], disparos[2])
  
  participante = {"numero_id": '',
                  "nombre": '',
                  "apellido": '',
                  "edad": '',
                  "sexo": '',
                  "disparos": '',
                  "mejor_disparo": '',
                  "promedio_disparo": ''
                  }
  
  participante['numero_id'] = numero_id
  participante['nombre'] = nombre
  participante['apellido'] = apellido
  participante['edad'] = edad
  participante['sexo'] = sexo
  participante['disparos'] = disparos
  participante['mejor_disparo'] = mejor_disparo
  participante['promedio_disparo'] = promedio_disparo
  participantes.append(participante)
  
#a)Mostrar el podio de los ganadores (los 3 primeros) en función del Mejor Disparo.
# Se pide informar por pantalla y en un archivo de texto.
print("                   ------------------- Podio de ganadores en función del MEJOR DISPARO ------------------- ")
mejor_disparo_ordenado = sorted(participantes, key=lambda x:x['mejor_disparo'])
podio(mejor_disparo_ordenado)
#Archivo de texto
podiotxt(participantes)

#i)	Opcional: Mejorar el punto a) asumiendo que se puede dar el caso en que dos participantes
#tengan el mismo Mejor Disparo, ordenar también por mejor promedio.
mejor_promedio_ordenado = sorted(participantes, key=lambda x:x['promedio_disparo'])
print("                   ------------------- Podio de ganadores en función del MEJOR PROMEDIO ------------------- ")
podio(mejor_promedio_ordenado)

#b)Informar quien fue el último (Nro Participante, Nombre, Apellido y Mejor disparo).
ultimo_lugar = mejor_disparo_ordenado[-1]
print(f"El último lugar lo obtuvo el participante ID N° {ultimo_lugar['numero_id']} -> {ultimo_lugar['nombre']} {ultimo_lugar['apellido']}, con un promedio de: {ultimo_lugar['promedio_disparo']}.")

#c)Informar cuantos participantes formaron parte del concurso.
total_participantes = len(participantes)
print(f"Total de participantes que participaron en el concurso: {total_participantes}.")

#d)Informar cuantos hombres formaron parte del concurso.
total_hombres = len(participantes_hombres(participantes))
print(f"Total de participantes hombres que participaron del concurso: {total_hombres}.")

#e)Informar edad promedio de las mujeres.
edad_mujeres = edad_mujeres(participantes)
print(f"La edad promedio de las participantes mujeres es de: {edad_mujeres}.")

#f)Mostrar el listado de todos los participantes ordenados por edad.
ordenados_por_edad = sorted(participantes, key=lambda x:x['edad'])
print("Listado de participantes ordenados por edad: ")
for i in ordenados_por_edad:
  print(f"ID: {i['numero_id']} -> {i['nombre']} {i['apellido']}, edad: {i['edad']}.")

#g)Informar el promedio de todos los disparos.
promedio_todos_disparos = round(promedio_todos_disparos(participantes),2)
print(f"El promedio de todos los disparos del concurso es de: {promedio_todos_disparos}.")

#h)Mostrar los participantes cuyo promedio de disparo sea mayor al promedio general.
mayor_promedio_general = mejor_promedio_general(promedio_todos_disparos, participantes)
print(f"Quienes obtuvieron un promedio mayor al general son: ")
for i in mayor_promedio_general:
  print(f"ID: {i['numero_id']} -> {i['nombre']} {i['apellido']}, con un promedio de: {i['promedio_disparo']}.")

  
  # lista_ordenada_por_edad = sorted(participantes, key=lambda x:x['edad'])
  # total_participantes = len(participantes) 
#promedio_todos_disparos(participantes)
#mejor_disparo_ordenado = sorted(participantes, key=lambda x:x['mejor_disparo'])
#mejor_promedio_ordenado = sorted(participantes, key=lambda x:x['promedio_disparo'])
#ultimo_lugar = mejor_disparo_ordenado[-1]
#ordenados_por_edad = sorted(participantes, key=lambda x:x['edad'])
# print(mejor_disparo_ordenado)
# podio(mejor_disparo_ordenado)
# print(len(participantes))
#print(len(participantes_hombres(participantes)))
#print(edad_mujeres(participantes))
#podiotxt(participantes)
