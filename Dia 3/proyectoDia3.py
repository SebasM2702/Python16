texto = input("Ingresa un texto: ").lower()
letras = input("Ingresa 3 letras: ").lower().replace(" ", "")
a,b,c = letras[0],letras[1],letras[2]
cantidad_palabras = len(texto.split())
primeraletra = texto[0]
ultima_letra = texto[-1]
print(f"{a.capitalize()} aparece {texto.count(a)} veces")
print(f"{b.capitalize()} aparece {texto.count(b)} veces")
print(f"{c.capitalize()} aparece {texto.count(c)} veces")
print(f"Cantidad total de palabras: {cantidad_palabras}")
print(f"Primera letra: {primeraletra}")
print(f"Ultima letra: {ultima_letra}")
separar_palabras = texto.split(" ")
unir = " ".join(separar_palabras[::-1])
print("Palabras en Orden Inverso: ",unir)
print("Texto al reves: ",texto[::-1])
dic = {True:"Si esta la palabra python",False:"No esta la palabra python"}
consultar_Python = "python" in texto
print(dic[consultar_Python])

"""
hacer una variable que guarde si python esta escrito en el texto
igualar la variable a los valores del diccionario y que escriba lo que contenga

Hacer un diccionario con valores true y false
"""




"""
separar con split para unirlo en una lista y contar las palabras mas facil"""

lorem ="""
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

