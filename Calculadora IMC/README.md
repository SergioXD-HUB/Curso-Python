Calculadora de IMC por Sergio Hernández Sandoval

1.- Se hace una pequeña presentacion y se informa que se pediran algunos datos

2.- Comenzamos con el nombre, esta parte de codigo va dentro de un while debido a que necesitamos un bucle hasta que nos 
    aseguremos que nuestra variable "nombre" contiene caracteres validos. Se usa .strip() para borrar todos los espacios
    que puedan dejarse a proposito y asi asegurar que haya una cadena de texto correspondiente al nombre.

3.- Parea la edad While True crea un bucle infinito que solo se detiene con break, si el valor es positivo, rompe el bucle con break, si es cero o negativo, muestra un mensaje de error, except ValueError captura el error si el usuario escribe algo que no es número.

4.- Para el peso While True crea un bucle infinito que solo se detiene con break, si el valor es positivo (debe ser esta vez variante tipo float), rompe el bucle con break, si es cero o negativo, muestra un mensaje de error, except ValueError captura el error si el usuario escribe algo que no es número.

5.- Para la altura se ocupa la misma estrucura que para el peso, solo que se especifica que se comparta el dato en metros.

6.- Mostramos resumenes de datos recolectados.

7.- Se hace la operacion correspondiente al calculo de IMC 

8.- Se muestra el resultado final.
