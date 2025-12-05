"""
Práctica con Conversiones 1
Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:
"""
num1 = 7.5

num2 = int(num1)

print(type(num2))
#Solucion, crear una variable nueva "num2" en la que vamos a convertir nuestra variable "num1" en una variable de tipo int
#Esto le quitaria los decimales al numero, NO LO REDONDEA

"""
Práctica con Conversiones 2
Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:
"""
num2 = 10
num1 = float(num2)
print(type(num1))
#Solucion, hay que hacer hacer una variable nueva "num1" en la que vamos hacer una conversion de la variable "num2" en la que lo vamos a convertir en float

"""
Práctica con Conversiones 3
Suma los valores de num1 y num2.

No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la función print().
"""
num1 = "7.5"
num2 = "10"
print(float(num1) + int(num2))
#Solucion, la variables llevan comillas, significa que son String y no se pueden sumar, hay que convertilos en sus respectivos tipos de datos, float y string