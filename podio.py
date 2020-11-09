def podio(participantes):
  for i in range(3):
    print("Puesto " + str(i+1))
    print("ID del participante: " + participantes[i]["numero_id"])
    print("Nombre: " + participantes[i]["nombre"])
    print("Apellido: " + participantes[i]["apellido"])
    print("Mejor disparo: " + str(participantes[i]["mejor_disparo"]))
    print("Promedio: " + str(participantes[i]["promedio_disparo"]) + "\n")

def podio_txt(participantes):
  txt = open("podio.txt", "w+")  
  for i in range(3):
    txt.write("Puesto " + str(i+1) + "\n")
    txt.write("ID del participante: " + participantes[i]["numero_id"] + "\n")
    txt.write("Nombre: " + participantes[i]["nombre"] + "\n")
    txt.write("Apellido: " + participantes[i]["apellido"] + "\n")
    txt.write("Mejor disparo: " + str(participantes[i]["mejor_disparo"]) + "\n")
    txt.write("Promedio: " + str(participantes[i]["promedio_disparo"]) + "\n")
    txt.write("\n")

def participantes_hombres(participantes):
  solo_hombres = []
  for hombres in participantes:
    if hombres['sexo'] == 'm':
      solo_hombres.append(hombres)
  return solo_hombres

def edad_mujeres(participantes):
  mujeres = []
  edad = 0
  for mujer in participantes:
    if mujer['sexo'] == 'f':
      mujeres.append(mujer)
  for mujer in mujeres:
    edad += mujer['edad']
  promedio = round(edad / len(mujeres), 2)
  return promedio

def promedio_todos_disparos(participantes):
  total = 0
  for disparo in participantes:
    total += disparo['promedio_disparo']
  resultado = total / len(participantes)
  return resultado

def mejor_promedio_general(promedio, participantes):
  mejores_al_promedio = []
  for participante in participantes:
    if participante['promedio_disparo'] > promedio:
      mejores_al_promedio.append(participante)
  return mejores_al_promedio