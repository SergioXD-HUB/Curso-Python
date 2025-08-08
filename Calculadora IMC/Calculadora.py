

#Bienvendida
print("""
    Hola, ¿como estás?
    Este programa te ayudara a calcular tu IMC (Índice de Masa Corporal).
    El IMC es una medida que relaciona tu peso con tu altura.
    Por lo cual, necesitaremos que ingreses algunos datos.
      """)

#Pedir nombre (no puede estar vacío)
nombre = ""
while nombre.strip() == "":
    nombre = input("¿Cuál es tu nombre? ")
    if nombre.strip() == "":
        print("Por favor, ingresa tu nombre.")

#Pedir edad (entero positivo)
while True:
    try:
        edad = int(input("¿Cuántos años tienes? "))
        if edad > 0:
            break
        else:
            print("Edad no válida. Ingresa un número positivo.")
    except ValueError:
        print("Ingresa un número válido para la edad.")

#Pedir peso (decimal positivo)
while True:
    try:
        peso = float(input("Ingresa tu peso en kilogramos: "))
        if peso > 0:
            break
        else:
            print("Peso no válido. Ingresa un valor positivo.")
    except ValueError:
        print("Ingresa un número válido para el peso.")

#Pedir altura (decimal positivo)
while True:
    try:
        altura = float(input("Ingresa tu altura en metros: "))
        if altura > 0:
            break
        else:
            print("Altura no válida. Ingresa un valor positivo.")
    except ValueError:
        print("Ingresa un número válido para la altura.")

#Mostrar resumen
print("\n Datos ingresados correctamente:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m\n")

#Calculos
imc = peso / (altura ** 2)

print(f"{nombre}, tienes {edad} años de edad y tu IMC es: {imc:.2f}\n")