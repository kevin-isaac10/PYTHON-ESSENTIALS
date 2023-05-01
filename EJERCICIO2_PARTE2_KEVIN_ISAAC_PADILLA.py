##Realizado por: "Kevin Isaac Padilla"   


while True:
    password = input("\nIngrese su contraseña: ")

    # Declaramos variables de validación a través de booleanos
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special_char = False
    is_valid_length = False

    #Examinamos cada caracter de la contraseña
    for char in password:
        if char in "abcdefghij":
            has_lowercase = True
        elif char in "KLMNOPQRST":
            has_uppercase = True
        elif char.isdigit():  ##Usamos el metodo isdigit para verificar si hay un numero en la contraseña
            has_digit = True
        elif char in "$%*@":
            has_special_char = True

    #Examinamos la longitud de la cadena de caracteres
    if 5 <= len(password) <= 15:
        is_valid_length = True

    #Verificamos todas las condiciones que requiere la contraseña 
    if has_lowercase and has_uppercase and has_digit and has_special_char and is_valid_length:
        print("Contraseña válida")
        break
    else:
        print("Contraseña inválida")
        if not has_lowercase:
            print("- Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.")
        if not has_uppercase:
            print("- Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.")
        if not has_digit:
            print("- Debe contener al menos un número entre 0 y 9.")
        if not has_special_char:
            print("- Debe contener un símbolo especial entre: $,%,*,@")
        if not is_valid_length:
            print("- La contraseña debe tener un tamaño mínimo de 5 caracteres y máximo de 15.")
    var1:True
