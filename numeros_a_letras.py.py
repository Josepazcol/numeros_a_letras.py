stUnidades = ("CERO", "UNO", "DOS", "TRES" ,"CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE", "DIEZ", "ONCE", "TRECE", "CATORCE", "QUINCE")
stDecenas = ("", "DIEZ", "VEINTE", "TREINTA", "CUARENTA", "CINCUENTA", "SESENTA", "SETENTA", "OCHENTA", "NOVENTA")
stCentenas = ("", "CIEN", "DISCIENTOS", "TRESCIENTOS", "CUATROCIENTOS", "QUINIENTOS", "SEISCIENTOS", "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS")

num = int(input("Ingresa un numero: "))
if num < 0 or num > 999:
    print ("Error numero")
else:
        unidades = num % 10
        decidades = num % 100
        decenas = (num // 10) % 10
        centenas = num // 100

        if centenas != 0:
            if centenas == 1:
                if decidades == 0:
                    print ("CIEN", end="")
                else:
                    print ("CIENTO", end="")
            else:
                print(stCentenas[centenas], end="")
            if decidades != 0:
                print (" ", end="")

        if decidades <= 15:
            if decidades != 0 or centenas == 0:
                print (stUnidades[decidades], end="")
        else:
            if decenas == 1:
                print ("DIECI", end="")
            elif decenas == 2:
                    if unidades == 0:
                        print("veinte", end="")
                    else:
                        print("veinti", end="")
            else:
                    print (stDecenas[decenas])
                    if unidades != 0:
                        print (" Y ", end="")
            if unidades != 0:
                print (stUnidades[unidades], end = "")                
        print ("")

        

    

       
