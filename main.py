from calculos_disparo import pitagoras, mejorDisparo, promedioDisparo

participantes = []
numero_id = ''
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