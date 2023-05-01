##Realizado por: "Kevin Isaac Padilla"

i=0
while i<5:
        
        valor = input(f"{i+1} iteracion, ingrese un valor cualquiera: ")

        
        if valor.isdigit(): ##Utilizando el comando isdigit se puede saber si la cadena
        #ingresada tiene un numero entero ,devolviendo un True, si no devolvera un False
            print("Este tipo de dato en Python es: un número entero.\n")
            
        elif valor.replace(".", "", 1).isdigit():##Si el valor ingresado fuera un punto flotante,
        #reemplazamos el punto por nada y verificamos si el string tiene un numero real entonces
        #debe ser un flotante al devolver un True.
            print("Este tipo de dato en Python es: un número de punto flotante.\n")
            
        elif valor.lower() == "true" or valor.lower() == "false":## Utilizamos el comando lower
        #por si acaso el usuario ingrese el valor booleano en mayusculas.
            print("Este tipo de dato en Python es: un booleano.\n")
            
        elif len(valor) == 1:##Si no se tuvo un numero en ninguna de las otras opciones y 
        #tampoco fue un valor booleano, se verificara si es un caracter usando la longitud del valor
            print("Este tipo de dato en Python es: un carácter.\n")
            
        else:##Finamente descartando los demas tipos de datos, se asume que es una cadena de 
        #caracteres
            print("Este tipo de dato en Python es: una cadena de caracteres.\n")      
        i+=1     
    
    
    