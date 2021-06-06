import random, sys ,time
from os import system, name
from colored import fg, bg, attr
from pynput.keyboard import Listener

def baccarat(ficha):

    #--Globales
    global accion 
    global posicion 
    global apuesta 
    global puntosBanco
    global puntosJugador
    global play 
    global empate
    global color 
    global color_2 
    global color_3 
    global Reset 
    global lista_direccion 
    global cartas_players 
    global baraja 
    global cartas 
    global dicc_card 
    global dicc_palo
    global dicc_palo2
    global elementMesa 
    global fichas

    #--Variables
    fichas = ficha
    accion = 0
    posicion = ""
    apuesta = 0
    puntosBanco = 0
    puntosJugador = 0
    play = True
    empate = False
    color = fg('sky_blue_3') + attr('bold')
    color_2 = bg('dark_green')
    color_3 =  fg('dark_orange') + attr('bold')
    Reset = attr('reset')
    lista_direccion = ["  ","  "]
    cartas_players = []
    baraja = ["corazones","picas","trebol","diamantes"]
    cartas = [1,2,3,4,5,6,7,8,9,10,"j","q","k"]
    dicc_card = {1:"║  1  ║",2:"║  2  ║",3:"║  3  ║",4:"║  4  ║",5:"║  5  ║",6:"║  6  ║",7:"║  7  ║",8:"║  8  ║",9:"║  9  ║",10:"║  10 ║",11:"║  J  ║",12:"║  Q  ║",13:"║  k  ║"}
    dicc_palo = {"corazones":"║♥    ║","picas":"║♠    ║","trebol":"║♣    ║","diamantes":"║♦    ║"}
    dicc_palo2 = {"corazones":"║    ♥║","picas":"║    ♠║","trebol":"║    ♣║","diamantes":"║    ♦║"}
    elementMesa = ["","","","","","","","","","","","","","","","","","","","","","",
                    "","","","","","","","","","","","","","","","","","","","","",""]
    linea, linea_1, linea_3, linea_4 = " "+color_3+"="*128+Reset , "||"+" "+"*"*124+" "+"||" , "||"+" "*3+"*"+" "*118+"*"+" "*3+"||" , "||"+" "*2+"*"+" "*120+"*"+" "*2+"||"

    #---------------------------------------- Funciones --|

    #--Limpia pantalla
    def clear():
      if name == 'nt':
          _ = system('cls')
      else:
          _ = system('clear')

    #--Efecto escribir print tecla por tecla
    def effect(prompt,x):
        for char in prompt:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(x)
        
    #-- Función para cambiar elementos en la mesa
    def switch(x,y,list):
        elementMesa[x] = list[y] 
        return elementMesa
    
    #-- Función que crea cartas aleatorias
    def carta(a,b,c,d,e):
        global cartas_players
        carta = random.randrange(1,14) #-------------La primera carta de este posición elegida en modo aleatorio con el modulo random
        Display(carta)
        switch(a,0,cartas_players)
        switch(b,1,cartas_players)
        switch(c,2,cartas_players)
        switch(d,3,cartas_players)
        switch(e,4,cartas_players)  
        cartas_players = []
        return carta

    #- Funciones para printear las cartas, el dato en entrada es el punto de la carta y como salida los print de las cartas 
    def Display(x):
        carta_player = []
        num = random.randrange(0,4)
        carta_player.append(baraja[num])
        carta_player.append(x)
        cartas_players.append("╔═════╗")
        cartas_players.append(dicc_palo[carta_player[0]])
        cartas_players.append(dicc_card[carta_player[1]])
        cartas_players.append(dicc_palo2[carta_player[0]])
        cartas_players.append("╚═════╝")

        return cartas_players

    #-Función para resetear el punto correcto de una singola carta, como de reglas pasados los 9 puntos vuelve a cero, el dato de entrada es el punto y el dato de salida es el punto reseteado segundo reglas.
    def reset(x):
        if x > 9:
            x = 0
        else:
            pass
        return x

    #Función para resetear la suma de los puntos totales de las cartas, como de reglas pasados los 9 puntos vuelve a cero, el dato de entrada son los puntos totales (la suma de los puntos de cada singola carta obtenida) y el dato de salida son los puntos totales reseteados segundo reglas.
    def reset_2(x):
        if x > 9:
            x = x - 10
        else:
            pass
        return x

    #--Dibujo principal de la mesa
    def disegna():
        clear()
        print(color_2+linea+color_2+" ")
        print(color_3+linea_1)
        print(color_3+"||"+" "*2+"*"+elementMesa[32].rjust(53, " ")+"* | JUGADOR | *".ljust(67," ")+"*"+" "*2+"||")
        print(linea_3)
        print(color_3+"||"+" "*2+"*"+" "*82+elementMesa[30].ljust(38," ")+"*"+" "*2+"||")
        print(color_3+"||"+" "+"*"+elementMesa[0].rjust(61, " ")+elementMesa[5].ljust(28, " ")+elementMesa[20].ljust(33, " ")+"*"+" "+"||")
        print(color_3+"||"+" "*2+"*"+elementMesa[1].rjust(60," ")+elementMesa[6].ljust(28," ")+elementMesa[21].ljust(32," ")+"*"+" "*2+"||")
        print(color_3+"||"+" "*3+"*"+elementMesa[2].rjust(59," ")+elementMesa[7].ljust(28," ")+elementMesa[22].ljust(16," ")+elementMesa[42].center(15," ")+"*"+" "*3+"||")
        print(color_3+"||"+" "*2+"*"+elementMesa[3].rjust(60," ")+elementMesa[8].ljust(28," ")+elementMesa[23].ljust(32," ")+"*"+" "*2+"||")
        print(color_3+"||"+" "+"*"+elementMesa[4].rjust(61, " ")+elementMesa[9].ljust(28, " ")+elementMesa[24].ljust(33, " ")+"*"+" "+"||")
        print(linea_4)
        print(color_3+"||"+" "*3+"*"+elementMesa[38].center(118, " ")+"*"+" "*3+"||")
        print(color_3+"||"+" "*2+"*"+elementMesa[35].ljust(120," ")+"*"+" "*2+"||")
        print(color_3+"||"+" "+"*"+elementMesa[40].center(122," ")+"*"+" "+"||")
        print(color_3+"||"+" "*2+"*"+elementMesa[34].ljust(120," ")+"*"+" "*2+"||")
        print(color_3+"||"+" "*3+"* "+">  <<--BACCARAT-->>  <".center(116, "-")+" *"+" "*3+"||")
        print(linea_4)
        print(color_3+"||"+" "+"*"+" "*83+elementMesa[31].ljust(39," ")+"*"+" "+"||")
        print(color_3+"||"+" "*2+"*"+elementMesa[10].rjust(60, " ")+elementMesa[15].ljust(28, " ")+elementMesa[25].ljust(32, " ")+"*"+" "*2+"||")
        print(color_3+"||"+" "*3+"*"+elementMesa[11].rjust(59," ")+elementMesa[16].ljust(28," ")+elementMesa[26].ljust(31," ")+"*"+" "*3+"||")
        print(color_3+"||"+" "*2+"*"+elementMesa[12].rjust(60," ")+elementMesa[17].ljust(28," ")+elementMesa[27].ljust(18," ")+elementMesa[43].ljust(14," ")+"*"+" "*2+"||")
        print(color_3+"||"+" "+"*"+elementMesa[13].rjust(61," ")+elementMesa[18].ljust(28," ")+elementMesa[28].ljust(33," ")+"*"+" "+"||")
        print(color_3+"||"+" "*2+"*"+elementMesa[14].rjust(60, " ")+elementMesa[19].ljust(28, " ")+elementMesa[29].ljust(32, " ")+"*"+" "*2+"||")
        print(linea_3)
        print(color_3+"||"+" "*2+"*"+elementMesa[39].center(120, " ")+"*"+" "*2+"||")
        print(color_3+"||"+" "+"*"+elementMesa[36].ljust(122," ")+"*"+" "+"||")
        print(color_3+"||"+" "*2+"*"+elementMesa[41].center(120," ")+"*"+" "*2+"||")
        print(color_3+"||"+" "*3+"*"+elementMesa[37].ljust(118," ")+"*"+" "*3+"||")
        print(color_3+"||"+" "*2+"*"+(elementMesa[33].rjust(54, " "))+"* | BANCO | *".ljust(66," ")+"*"+" "*2+"||")
        print(linea_1)
        print(linea+color_2+" "+Reset+"\n")

    #-- Función para el turno del "jugador"
    def turnoJugador():
        global accion
        global puntosBanco
        global lista_direccion

        carta_1 = carta(0,1,2,3,4)
        carta_2 = carta(5,6,7,8,9)
        time.sleep(1.5)
        clear()
        disegna()
        elementMesa[38] = "Puntos: "+str(reset(carta_1))+" "+str(reset(carta_2))
        time.sleep(1.5)
        clear()
        disegna()
        puntosJugador = reset(carta_1) + reset(carta_2)
        puntosJugador = reset_2(puntosJugador)
        elementMesa[40] = "Puntos totales: "+str(puntosJugador)
        time.sleep(1.5)
        clear()
        disegna()
        
        if posicion == "jugador" and reset_2(puntosJugador) <= 7: #-Si el usuario es en posición "jugador" y tiene meno de 8 puntos puede elegir una tercera carta.
            print("\n\n\t\t\t\t\t\t\t    %s%sPress Enter%s" % (fg('sky_blue_2'), attr('bold'),attr('reset')))
            with Listener(on_press=key_recorder) as l: 
                accion = 4
                lista_direccion = ["  ","  "]  
                l.join()
            
            if lista_direccion[0] == "->": #------------------------Si el usuario elige una tercera carta.
                elementMesa[30] = "<*| Carta bonus |*>"
                carta_3 = carta(20,21,22,23,24)    
                elementMesa[38] = "Puntos: "+str(reset(carta_1))+" "+str(reset(carta_2))+" "+str(reset(carta_3))
                puntosJugador = puntosJugador + reset(carta_3)
                puntosJugador = reset_2(puntosJugador) #-Puntos total del jugador
                elementMesa[40] = "Puntos totales: "+str(puntosJugador)
                clear()
                disegna()
            else:
                pass
        else:
            if reset_2(puntosJugador) <= 4 and reset_2(puntosJugador) < reset_2(puntosBanco):
                time.sleep(1)
                elementMesa[30] = "<*| Carta bonus |*>"
                carta_3 = carta(20,21,22,23,24)  
                elementMesa[38] = "Puntos: "+str(reset(carta_1))+" "+str(reset(carta_2))+" "+str(reset(carta_3))
                puntosJugador = puntosJugador + reset(carta_3)
                puntosJugador = reset_2(puntosJugador) #-Puntos total del jugador
                elementMesa[40] = "Puntos totales: "+str(puntosJugador)
        clear()
        disegna()
        time.sleep(1.5)
        return puntosJugador
    
    def turnoBanco():
        global accion
        global puntosJugador        
        global lista_direccion


        carta_4 = carta(10,11,12,13,14)
        carta_5 = carta(15,16,17,18,19)
        time.sleep(1.5)
        clear()
        disegna()
        elementMesa[39] = "Puntos: "+str(reset(carta_4))+" "+str(reset(carta_5))
        time.sleep(1.5)
        clear()
        disegna()
        puntosBanco = reset(carta_4) + reset(carta_5)
        puntosBanco = reset_2(puntosBanco)
        elementMesa[41] = "Puntos totales: "+str(puntosBanco)
        time.sleep(1.5)
        clear()
        disegna()
        if posicion == "banco" and reset_2(puntosBanco) <= 7: #-Si el usuario es en posición "jugador" y tiene meno de 8 puntos puede elegir una tercera carta.
            print("\n\n\t\t\t\t\t\t\t    %s%sPress Enter%s" % (fg('sky_blue_2'), attr('bold'),attr('reset')))
            with Listener(on_press=key_recorder) as l:   
                accion = 4
                lista_direccion = ["  ","  "] 
                l.join()
                
            if lista_direccion[0] == "->": #------------------------Si el usuario elige una tercera carta.
                elementMesa[31] = "<*| Carta bonus |*>"
                carta_6 = carta(25,26,27,28,29)
                elementMesa[39] = "Puntos: "+str(reset(carta_4))+" "+str(reset(carta_5))+" "+str(reset(carta_6))
                puntosBanco = puntosBanco + reset(carta_6)
                puntosBanco = reset_2(puntosBanco) #-Puntos total del jugador
                elementMesa[41] = "Puntos totales: "+str(puntosBanco)
                clear()
                disegna()
            else:
                pass
        else:
            if reset_2(puntosBanco) < reset_2(puntosJugador):
                time.sleep(1)
                elementMesa[31] = "<*| Carta bonus |*>"
                carta_6 = carta(25,26,27,28,29)
                elementMesa[39] = "Puntos: "+str(reset(carta_4))+" "+str(reset(carta_5))+" "+str(reset(carta_6))
                puntosBanco = puntosBanco + reset(carta_6)
                puntosBanco = reset_2(puntosBanco) #-Puntos total del jugador
                elementMesa[41] = "Puntos totales: "+str(puntosBanco)
                time.sleep(1.5)
                clear()
                disegna()
        clear()
        disegna()
        time.sleep(1.5)
        return puntosBanco

    # |---- Función que establece el resultado del juego ----|
    def resultado():
        global puntosJugador
        global puntosBanco
        global fichas
        
        if reset_2(puntosBanco) == reset_2(puntosJugador): #-Si el juego es empacto
            puntosBanco, puntosJugador = empate(puntosBanco,puntosJugador) 

        if reset_2(puntosBanco) > reset_2(puntosJugador): #-Si los puntos del "banco" son mayores de los puntos del "jugador"
            time.sleep (1.5) #-------------------------Pausa temporal del modulo TIME para crear "Suspens".
            elementMesa[43] = "GANADOR!!"
            elementMesa[42] = "Perdedor..."
            clear()
            disegna()
            if posicion == "banco": #------------------------------Si el usuario es en posición "banco"...
                fichas = fichas + apuesta #------------------Suma de fichas apostado al fichas actual. 
                elementMesa[37] = "    Fichas totales: "+str(fichas)
                elementMesa[36] = ""
            else: #------------------------------------------Si el usuario es en posición "jugador"...
                fichas = fichas - apuesta #------------------Resta de fichas apostado al fichas actual. 
                elementMesa[34] = "    Fichas totales: "+str(fichas)
                elementMesa[35] = ""
            clear()
            disegna()
            time.sleep(1.5)
        
        if reset_2(puntosBanco) < reset_2(puntosJugador): #-Si los puntos del "banco" son minores de los puntos del "jugador"
            time.sleep (1.5) #-------------------------Pausa temporal del modulo TIME para crear "Suspens".
            elementMesa[43] = "Perdedor..."
            elementMesa[42] = "GANADOR!!"
            clear()
            disegna()

            if posicion == "jugador": #------------------------------Si el usuario es en posición "jugador"...
                fichas = fichas + apuesta #------------------Suma de fichas apostado al fichas actual.
                elementMesa[34] = "     Fichas totales: "+str(fichas)
                elementMesa[35] = ""
            else: #------------------------------------------Si el usuario es en posición "banco"...
                fichas = fichas - apuesta #------------------Resta de fichas apostado al fichas actual.
                elementMesa[37] = "     Fichas totales: "+str(fichas)
                elementMesa[36] = ""
        clear()
        disegna()
        return fichas

    #--Función para resolver el empate
    def empate(puntosBanco,puntosJugador):
  
        empate = True
        while empate:
            elementMesa[43] = "EMPATE!"
            elementMesa[42] = "EMPATE!"
            time.sleep(1.5)#-------------------------Pausa temporal del modulo TIME para crear "Suspens".
            elementMesa[30] = ""
            elementMesa[31] = ""
            elementMesa[25] = ""  
            elementMesa[26] = "" 
            elementMesa[27] = ""   
            elementMesa[28] = ""  
            elementMesa[29] = ""
            elementMesa[20] = ""  
            elementMesa[21] = ""  
            elementMesa[22] = ""   
            elementMesa[23] = ""   
            elementMesa[24] = "" 
            clear()
            disegna()
            effect("%s%sCarta Bonus para {}.%s".format(nombre) % (fg('red_3a'), attr('bold'), attr('reset')), .1)
            time.sleep(.5)
            if posicion == "jugador": #------------------------------Si el usuario es en posición "jugador"...
                elementMesa[30] = "<*| Carta bonus |*>"
                carta_7 = carta(20,21,22,23,24)
                elementMesa[38] = "Puntos: "+str(reset(carta_7))
                puntosJugador = reset_2(puntosJugador) + reset(carta_7) #-Puntos total del jugador.
                puntosJugador = reset_2(puntosJugador) #-Puntos total del jugador
                elementMesa[40] = "Puntos totales: "+str(puntosJugador)
            else: #------------------------------------------Si el usuario es en posición "banco"...
                elementMesa[31] = "<*| Carta bonus |*>"
                carta_7 = carta(25,26,27,28,29)
                elementMesa[39] = "Puntos: "+str(reset(carta_7))
                puntosBanco = puntosBanco + reset(carta_7)
                puntosBanco = reset_2(puntosBanco) #-Puntos total del jugador
                elementMesa[41] = "Puntos totales: "+str(puntosBanco)
            if reset_2(puntosBanco) != reset_2(puntosJugador):
                empate = False
        clear()  
        disegna()
        time.sleep(.5)  
        return puntosBanco, puntosJugador

    #--Dibujo de presentación
    def dibujo(x,y):
        print('\n\n\n\t\t\t\t\t\t  ',end="")
        effect("%s%sBIENVENIDO AL JUEGO%s" % (fg('sky_blue_2'), attr('bold'),attr('reset')),x)
        effect('''%s%s                                                                                                                                                               
        BBBBBBBBBBBBBB                                                                                              tt          
        B:::::::::::::B                                                                                           tt:t          
        B::::BBBBBB::::B                                                                                         t:::t          
        BB:::B     B::::B                                                                                        t:::t          
          B::B     B::::B   aaaaaaaa        ccccccc      ccccccc     aaaaaaaa   rrrr   rrrrr    aaaaaaaa   ttttttt:::ttttttt    
          B::B     B::::B   a:::::::a     cc:::::::c   cc:::::::c    a:::::::a  r:::rrr:::::r   a:::::::a  t:::::::::::::::t    
          B::BBBBBB::::B    aaaaaaaa:a   c::::::::::c  c:::::::::c   aaaaaaaa:a r::::::::::::r  aaaaaaaa:a t:::::::::::::::t    
          B::::::::::BB            a:a  c::::cccc:::c c:::cccc:::c          a:a rr:::::rr::::r         a:a tttttt:::::tttttt    
          B::BBBBBB::::B      aaaaaa:a  c:::c   ccccc c::c   ccccc     aaaaaa:a  r::::r  r:::r   aaaaaaa:a       t:::t          
          B::B     B::::B   aa:::::::a  c::c          c::c           aa:::::::a  r::::r  rrrrr aa::::::::a       t:::t          
          B::B     B::::B  a:::aaaa::a  c::c          c::c          a:::aaaa::a  r::::r       a::::aaaa::a       t:::t          
          B::B     B::::B a:::a    a:a  c:::c  ccccc  c:::c  ccccc a::::a   a:a  r::::r      a::::a    a:a       t:::t    tttt
        BB:::BBBBBB:::::B a:::a    a:a  c:::cccc:::c  c:::cccc:::c a::::a   a:a  r::::r      a::::a    a:a       t::::tttt:::t
        B::::::::::::::B  a::::aaaa::a  c::::::::::c   c:::::::::c a::::aaaa::a  r::::r      a:::::aaaa::a       tt::::::::::t
        B:::::::::::::B    a:::::::a:a   cc:::::::c     cc::::::c   a:::::::a:a  r::::r       a::::::::a:a        tt:::::::tt
        BBBBBBBBBBBBBB      aaaaaaaa aa   ccccccc        ccccccc     aaaaaaa  aa rrrrrr        aaaaaaaa  aa         ttttttt     %s''' % (fg('dark_orange_3a'), attr('bold'),attr('reset')),y)
        
        time.sleep(.5)
        print("\n\n\n\n\t\t\t\t\t\t     %s%sPress Enter%s" % (fg('sky_blue_2'), attr('bold'),attr('reset')))


    #--Funcion Listener por el pynput module
    def key_recorder(key):
        global accion
        global lista_direccion
        global play
        global elementMesa
        global cartas_players
        global posicion
        global apuesta
        global puntosJugador
        global puntosBanco
        global fichas

        if accion == 0:  #----------accion "0" indica la intro donde se elige si jugar o salir
            clear()
            elementMesa = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
            cartas_players = [] 
            disegna() 
            print("\t\t\t\t\t  " + color + lista_direccion[0] + Reset + "%s%s Jugar%s" % (fg('white'), attr('bold'), attr('reset')) + "\t\t\t\t" + color + lista_direccion[1] + Reset +"%s%s Salir%s" % (   fg('white'), attr('bold'), attr('reset')))
            if key == key.left:
                clear()
                lista_direccion = ["->","  "]
                disegna()
                print("\t\t\t\t\t  " + color + lista_direccion[0] + Reset + "%s%s Jugar%s" % (fg('red_3a'), attr('bold'), attr('reset')) + "\t\t\t\t" + color + lista_direccion[1] + Reset +"%s%s Salir%s" % (fg('white'), attr('bold'), attr('reset')))

            if key == key.right:
                clear()
                lista_direccion = ["  ","->"]
                disegna()
                print("\t\t\t\t\t  " + color + lista_direccion[0] + Reset + "%s%s Jugar%s" % (fg('white'), attr('bold'), attr('reset')) + "\t\t\t\t" + color + lista_direccion[1] + Reset +"%s%s Salir%s" % (fg('red_3a'), attr('bold'), attr('reset')))
            
            if key == key.enter and lista_direccion[0] == "->":
                accion = 1
                lista_direccion = ["  ","  "]
                l.stop()
            
            if key == key.enter and lista_direccion[1] == "->":
                clear()
                print('\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t   ',end="")
                effect("%s%sFichas actuales {}£%s".format(str(fichas)) % (fg('sky_blue_2'), attr('bold'),attr('reset')), .1)
                print('\n\n\t\t\t\t\t\t',end="")
                effect("%s%sAdios {}! Vuelva pronto!%s".format(nombre) % (fg('sky_blue_2'), attr('bold'),attr('reset')), .1)
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                play = False
                l.stop()
                return False 

        if accion == 1:  #accion "1" indica donde se elige la posición donde jugar entre "jugador" o "banco"
            clear()
            disegna()
            print("\t\t\t\t\t\t    %s%s{} elije tu posición entre:%s".format(nombre) % (fg('sky_blue_2'), attr('bold'), attr('reset')))
            print("\n\n\t\t\t\t\t" + color + lista_direccion[0] + Reset + "%s%s  Jugador%s" % (fg('white'), attr('bold'), attr('reset')) + "\t\t\t\t" + color + lista_direccion[1] + Reset +"%s%s  Banco%s" % (fg('white'), attr('bold'), attr('reset')))
            
            if key == key.left:
                clear()
                lista_direccion = ["->","  "]
                disegna()
                print("\t\t\t\t\t\t    %s%s{} elije tu posición entre:%s".format(nombre) % (fg('sky_blue_2'), attr('bold'), attr('reset')))
                print("\n\n\t\t\t\t\t" + color + lista_direccion[0] + Reset + "%s%s  Jugador%s" % (fg('red_3a'), attr('bold'), attr('reset')) + "\t\t\t\t" + color + lista_direccion[1] + Reset +"%s%s  Banco%s" % (fg('white'), attr('bold'), attr('reset')))
                
            if key == key.right:
                clear()
                lista_direccion = ["  ","->"]
                disegna()
                print("\t\t\t\t\t\t    %s%s{} elije tu posición entre:%s".format(nombre) % (fg('sky_blue_2'), attr('bold'), attr('reset')))
                print("\n\n\t\t\t\t\t" + color + lista_direccion[0] + Reset + "%s%s  Jugador%s" % (fg('white'), attr('bold'), attr('reset')) + "\t\t\t\t" + color + lista_direccion[1] + Reset +"%s%s  Banco%s" % (fg('red_3a'), attr('bold'), attr('reset')))
                
            if key == key.enter and lista_direccion[0] == "->":
                posicion = "jugador"
                elementMesa[32] = nombre +" --> "
                elementMesa[33] = "Computer --> "
                elementMesa[34] = "   Fichas totales: " + str(fichas) 
                accion = 2
                l.stop()
                
            if key == key.enter and lista_direccion[1] == "->":
                posicion = "banco"
                elementMesa[32] = "Computer --> "
                elementMesa[33] = nombre +" --> "
                elementMesa[37] = "   Fichas totales: " + str(fichas) 
                accion = 2
                l.stop()

        if accion == 2: #----------------- accion "2" indica donde se elige la apuesta 
            clear()
            disegna()
            print("\t\t\t\t\t    %s%sPara subir la apuesta teclee la tecla arriba%s"% (fg('sky_blue_2'), attr('bold'),attr('reset')))
            
            if key == key.up:
                if apuesta < fichas:
                    apuesta += 10
                    if posicion == "jugador":
                        elementMesa[35] = "     Apuesta: " + str(apuesta)
                        elementMesa[36] = ""
                    else:
                        elementMesa[36] = "       Apuesta: " + str(apuesta)
                        elementMesa[35] = ""
                    clear()
                    disegna()
                    print("\t\t\t\t\t    %s%sPara subir la apuesta teclee la tecla arriba%s"% (fg('sky_blue_2'), attr('bold'),attr('reset')))
                    print("\n\t\t\t\t\t    %s%sPara Bajar la apuesta teclee la tecla abajo%s"% (fg('sky_blue_2'), attr('bold'),attr('reset')))
                    print('\n\t\t\t\t\t     %s%sCuando su apuesta es lista teclee: "Enter" %s'% (fg('sky_blue_2'), attr('bold'),attr('reset')))
                    
            if key == key.down:
                if apuesta > 0: 
                    apuesta -= 10
                    if posicion == "jugador":
                        elementMesa[35] = "     Apuesta: " + str(apuesta)
                        elementMesa[36] = ""
                    else:
                        elementMesa[36] = "       Apuesta: " + str(apuesta)
                        elementMesa[35] = ""
                    clear()
                    disegna()
                    print("\t\t\t\t\t    %s%sPara subir la apuesta teclee la tecla arriba%s"% (fg('sky_blue_2'), attr('bold'),attr('reset')))
                    print("\n\t\t\t\t\t    %s%sPara Bajar la apuesta teclee la tecla abajo%s"% (fg('sky_blue_2'), attr('bold'),attr('reset')))
                    print('\n\t\t\t\t\t     %s%sCuando su apuesta es lista teclee: "Enter" %s'% (fg('sky_blue_2'), attr('bold'),attr('reset')))
                    
            if key == key.enter and apuesta >= 10:
                clear()
                disegna()
                accion = 3
                l.stop()

        if accion == 3: #   <---- accion "3" es donde se sacan las cartas y se juega ----|
            clear()
            disegna()
            if posicion == "jugador":
                print('\n\t\t\t\t\t\t\t   ',end="")
                effect("%s%sTurno Jugador%s" % (fg('red_3a'), attr('bold'), attr('reset')), .1)
                puntosJugador = turnoJugador()
                print('\n\t\t\t\t\t\t\t    ',end="")
                effect("%s%sTurno Banco%s" % (fg('red_3a'), attr('bold'), attr('reset')), .1)
                puntosBanco = turnoBanco()
            else:
                print('\n\t\t\t\t\t\t\t    ',end="")
                effect("%s%sTurno Banco%s" % (fg('red_3a'), attr('bold'), attr('reset')), .1)
                puntosBanco = turnoBanco()
                print('\n\t\t\t\t\t\t\t   ',end="")
                effect("%s%sTurno Jugador%s" % (fg('red_3a'), attr('bold'), attr('reset')), .1)
                puntosJugador = turnoJugador()
            resultado()
            print("\n\n\t\t\t\t\t\t\t    %s%sPress Enter%s" % (fg('sky_blue_2'), attr('bold'),attr('reset')))
            lista_direccion = ["  ","  "]
            elementMesa = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
            cartas_players = [] 
            accion = 0
            apuesta = 0
            l.stop() 

        if accion == 4: #   <---- accion "4" es donde se elige si sacar la carta bonus cuando los puntos son muy bajos----|
            clear()
            disegna()
            print('\n\t\t\t\t\t\t       ',end="")
            print("%s%sQuieres una carta más?%s" % (fg('red_3a'), attr('bold'), attr('reset')))
            print("\n\t\t\t\t\t   " + color + lista_direccion[0] + Reset + "%s%s  Si%s" % (fg('white'), attr('bold'), attr('reset')) + "\t\t\t\t" + color + lista_direccion[1] + Reset +"%s%s  No%s" % (fg('white'), attr('bold'), attr('reset')))
            if key == key.left:
                clear()
                lista_direccion = ["->","  "] 
                disegna()
                print('\n\t\t\t\t\t\t       ',end="")
                print("%s%sQuieres una carta más?%s" % (fg('red_3a'), attr('bold'), attr('reset')))
                print("\n\t\t\t\t\t   " + color + lista_direccion[0] + Reset + "%s%s  Si%s" % (fg('red_3a'), attr('bold'), attr('reset')) + "\t\t\t\t" + color + lista_direccion[1] + Reset +"%s%s  No%s" % (fg('white'), attr('bold'), attr('reset')))
            
            if key == key.right:
                clear()
                lista_direccion = ["  ","->"]
                disegna()
                print('\n\t\t\t\t\t\t       ',end="")
                print("%s%sQuieres una carta más?%s" % (fg('red_3a'), attr('bold'), attr('reset')))
                print("\n\t\t\t\t\t   " + color + lista_direccion[0] + Reset + "%s%s  Si%s" % (fg('white'), attr('bold'), attr('reset')) + "\t\t\t\t" + color + lista_direccion[1] + Reset +"%s%s  No%s" % (fg('red_3a'), attr('bold'), attr('reset')))


            if key == key.enter and lista_direccion[0] == "->":
                l.stop()
                return False
            
            if key == key.enter and lista_direccion[1] == "->":
                l.stop()
                return False
    
   
    
   
        return accion
    
    #---- Intro
    nombre = input("\n\t\t\t\t\t%s%s        Introduzca su nombre: %s" % (fg('sky_blue_2'), attr('bold'),attr('reset'))).title()
    clear()
    dibujo(0.01,.001)

    #---- programa
    while play:
        with Listener(on_press=key_recorder) as l:
            l.join()

        if fichas == 0 or fichas >= 5000:
            if fichas >= 5000:
                clear()
                print('\n\t\t\t\t\t\t',end="")
                effect("Has ganado el maximo importe establecido!!",.1)
                print('\n\t\t\t\t\t\t  ',end="")
                effect("Adios "+nombre+"! Vuelva pronto!",.1)
                print('\n\n\n\n\n\n\n\n\n\n\n\n')
                play = False
            else:
                clear()
                print('\n\t\t\t\t\t\t',end="")
                effect("Has perdido todas la fichas",.1)
                print('\n\t\t\t\t\t\t  ',end="")
                effect("Adios "+nombre+"! Vuelva pronto!",.1)
                print('\n\n\n\n\n\n\n\n\n\n\n\n')        
                play = False
        else:
            pass
    
    return fichas , exit()
    



baccarat(500)