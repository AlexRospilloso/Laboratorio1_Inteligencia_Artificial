import random

#Creamos las variables que manejaran la creación del laberinto (filas, columnas y paredes)
laberinto = []
numeroFilas = int(input("Introduzca el número de filas "))
numeroColumnas = int(input("Introduzca el número de columnas "))
numeroParedes = int(input("Introduzca el número de paredes "))
espaciosVacios = numeroFilas * numeroColumnas - numeroParedes

#Creamos el laberinto en base a listas, añadiendo paredes que son #
for i in range(numeroFilas):
    laberinto.append([])
    for j in range(numeroColumnas):
        laberinto[i].append("#")

#Función dedicada a imprimir el laberinto por filas
def imprimirlaberinto():
    for indice in range(numeroFilas):
        print(laberinto[indice])

#Función que crea un espacio vacio en los bordes del laberinto, representados por un " "
def crearespacioorigen():
    indicecasillaorigen = random.randrange(1, 5)
    if indicecasillaorigen == 1 and espaciosVacios > 0:
        espaciocolumna = random.randrange(0, numeroColumnas-1)
        laberinto[0][espaciocolumna] = " "
        puntox = espaciocolumna
        puntoy = 0
        borrarparedes(puntox,puntoy)
    elif indicecasillaorigen == 2 and espaciosVacios > 0:
        espaciofila = random.randrange(0, numeroFilas - 1)
        laberinto[espaciofila][numeroColumnas-1] = " "
        puntox = numeroColumnas - 1
        puntoy = espaciofila
        borrarparedes(puntox,puntoy)
    elif indicecasillaorigen == 3 and espaciosVacios > 0:
        espaciocolumna = random.randrange(0, numeroColumnas-1)
        laberinto[numeroFilas-1][espaciocolumna] = " "
        puntox = espaciocolumna
        puntoy = numeroFilas - 1
        borrarparedes(puntox,puntoy)
    elif indicecasillaorigen == 4 and espaciosVacios > 0:
        espaciofila = random.randrange(0, numeroFilas-1)
        laberinto[espaciofila][0] = " "
        puntox = 0
        puntoy = espaciofila
        borrarparedes(puntox,puntoy)

#Función que borra las paredes a partir del primer punto que creamos, haciendo un camino seguido, reemplazando las paredes # por " "
def borrarparedes(puntox,puntoy):
    espaciosVacios = numeroFilas * numeroColumnas - numeroParedes
    while espaciosVacios > 1:
        direccion = random.randrange(1,5)
        if direccion == 1:
            puntoxauxiliar = puntox + 1
            if puntoxauxiliar <= numeroColumnas - 1:
                puntox = puntoxauxiliar
                if laberinto[puntoy][puntox] == "#":
                    laberinto[puntoy][puntox] = " "
                    espaciosVacios = espaciosVacios - 1
        elif direccion == 2:
            puntoyauxiliar = puntoy + 1
            if puntoyauxiliar <= numeroFilas - 1:
                puntoy = puntoyauxiliar
                if laberinto[puntoy][puntox] == "#":
                    laberinto[puntoy][puntox] = " "
                    espaciosVacios = espaciosVacios - 1
        elif direccion == 3:
            puntoxauxiliar = puntox - 1
            if puntoxauxiliar >= 0:
                puntox = puntoxauxiliar
                if laberinto[puntoy][puntox] == "#":
                    laberinto[puntoy][puntox] = " "
                    espaciosVacios = espaciosVacios - 1
        elif direccion == 4:
            puntoyauxiliar = puntoy - 1
            if puntoyauxiliar >= 0:
                puntoy = puntoyauxiliar
                if laberinto[puntoy][puntox] == "#":
                    laberinto[puntoy][puntox] = " "
                    espaciosVacios = espaciosVacios - 1
    generarcaracter(puntox,puntoy)

#Función que crea el caracter en un punto del laberinto, representado por *
def generarcaracter(puntoxcaracter,puntoycaracter):
        laberinto[puntoycaracter][puntoxcaracter] = "*"
        print("Generando el caracter en la posición "+str(puntoxcaracter)+","+str(puntoycaracter))
        imprimirlaberinto()
        caminarcaracter(puntoxcaracter,puntoycaracter)

#Función que hará que el caracter se mueva por los espacios vacíos permitidos en base a un número de pasos que le daremos
def caminarcaracter(puntoxcaracter,puntoycaracter):
    numeroPasos = int(input("Introduzca el número de pasos que realizará el carácter "))
    while numeroPasos > 0:
        direccion = random.randrange(1,5)
        if direccion == 1:
            puntoxcaracterauxiliar = puntoxcaracter + 1
            if puntoxcaracterauxiliar <= numeroColumnas - 1:
                if laberinto[puntoycaracter][puntoxcaracterauxiliar] == " ":
                    laberinto[puntoycaracter][puntoxcaracter] = " "
                    puntoxcaracter = puntoxcaracterauxiliar
                    laberinto[puntoycaracter][puntoxcaracter] = "*"
                    print("Paso")
                    imprimirlaberinto()
                    numeroPasos = numeroPasos - 1
        if direccion == 2:
            puntoycaracterauxiliar = puntoycaracter + 1
            if puntoycaracterauxiliar <= numeroFilas - 1:
                if laberinto[puntoycaracterauxiliar][puntoxcaracter] == " ":
                    laberinto[puntoycaracter][puntoxcaracter] = " "
                    puntoycaracter = puntoycaracterauxiliar
                    laberinto[puntoycaracter][puntoxcaracter] = "*"
                    print("Paso")
                    imprimirlaberinto()
                    numeroPasos = numeroPasos - 1
        if direccion == 3:
            puntoxcaracterauxiliar = puntoxcaracter - 1
            if puntoxcaracterauxiliar >= 0:
                if laberinto[puntoycaracter][puntoxcaracterauxiliar] == " ":
                    laberinto[puntoycaracter][puntoxcaracter] = " "
                    puntoxcaracter = puntoxcaracterauxiliar
                    laberinto[puntoycaracter][puntoxcaracter] = "*"
                    print("Paso")
                    imprimirlaberinto()
                    numeroPasos = numeroPasos - 1
        if direccion == 4:
            puntoycaracterauxiliar = puntoycaracter - 1
            if puntoycaracterauxiliar >= 0:
                if laberinto[puntoycaracterauxiliar][puntoxcaracter] == " ":
                    laberinto[puntoycaracter][puntoxcaracter] = " "
                    puntoycaracter = puntoycaracterauxiliar
                    laberinto[puntoycaracter][puntoxcaracter] = "*"
                    print("Paso")
                    imprimirlaberinto()
                    numeroPasos = numeroPasos - 1


crearespacioorigen()
