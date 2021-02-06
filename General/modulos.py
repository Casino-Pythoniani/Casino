# Es solo un ejemplo, asi no se puede printear cartas seguidas.
ejemplo_carta_1="""  
        ╔═════╗
        ║♥    ║
        ║  k  ║
        ║    ♥║
        ╚═════╝ """

#------------------------------ XA OBTENER CARTA ALEATORIA ---------------------------------------------------

from random import randrange  #!!!  necesitamos tener importado randrange:   from random import randrange
#!!!x probar!!! limites variable etc...

def random_card (num_cartas,lista_cartas): #--Esta funcion crea cartas aleatorias, el primer parametro ha de ser un int y el segundo una lista

    palo=["corazones","picas","trebol","diamantes"]
    for i in range (num_cartas):  #-- Xa crear n cantidad de cartas
        carta_player=[]  #-- Lista xa informacion de 1 carta, la que estamos haciendo
        a=randrange(0,4)#-- Xa elegir palo random de la lista palo  
        carta_player.append(palo[a]) #-- Añadimos el palo de la carta en curso a la lista
        numero=randrange(1,13) #-- Xa elegir numero carta de forma random
        carta_player.append(numero) #-- Añadimos el numero de la carta en curso a la lista
        lista_cartas.append(carta_player) #-- Añadimos la carta random ya creada a una lista de cartas dada x parametro ( nuestra mano)
    return lista_cartas #-- Devolvemos la lista dada x parametro que ahora contendra nuestra mano mas las cartas nuevas en una lista de listas.

#--En esta funcion crearemos cartas aleatorias,y las añadiremos a una lista (nuestra mano de cartas) dada x parametro ya que puede contener cartas ya durante el juego
#    esa lista la pondremos en return asi nos devolverá las cartas que ya teniamos (en mano) y las creadas por nuestra funcion.
#--La función tiene el siguiente funcionamiento: El primer bucle sirve xa crear n cantidad de cartas, carta_player es una lista donde guardaremos la información (numero y palo)
#    de una carta. Creamos un palo aleatorio y un numero aleatorio, lo añadimos a carta_player que contiene la informacion de una sola carta ( la creada) y añadimos esta lista a otra
#    dada por parámetro que sera nuestra mano. hacemos return de esta lista.
#-- EJEMPLO ==> mi_mano = random_card (2,mi_mano), necesitamos importar : from random import randrange

#----- DEJO COMENTADO EL TEST QUE LE HICE A LA FUNCION-------

##mi_mano=[]
##mi_mano=random_card(5,mi_mano)
##print (mi_mano)


#-------------------------------XA IMPRIMIR LAS CARTAS---------------------------------------------------------


def print_card (list_of_cards): #--Esta función imprime las cartas de una lista de listas <== IMP. que sera la mano del jugador

    dicc_palo={"corazones":"║♥    ║","picas":"║♠    ║","trebol":"║♣    ║","diamantes":"║♦    ║"}
    dicc_palo2={"corazones":"║    ♥║","picas":"║    ♠║","trebol":"║    ♣║","diamantes":"║    ♦║"}
    dicc_card={1:"║  1  ║",2:"║  2  ║",3:"║  3  ║",4:"║  4  ║",5:"║  5  ║",6:"║  6  ║",7:"║  7  ║",8:"║  8  ║",9:"║  9  ║",10:"║  10 ║",11:"║  J  ║",12:"║  Q  ║",13:"║  k  ║"}

    num_cartas=len(list_of_cards)#--Xa saber cuantas cartas vamos a printear
    
    for i in range (num_cartas): #-- Xa imprimir linea a linea n cartas 
        print ("╔═════╗",end="") #--Imprime la parte de arriba
    print("")
    for i in range (num_cartas):    
       print (dicc_palo[list_of_cards [i][0]],end="") #--Usa un diccionario xa decirle que figura debe printear, n veces
    print("")
    for i in range (num_cartas):                      #--Igual que la anterior pero con numeros
        print(dicc_card[list_of_cards [i][1]],end="")
    print("")
    for i in range (num_cartas):    
       print (dicc_palo2[list_of_cards [i][0]],end="")#--Xa la figura de abajo, n veces
    print("")
    for i in range (num_cartas): #--Parte de abajo de la carta, n veces
        print("╚═════╝",end="")
    print("")

#--Esta funcion imprime cartas una al lado de otra, para que sea asi debe ser linea a linea. Por eso utilizamos bucles for (la cantidad de cartas a printear)
#   para los palos y los numeros. Tambien usamos diccionarios que segun lo que introduzcas imprime. x ej :"picas":"║♠    ║" y asi vamos cambiando segun que cartas.    

