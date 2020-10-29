from math import sqrt

#Función para el cálculo del disparo. Recibe las coordenadas y retorna la distancia al centro.
def pitagoras(x, y):
  eje_x = (int(x) * int(y))
  eje_y = (int(x) * int(y))
  resultado = sqrt(eje_x + eje_y)
  return resultado

def mejor_disparo():
  