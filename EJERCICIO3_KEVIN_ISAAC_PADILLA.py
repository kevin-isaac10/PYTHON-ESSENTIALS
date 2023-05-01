    ##Realizado por Kevin Padilla

def find_max_min(dictionary, num_max, num_min):
    values = list(dictionary.values())
    values.sort()
    max_values = values[-num_max:]
    min_values = values[:num_min]
    return max_values, min_values

while True:
    print("Elija una opción:\n")
    print("1) Demostración del cálculo de valores altos y bajos en diccionarios.")
    print("2) Salir.\n")
    option = input()

    if option == "1":
        print("\nElija un diccionario para la demostración:\n")
        print("1) {Raul:34,Paula:19,Jorge:43,Richard:10,Diana:3,Isabel:76,Gustavo:12,Diego:37}")
        print("2) {tplA:(4,-12,56,-34,98,102),tplB:(9,0,1,10,-3,14),tlpC:(87,12,56,987,-61)}")
        print("3) {val1:-12.5,val2:12.5,val3:83,val4:2.1,val5:23,val6:100,val7:13.4,val8:92}")
        print("4) {lst1:[4,6,-12,56,-9,5.7,33,100],lst2:[9,0,81,-2,-56,],lst3:[12,31,87,1,0,4,-11]}\n")
        dictionary_option = input()

        if dictionary_option == "1":
            dictionary = {"Raul":34,"Paula":19,"Jorge":43,"Richard":10,"Diana":3,"Isabel":76,"Gustavo":12,"Diego":37}
        elif dictionary_option == "2":
            dictionary = {"tplA":(4,-12,56,-34,98,102),"tplB":(9,0,1,10,-3,14),"tlpC":(87,12,56,987,-61)}
        elif dictionary_option == "3":
            dictionary = {"val1":-12.5,"val2":12.5,"val3":83,"val4":2.1,"val5":23,"val6":100,"val7":13.4,"val8":92}
        elif dictionary_option == "4":
            dictionary = {"lst1":[4,6,-12,56,-9,5.7,33,100],"lst2":[9,0,81,-2,-56,],"lst3":[12,31,87,1,0,4,-11]}
        else:
            print("\nOpción no válida. Intente nuevamente.\n")
            continue

        while True:
            num_max = int(input("\nDigite el número de valores altos que desea mostrar: "))
            num_min = int(input("\nDigite el número de valores bajos que desea mostrar: "))

            if num_max + num_min > len(dictionary):
                print("\nNúmero de valores excede el tamaño del arreglo. Intente nuevamente.")
            else:
                break

        max_values, min_values = find_max_min(dictionary, num_max, num_min)

        print("\nValores calculados en formato LISTA:", max_values + min_values)
        print("Valores calculados en formato TUPLA:", tuple(max_values+min_values),"\n")
    elif option == "2":
        print("\nAdios")
        break