#----- DEJO COMENTADO EL TEST QUE LE HICE A LA FUNCION-------

##mi_mano=[['picas', 2], ['corazones', 10], ['picas', 4], ['corazones', 4], ['trebol', 6]]
##print_card (mi_mano)


#------------------MODULO QUE MUESTRA LAS IMAGENES DEL TRAGAPERRAS--------------#

import random

# Las intrucciones para imprimir las imagenes del tragaperras.
# Falta implementarla en el tragaperras como un modulo, para que funcione.

#--------------Función para mostrar las imágenes------------------------#
# LAS SIGUIENTES FUNCIONES SE DEBEN PROBAR AL FINAL DE ESTE MÓDULO, POR LAS VARIABLES.
def rueda(pri,seg,ter): # Requerimos de 3 valores para sacar las imagenes.
    print("\t ╔" + "═"*11 + "╗\t ╔" + "═"*11 + "╗\t ╔" + "═"*11 + "╗") # primera linea
    for x in range(6): # Bucle for para sacar la imagen entera
        print("\t",dicc[pri][x],"\t",dicc[seg][x],"\t",dicc[ter][x]) 
    print("\t ╚" + "═"*11 + "╝\t ╚" + "═"*11 + "╝\t ╚" + "═"*11 + "╝") # ultima linea

# El bucle usa los numeros para imprimir la variable del diccionario.
# Ejemplo: diccionario con clave[1] y valor numerico[0] imprime la variable (0) de la clave (1)
# Explicación: Le damos un valor que la funcion recoge como una clave del diccionario y este imprime la imagen.


#--------------Función para ir cambiando las imágenes, en caso de no ganar--------------#
def aleat(): # Una función para mostrar aleatoriamente las imagenes que te da el juego.
    # Los valores se dan de esta forma debido a que no se puede hacer usando un bucle.
    pri=random.randint(1,3) 
    seg=random.randint(1,3)
    ter=random.randint(1,3)
    if pri==seg==ter: # Valida si todos las imagenes son iguales.
        seg += 1 # Le suma 1 al valor de la segunda imagen, para que sea diferente del resto.
        if seg not in dicc: # Si el valor de la segunda imagen no esta asociado a ninguna clave del diccionario hace esta acción.
            seg -= 2 # Le resta 2 al valor de la segunda imagen, para que sea diferente del resto.
    rueda(pri,seg,ter) # Llama a la función que muestra las imagenes.
    return

# Si hay problemas con el programa del juego, es posible que le estén afectando las variables.
# Recomiendo usar las variables de esta forma, ya que sería código innecesario dentro del programa final.
# En cualquier caso las dos cosas hacen lo mismo.

# Variables para mostrar un diamante
di1="║ " + "╔"+"═"*7+"╗"+ " ║"
di2="║ " + "╚╗"+" "*5+"╔╝" + " ║"
di3="║  " + "╚╗"+" "*3+"╔╝" + "  ║"
di4="║   " + "╚╗"+" "+"╔╝" "   ║"
di5="║    " + "╚"+"═"+"╝" + "    ║"
di6="║" + " "*11 + "║"
diam=[di1,di2,di3,di4,di5,di6]
# Variables para mostrar una fresa
fre1="║ " + " "*5+"╔═╗" + "  ║"
fre2="║ " + "╔"+"═"*4+"╝ ╚╗" + " ║"
fre3="║ " + "║"+" "*5+"╔═╝" + " ║"
fre4="║ " +"║"+" "*5+"║" + "   ║"
fre5="║ " +"╚"+"═"*5+"╝" + "   ║"
fre6="║" + " "*11 + "║"
fres=[fre1,fre2,fre3,fre4,fre5,fre6]
# Variables para mostrar otra imagen
ot1="║ "+"╗"+" "*7+"╔"+" ║"
ot2="║ "+"╚═╗"+" "*3+"╔═╝"+" ║"
ot3="║   "+"╚═╗"+"═╝"+" "*2+" ║"
ot4="║   "+"╔═╝"+"═╗"+" "*2+" ║"
ot5="║ "+"╔═╝"+" "*3+"╚═╗"+" ║"
ot6="║ "+"╝"+" "*7+"╚"+" ║"
otr=[ot1,ot2,ot3,ot4,ot5,ot6]
# Diccionario con las listas de las formas.
dicc={1:diam,2:fres,3:otr}

#----------------TEST DEL MÓDULO-----------#
##rueda(1,2,3)
##aleat()

