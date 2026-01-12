"""
bool = 7 < 4
print(f"7 es menos a cuatro: {bool}")
"""
"""
var1 = True
var2 = False

print(type(var1),type(var2))
print(isinstance(var1,bool) and isinstance(var2,bool))
"""
"""
print("Verificaciones")
print("0",bool(0))
print("1",bool(1))
print(" ",bool(""))
print("hola",bool("hola"))
print("[]",bool([]))
print("1,2",bool([1,2]))
print("none",bool(None))

print("Comparaciones")
print(1 and 0)
print(1 or 0)
print(0 or 5)
print(5 and 0)
"""
"""
lista = [1,2,3,4]
requeridos = [1,2,6]
control = all(x in lista for x in requeridos)
print(type(control))
print(control)
"""

"""
Práctica Booleanos 1
Realiza una comparación que arroje como resultado un booleano y almacena el resultado (True/False) en una variable llamada prueba

prueba = bool()
print(type(prueba))
"""
"""
Práctica Booleanos 2
Verifica si 17834/34 es mayor que 87*56 y muestra el resultado (booleano) en pantalla utilizando print()
verificacion = 17834/34 > 87*56
print(f"17834/34 = {round(17834/34,1)} es mayor que 87*56 = {87*56}: {verificacion}")
print(verificacion)
"""

"""
Práctica Booleanos 3
Verifica si la raíz cuadrada de 25 es igual a 5 y muestra el resultado (booleano) en pantalla utilizando print()


"""
verificacion = 25**0.5 == 5
print(f"{25**0.5} == 5?")
print(verificacion)
