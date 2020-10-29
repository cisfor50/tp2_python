from calculos_disparo import pitagoras

participantes = []
numero_id = ''

while numero_id != 999:
  numero_id = input("Ingrese el ID del participante: ")
  nombre_completo = input("Ingrese nombre y apellido del participante: ")
  edad = int(input("Ingrese la edad del participante: "))
  sexo = input("Ingrese el sexo del participante (F/M): ")
  disparos = []
  for i in range(3):
    disparo = [input("Disparo. Eje x: "), input("Disparo. Eje y: ")]
    disparo = pitagoras(disparo[0], disparo[1])
    disparos.append(disparo)
  
    print(disparos) 
  