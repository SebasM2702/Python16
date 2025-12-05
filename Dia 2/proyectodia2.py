print("Bienvenido al Sistema de Ventas\nAqui calcularemos sus comisiones\nPorfavor ingrese los datos solicitados a continuacion")
nombre = input("Ingresa tu nombre: ")
ventas = float(input("Ingresa tus ventas del mes: "))
comision = round(ventas * 13 / 100)
print(f"Bienvenido {nombre}"
      f"\nA continuacion su respectivo calculo"
      f"\nVentas: {ventas}"
      f"\nComision: {comision}"
      f"\nGanancia total: {ventas - comision}")