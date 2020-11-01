from math import sqrt

#Función para el cálculo del disparo. Recibe las coordenadas y retorna la distancia al centro.
def pitagoras(x, y):
  eje_x = (int(x) * int(y))
  eje_y = (int(x) * int(y))
  resultado = sqrt(eje_x + eje_y)
  resultado = round(resultado, 2)
  return resultado

def mejorDisparo(a, b, c):
  temp = 0
  if a < b and a < c:
    temp = a
  elif b < c:
    temp = b
  else:
    temp = c
  return temp

def promedioDisparo(x,y,z):
  resultado = (x + y + z) /3
  resultado = round(resultado, 2)
  return resultado