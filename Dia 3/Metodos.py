"""
texto= "Este es el texto de Federico"


resultado = texto.replace("e", "x")
print(resultado)

"""

"""
a= "aprender"
b = "python"
c= "es"
d= "genial"
e= " ".join([a,b,c,d]).capitalize()

print(e)
"""

"""
Práctica Métodos de String 1
Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."

resultado = frase.upper()
print(resultado)
"""
"""
Práctica Métodos de String 2
Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
lista_palabras = ["La","legibilidad","cuenta."]
espacio = " ".join(lista_palabras)
print(espacio)
"""

"""
Práctica Métodos de String 3
Reemplaza en la siguiente frase:

"Si la implementación es difícil de explicar, puede que sea una mala idea."

los siguientes pares de palabras:

"difícil" --> "fácil"

"mala" --> "buena"

y muestra en pantalla la frase con ambas palabras modificadas.

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
remplazar = frase.replace("difícil", "fácil")
remplazar = remplazar.replace("mala", "buena")
print(remplazar)
"""




texto= "Este es el texto de Federico"


resultado = texto.split("t")
print(resultado)
