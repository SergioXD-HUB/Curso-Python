numero = "147"
print(numero)
print(type(numero)) 

numero = int(numero)
print(type(numero))

# basicametne aca se explica que el numero es un string y luego se convierte a int
print(numero + 3)  # Esto ahora funciona porque 'numero' es un entero

# No se puede convertir un string que no es un numero a int
# Esto lanzará un ValueError porque "hola" no es un número válido

numero = "hola"
print(numero)

numero = int(numero)  # Esto causará un error
print(type(numero))  # Esto no se ejecutará porque la línea anterior falla  


#recomendaciones para variables 

numeroUno = 1
numeroDos = 2
numeroTres = 3

# Es mejor usar nombres de variables descriptivos

numero_primero = 1
numero_segundo = 2  

