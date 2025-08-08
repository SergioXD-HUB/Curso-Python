texto_variable = "Hola soy sergio #$#"
print(type(texto_variable))

#Podemos usar comillas triples para crear cadenas de texto
#que se extienden por varias lineas, lo cual es muy util para comentarios largos
# print (""" 
#        Imaginate este texto como un comentario
#        que se extiende por varias lineas, asi tal cual como lo imaginas.
#        Para eso las triples comillas son muy utiles.
#        Tambien puedes usar comillas simples, pero las triples son mas comunes.
#        """)

# #subspriting e indexado de cadenas

# texto = "Sergio es un programador"

#print(texto[4])  # Imprime el quinto caracter
#print(texto[6])  # Imprime el séptimo caracter

#basicamente es el conteo de caracteres, empezando desde 0

#LAS CADENAS DE TEXTO SON INMUTABLES, NO SE PUEDEN MODIFICAR EN EL TRANSCURSO.



#SLICING O SUBSTRING
# print(texto[0:5])  # Imprime los primeros 5 caracteres
# print(texto[6:9])  # Imprime del séptimo al noveno
# print(texto[10:])  # Imprime desde el décimo caracter hasta el final
# print(texto[:5])   # Imprime desde el inicio hasta el quinto caracter  
# print(texto[-1])  # Imprime el último caracter
# print(texto[-2])  # Imprime el penúltimo caracter   
# print(texto[-5:])  # Imprime los últimos 5 caracteres
# print(texto[-10:-5])  # Imprime del décimo al quinto desde el final
# print(texto[-10:])  # Imprime desde el décimo desde el final hasta el final
# print(texto[-10::-5])  # Imprime del décimo al quinto desde el final

#cadenas y formatos 

# texto = "Hola mundo! Buenastardes"
# print(texto.lower()) #cambia a minusculas
# print(texto.upper()) #cambia a mayusculas
# print(texto.title()) #cambia la primera letra de cada palabra a mayuscula
# print(texto.capitalize()) #cambia la primera letra de la cadena a mayuscula
# print(texto.strip()) #elimina los espacios al principio y al final de la cadena
# print(texto.replace("Hola", "Adios")) #reemplaza una palabra por otra
# print(texto.split(" ")) #divide la cadena en una lista de palabras
# print(texto.split("a")) #divide la cadena en una lista de palabras usando "a" como separador
# print(texto.swapcase()) #cambia las mayusculas por minusculas y viceversa
# print(texto.startswith("Hola")) #verifica si la cadena empieza con "Hola"
# print(texto.endswith("tardes")) #verifica si la cadena termina con "tardes"
# print(texto.find("mundo")) #busca la palabra "mundo" y devuelve su posición
# print(texto.index("mundo")) #busca la palabra "mundo" y devuelve su posición, si no la encuentra lanza un error
# print(texto.count("a")) #cuenta cuantas veces aparece la letra "a"  

# print ( " {} + {} + {} ".format("Hola", "Mundo", "Sergio") ) #formatea la cadena con los valores que le pasamos
# print ( " {2} + {0} + {2} ".format("Hola", "Mundo", "Sergio") ) #formatea la cadena con los valores que le pasamos, usando indices
# print ( " {} + {} + {} = {} ".format( 4 , 5, 6 , 3*2) ) #formatea la cadena con los valores que le pasamos
# print ( " {3:2f} + {2:2f} + {1:2f} = {0:2f} ".format( 4 , 5, 6 , 3*2) ) #formatea la cadena con los valores que le pasamos, usando indices y especificando el formato de los numeros
# print ( " {:d} = {:b} = {:o} = {:x} ".format( 14 , 14, 14 , 14) ) #formatea la cadena con los valores que le pasamos, usando indices y especificando el formato de los numeros como enteros