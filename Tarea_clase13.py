# SEMANA TAREA EN CLASE 13
# Crea una función que me permita transformar grados centigrados a grados Fahrenheit y kelvin utilizando tuplas
# Formula para transformar centigrados -> Fahrenheit
# Formula para transformar centigrados -> Kelvin
# subir al repositorio de tareas convertitor_grados.py

def convertidor(grados_centigrados):
  faren = (9 * (grados_centigrados - 32)) / 5
  kelvin = grados_centigrados + 273.15

  return faren, kelvin


grados_cent = float(input("Ingrese los grados centigrados: "))
r_faren, r_kelvin = convertidor(grados_cent)
print("Los grados farenheit son:", r_faren)
print("Los grados kelvin son:", r_kelvin)
