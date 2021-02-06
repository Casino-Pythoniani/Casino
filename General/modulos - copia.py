ejemplo_carta_1="""
        ╔═════╗
        ║♥    ║
        ║  k  ║
        ║    ♥║
        ╚═════╝ """

#------------------------------ XA OBTENER CARTA ALEATORIA ---------------------------------------------------
def random_card (): #--Esta funcion crea 1 carta, o la adapamos xa que como parametro introduzcas el numero y cree n cartas o se llama en bucle for en el main .
    carta_player=[] 
    palo=randrange(0,4)
    carta_player.append(baraja[palo])
    carta=randrange(1,13)
    carta_player.append(carta)
    cartas_player.append(carta_player)
    return cartas_player

#--En esta funcion crearemos una carta aleatoria, carta_player es una lista
