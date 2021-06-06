import time
import random, sys ,time
from os import system, name
from colored import fg, bg, attr
from pynput.keyboard import Listener


def baccarat(fichas):
    play = True
    
    class Player:
        def __init__(self,  puntosTotales, nombre = "", fichas = 0, apuesta = 0, accion = 0, posicion = ""):
            self.puntoTotales = puntosTotales
            self.nombre = nombre
            self.fichas = fichas
            self.apuesta = apuesta
            self.accion = accion
            self.posicion = posicion

        def acciones(self):

            def key_recorder(key):
                global play

                if self.accion == 0:  #----------accion "0" indica la intro donde se elige si jugar o salir
                    Dibujo.clear()
                    Dibujo.disegna() 
                    print("\t\t\t\t\t  " + Dibujo.color + Dibujo.lista_direccion[0] + Dibujo.Reset + "%s%s Jugar%s" % (fg('white'), attr('bold'), attr('reset')) + "\t\t\t\t" + Dibujo.color + Dibujo.lista_direccion[1] + Dibujo.Reset +"%s%s Salir%s" % (   fg('white'), attr('bold'), attr('reset')))
                    if key == key.left:
                        Dibujo.clear()
                        Dibujo.lista_direccion = ["->","  "]
                        Dibujo.disegna()
                        print("\t\t\t\t\t  " + Dibujo.color + Dibujo.lista_direccion[0] + Dibujo.Reset + "%s%s Jugar%s" % (fg('red_3a'), attr('bold'), attr('reset')) + "\t\t\t\t" + Dibujo.color + Dibujo.lista_direccion[1] + Dibujo.Reset +"%s%s Salir%s" % (fg('white'), attr('bold'), attr('reset')))
                    
                    if key == key.right:
                        Dibujo.clear()
                        Dibujo.lista_direccion = ["  ","->"]
                        Dibujo.disegna()
                        print("\t\t\t\t\t  " + Dibujo.color + Dibujo.lista_direccion[0] + Dibujo.Reset + "%s%s Jugar%s" % (fg('white'), attr('bold'), attr('reset')) + "\t\t\t\t" + Dibujo.color + Dibujo.lista_direccion[1] + Dibujo.Reset +"%s%s Salir%s" % (fg('red_3a'), attr('bold'), attr('reset')))
                    
                    if key == key.enter and Dibujo.lista_direccion[0] == "->":
                        self.accion = 1
                        Dibujo.lista_direccion = ["  ","  "]
                        l.stop()
                    
                    if key == key.enter and Dibujo.lista_direccion[1] == "->":
                        Dibujo.clear()
                        print('\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t   ',end="")
                        Dibujo.effect("%s%sFichas actuales {}£%s".format(str(self.fichas)) % (fg('sky_blue_2'), attr('bold'),attr('reset')), .1)
                        print('\n\n\t\t\t\t\t\t',end="")
                        Dibujo.effect("%s%sAdios {}! Vuelva pronto!%s".format(self.nombre) % (fg('sky_blue_2'), attr('bold'),attr('reset')), .1)
                        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                        play = False
                        l.stop()
                        return False

                if self.accion == 1:  #accion "1" indica donde se elige la posición donde jugar entre "jugador" o "banco"
                    Dibujo.clear()
                    Dibujo.disegna()
                    print("\t\t\t\t\t\t    %s%s{} elije tu posición entre:%s".format(self.nombre) % (fg('sky_blue_2'), attr('bold'), attr('reset')))
                    print("\n\n\t\t\t\t\t" + Dibujo.color + Dibujo.lista_direccion[0] + Dibujo.Reset + "%s%s  Jugador%s" % (fg('white'), attr('bold'), attr('reset')) + "\t\t\t\t" + Dibujo.color + Dibujo.lista_direccion[1] + Dibujo.Reset +"%s%s  Banco%s" % (fg('white'), attr('bold'), attr('reset')))
                    
                    if key == key.left:
                        Dibujo.clear()
                        Dibujo.lista_direccion = ["->","  "]
                        Dibujo.disegna()
                        print("\t\t\t\t\t\t    %s%s{} elije tu posición entre:%s".format(self.nombre) % (fg('sky_blue_2'), attr('bold'), attr('reset')))
                        print("\n\n\t\t\t\t\t" + Dibujo.color + Dibujo.lista_direccion[0] + Dibujo.Reset + "%s%s  Jugador%s" % (fg('red_3a'), attr('bold'), attr('reset')) + "\t\t\t\t" + Dibujo.color + Dibujo.lista_direccion[1] + Dibujo.Reset +"%s%s  Banco%s" % (fg('white'), attr('bold'), attr('reset')))
                        
                    if key == key.right:
                        Dibujo.clear()
                        Dibujo.lista_direccion = ["  ","->"]
                        Dibujo.disegna()
                        print("\t\t\t\t\t\t    %s%s{} elije tu posición entre:%s".format(self.nombre) % (fg('sky_blue_2'), attr('bold'), attr('reset')))
                        print("\n\n\t\t\t\t\t" + Dibujo.color + Dibujo.lista_direccion[0] + Dibujo.Reset + "%s%s  Jugador%s" % (fg('white'), attr('bold'), attr('reset')) + "\t\t\t\t" + Dibujo.color + Dibujo.lista_direccion[1] + Dibujo.Reset +"%s%s  Banco%s" % (fg('red_3a'), attr('bold'), attr('reset')))
                        
                    if key == key.enter and Dibujo.lista_direccion[0] == "->":
                        self.posicion = "jugador"
                        Dibujo.elementMesa[32] = nombre +" --> "
                        Dibujo.elementMesa[33] = "Computer --> "
                        Dibujo.elementMesa[34] = "   Fichas totales: " + str(self.fichas) 
                        self.accion = 2
                        l.stop()
                        
                    if key == key.enter and Dibujo.lista_direccion[1] == "->":
                        self.posicion = "banco"
                        Dibujo.elementMesa[32] = "Computer --> "
                        Dibujo.elementMesa[33] = nombre +" --> "
                        Dibujo.elementMesa[37] = "   Fichas totales: " + str(self.fichas) 
                        self.accion = 2
                        l.stop()
                if self.accion == 2: #----------------- accion "2" indica donde se elige la apuesta 
                    Dibujo.clear()
                    Dibujo.disegna()
                    print("\t\t\t\t\t    %s%sPara subir la apuesta teclee la tecla arriba%s"% (fg('sky_blue_2'), attr('bold'),attr('reset')))
                    
                    if key == key.up:
                        if self.apuesta < self.fichas:
                            self.apuesta += 10
                            if self.posicion == "jugador":
                                Dibujo.elementMesa[35] = "     Apuesta: " + str(self.apuesta)
                                Dibujo.elementMesa[36] = ""
                            else:
                                Dibujo.elementMesa[36] = "       Apuesta: " + str(self.apuesta)
                                Dibujo.elementMesa[35] = ""
                            Dibujo.clear()
                            Dibujo.disegna()
                            print("\t\t\t\t\t    %s%sPara subir la apuesta teclee la tecla arriba%s"% (fg('sky_blue_2'), attr('bold'),attr('reset')))
                            print("\n\t\t\t\t\t    %s%sPara Bajar la apuesta teclee la tecla abajo%s"% (fg('sky_blue_2'), attr('bold'),attr('reset')))
                            print('\n\t\t\t\t\t     %s%sCuando su apuesta es lista teclee: "Enter" %s'% (fg('sky_blue_2'), attr('bold'),attr('reset')))
                            
                    if key == key.down:
                        if self.apuesta > 0: 
                            self.apuesta -= 10
                            if self.posicion == "jugador":
                                Dibujo.elementMesa[35] = "     Apuesta: " + str(self.apuesta)
                                Dibujo.elementMesa[36] = ""
                            else:
                                Dibujo.elementMesa[36] = "       Apuesta: " + str(self.apuesta)
                                Dibujo.elementMesa[35] = ""
                            Dibujo.clear()
                            Dibujo.disegna()
                            print("\t\t\t\t\t    %s%sPara subir la apuesta teclee la tecla arriba%s"% (fg('sky_blue_2'), attr('bold'),attr('reset')))
                            print("\n\t\t\t\t\t    %s%sPara Bajar la apuesta teclee la tecla abajo%s"% (fg('sky_blue_2'), attr('bold'),attr('reset')))
                            print('\n\t\t\t\t\t     %s%sCuando su apuesta es lista teclee: "Enter" %s'% (fg('sky_blue_2'), attr('bold'),attr('reset')))
                            
                    if key == key.enter and self.apuesta >= 10:
                        Dibujo.clear()
                        Dibujo.disegna()
                        self.accion = 3
                        l.stop()
                
                if self.accion == 3: #   <---- accion "3" es donde se sacan las cartas y se juega ----|
                    Dibujo.clear()
                    Dibujo.disegna()
                    turnos()
                    Dibujo.listasBasias()
                    self.accion = 0
                    self.apuesta = 0
                    l.stop()

                if self.accion == 4: #   <---- accion "4" es donde se elige si sacar la carta bonus cuando los puntos son muy bajos----|
                    Dibujo.clear()
                    Dibujo.disegna()
                    print('\n\t\t\t\t\t\t       ',end="")
                    print("%s%sQuieres una carta más?%s" % (fg('red_3a'), attr('bold'), attr('reset')))
                    print("\n\t\t\t\t\t   " + Dibujo.color + Dibujo.lista_direccion[0] + Dibujo.Reset + "%s%s  Si%s" % (fg('white'), attr('bold'), attr('reset')) + "\t\t\t\t" + Dibujo.color + Dibujo.lista_direccion[1] + Dibujo.Reset +"%s%s  No%s" % (fg('white'), attr('bold'), attr('reset')))
                    if key == key.left:
                        Dibujo.clear()
                        Dibujo.lista_direccion = ["->","  "] 
                        Dibujo.disegna()
                        print('\n\t\t\t\t\t\t       ',end="")
                        print("%s%sQuieres una carta más?%s" % (fg('red_3a'), attr('bold'), attr('reset')))
                        print("\n\t\t\t\t\t   " + Dibujo.color + Dibujo.
                        lista_direccion[0] + Dibujo.Reset + "%s%s  Si%s" % (fg('red_3a'), attr('bold'), attr('reset')) + "\t\t\t\t" + Dibujo.color + Dibujo.lista_direccion[1] + Dibujo.Reset +"%s%s  No%s" % (fg('white'), attr('bold'), attr('reset')))
                    
                    if key == key.right:
                        Dibujo.clear()
                        Dibujo.lista_direccion = ["  ","->"]
                        Dibujo.disegna()
                        print('\n\t\t\t\t\t\t       ',end="")
                        print("%s%sQuieres una carta más?%s" % (fg('red_3a'), attr('bold'), attr('reset')))
                        print("\n\t\t\t\t\t   " + Dibujo.color + Dibujo.lista_direccion[0] + Dibujo.Reset + "%s%s  Si%s" % (fg('white'), attr('bold'), attr('reset')) + "\t\t\t\t" + Dibujo.color + Dibujo.lista_direccion[1] + Dibujo.Reset +"%s%s  No%s" % (fg('red_3a'), attr('bold'), attr('reset')))
                    
                    if key == key.enter and Dibujo.lista_direccion[0] == "->":
                        
                        return False

                    if key == key.enter and Dibujo.lista_direccion[1] == "->":
                        return False

            with Listener(on_press=key_recorder) as l:
                l.join()
            return 

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




            #-- Función para el turno del "jugador"
        def puntos(self,a,b,c,d,e,f,g,h,i,l,m,n,o,p,q,r,s,t,u):
            
            carta_1 = Cartas.generarCarta(a,b,c,d,e)
            carta_2 = Cartas.generarCarta(f,g,h,i,l)
            time.sleep(1.5)
            Dibujo.clear()
            Dibujo.disegna()
            punto_1 = Player.reset(carta_1)
            punto_2 = Player.reset(carta_2)
            Dibujo.elementMesa[m] = "Puntos: "+str(punto_1)+" "+str(punto_2)
            time.sleep(1.5)
            Dibujo.clear()
            Dibujo.disegna()
            self.puntoTotales = punto_1 + punto_2
            self.puntoTotales = Player.reset_2(self.puntoTotales)
            Dibujo.elementMesa[n] = "Puntos totales: "+str(self.puntoTotales)
            time.sleep(1.5)
            Dibujo.clear()
            Dibujo.disegna()
            
            if u == True and Player.reset_2(jugador.puntoTotales) <= 7: #-Si el usuario es en posición "jugador" y tiene meno de 8 puntos puede elegir una tercera carta.
                print("\n\n\t\t\t\t\t\t\t    %s%sPress Enter%s" % (fg('sky_blue_2'), attr('bold'),attr('reset')))
                jugador.accion = 4
                Dibujo.lista_direccion = ["  ","  "] 
                jugador.acciones()
                
                if Dibujo.lista_direccion[0] == "->": #------------------------Si el usuario elige una tercera carta.
                    Dibujo.elementMesa[o] = "<*| Carta bonus |*>"
                    carta_3 = Cartas.generarCarta(p,q,r,s,t) 
                    punto_3 = Player.reset(carta_3)   
                    Dibujo.elementMesa[m] = "Puntos: "+str(punto_1)+" "+str(punto_2)+" "+str(punto_3)
                    self.puntoTotales = self.puntoTotales + punto_3
                    self.puntoTotales = Player.reset_2(self.puntoTotales) #-Puntos total del jugador
                    Dibujo.elementMesa[n] = "Puntos totales: "+str(self.puntoTotales)  
                else:
                    pass
            else:
                if Player.reset_2(computer.puntoTotales) < Player.reset_2(jugador.puntoTotales):
                    time.sleep(1)
                    Dibujo.elementMesa[o] = "<*| Carta bonus |*>"
                    carta_3 = Cartas.generarCarta(p,q,r,s,t)  
                    punto_3 = Player.reset(carta_3) 
                    Dibujo.elementMesa[m] = "Puntos: "+str(punto_1)+" "+str(punto_2)+" "+str(punto_3)
                    self.puntoTotales = self.puntoTotales + punto_3
                    self.puntoTotales = Player.reset_2(self.puntoTotales) #-Puntos total del jugador
                    Dibujo.elementMesa[n] = "Puntos totales: "+str(self.puntoTotales)   
            Dibujo.clear()
            Dibujo.disegna()
            time.sleep(1.5)
            return self.puntoTotales

        # |---- Función que establece el resultado del juego ----|
        def resultado(self):
            if self.puntoTotales == computer.puntoTotales: #-Si el juego es empacto
                jugador.empate() 

            if computer.puntoTotales > self.puntoTotales: #-Si los puntos del "banco" son mayores de los puntos del "jugador"

                time.sleep (1.5) #-------------------------Pausa temporal del modulo TIME para crear "Suspens".
                self.fichas = self.fichas - self.apuesta #------------------Suma de fichas apostado al fichas actual. 
               
                if self.posicion == "banco": #------------------------------Si el usuario es en posición "banco"...
                    Dibujo.elementMesa[37] = "    Fichas totales: "+str(self.fichas)
                    Dibujo.elementMesa[36] = ""
                    Dibujo.elementMesa[42] = "GANADOR!!"
                    Dibujo.elementMesa[43] = "Perdedor..."
                else: #------------------------------------------Si el usuario es en posición "jugador"...
                    Dibujo.elementMesa[34] = "    Fichas totales: "+str(self.fichas)
                    Dibujo.elementMesa[35] = ""
                    Dibujo.elementMesa[43] = "GANADOR!!"
                    Dibujo.elementMesa[42] = "Perdedor..."
                Dibujo.clear()
                Dibujo.disegna()
                time.sleep(1.5)
            
            if computer.puntoTotales < self.puntoTotales: #-Si los puntos del "banco" son minores de los puntos del "jugador"
                time.sleep (1.5) #-------------------------Pausa temporal del modulo TIME para crear "Suspens".
                self.fichas = self.fichas + self.apuesta #------------------Suma de fichas apostado al fichas actual.

                if self.posicion == "jugador": #------------------------------Si el usuario es en posición "jugador"...
                    Dibujo.elementMesa[34] = "     Fichas totales: "+str(fichas)
                    Dibujo.elementMesa[35] = ""
                    Dibujo.elementMesa[42] = "GANADOR!!"
                    Dibujo.elementMesa[43] = "Perdedor..."
                else: #------------------------------------------Si el usuario es en posición "banco"...
                    Dibujo.elementMesa[37] = "     Fichas totales: "+str(fichas)
                    Dibujo.elementMesa[36] = ""
                    Dibujo.elementMesa[43] = "GANADOR!!"
                    Dibujo.elementMesa[42] = "Perdedor..."
            Dibujo.clear()
            Dibujo.disegna()
            return fichas

        #--Función para resolver el empate
        def empate(self):
  
            empate = True
            while empate:
                Dibujo.elementMesa[43] = "EMPATE!"
                Dibujo.elementMesa[42] = "EMPATE!"
                time.sleep(1.5)#-------------------------Pausa temporal del modulo TIME para crear "Suspens".
                Dibujo.elementMesa[30] = ""
                Dibujo.elementMesa[31] = ""
                Dibujo.elementMesa[25] = ""  
                Dibujo.elementMesa[26] = "" 
                Dibujo.elementMesa[27] = ""   
                Dibujo.elementMesa[28] = ""  
                Dibujo.elementMesa[29] = ""
                Dibujo.elementMesa[20] = ""  
                Dibujo.elementMesa[21] = ""  
                Dibujo.elementMesa[22] = ""   
                Dibujo.elementMesa[23] = ""   
                Dibujo.elementMesa[24] = "" 
                Dibujo.clear()
                Dibujo.disegna()
                print('\n\t\t\t\t\t\t\t    ',end="")
                Dibujo.effect("%s%sCarta Bonus para {}.%s".format(nombre) % (fg('red_3a'), attr('bold'), attr('reset')), .1)
                time.sleep(1.5)
                if self.posicion == "jugador": #------------------------------Si el usuario es en posición "jugador"...
                    Dibujo.elementMesa[30] = "<*| Carta bonus |*>"
                    carta_4 = Cartas.generarCarta(20,21,22,23,24) 
                    punto_4 = Player.reset(carta_4)   
                    Dibujo.elementMesa[38] = "Puntos: " + str(punto_4)
                    self.puntoTotales = self.puntoTotales + punto_4
                    self.puntoTotales = Player.reset_2(self.puntoTotales) #-Puntos total del jugador
                    Dibujo.elementMesa[40] = "Puntos totales: "+str(self.puntoTotales) 
                else: #------------------------------------------Si el usuario es en posición "banco"...
                    Dibujo.elementMesa[31] = "<*| Carta bonus |*>"
                    carta_4 = Cartas.generarCarta(25,26,27,28,29)
                    punto_4 = Player.reset(carta_4)   
                    Dibujo.elementMesa[39] = "Puntos: " + str(punto_4)
                    self.puntoTotales = self.puntoTotales + punto_4
                    self.puntoTotales = Player.reset_2(self.puntoTotales) #-Puntos total del jugador
                    Dibujo.elementMesa[41] = "Puntos totales: "+str(self.puntoTotales) 

                if self.puntoTotales != computer.puntoTotales:
                    empate = False
            Dibujo.clear()  
            Dibujo.disegna()
            time.sleep(.5)  
            
            return 
            
    class Cartas:
        cartas_players = []
        baraja = ["corazones","picas","trebol","diamantes"]
        cartas = [1,2,3,4,5,6,7,8,9,10,"j","q","k"]
        dicc_card = {1:"║  1  ║",2:"║  2  ║",3:"║  3  ║",4:"║  4  ║",5:"║  5  ║",6:"║  6  ║",7:"║  7  ║",8:"║  8  ║",9:"║  9  ║",10:"║  10 ║",11:"║  J  ║",12:"║  Q  ║",13:"║  k  ║"}
        dicc_palo = {"corazones":"║♥    ║","picas":"║♠    ║","trebol":"║♣    ║","diamantes":"║♦    ║"}
        dicc_palo2 = {"corazones":"║    ♥║","picas":"║    ♠║","trebol":"║    ♣║","diamantes":"║    ♦║"}
        
        #-- Generador de cartas aleatorias
        def generarCarta(a,b,c,d,e):
            carta = random.randrange(1,14) #-------------La primera carta de este posición elegida en modo aleatorio con el modulo random
            Cartas.display(carta)
            Dibujo.switch(a,0,Cartas.cartas_players)
            Dibujo.switch(b,1,Cartas.cartas_players)
            Dibujo.switch(c,2,Cartas.cartas_players)
            Dibujo.switch(d,3,Cartas.cartas_players)
            Dibujo.switch(e,4,Cartas.cartas_players)  
            Cartas.cartas_players = []
            return carta

        #- Funciones para printear las cartas, el dato en entrada es el punto de la carta y como salida los print de las cartas 
        def display(x):
            carta_player = []
            num = random.randrange(0,4)
            carta_player.append(Cartas.baraja[num])
            carta_player.append(x)
            Cartas.cartas_players.append("╔═════╗")
            Cartas.cartas_players.append(Cartas.dicc_palo[carta_player[0]])
            Cartas.cartas_players.append(Cartas.dicc_card[carta_player[1]])
            Cartas.cartas_players.append(Cartas.dicc_palo2[carta_player[0]])
            Cartas.cartas_players.append("╚═════╝")
            return Cartas.cartas_players

    class Dibujo:
        color = fg('sky_blue_3') + attr('bold')
        color_2 = bg('dark_green')
        color_3 =  fg('dark_orange') + attr('bold')
        Reset = attr('reset')
        lista_direccion = ["  ","  "]
        elementMesa = ["","","","","","","","","","","","","","","","","","","","","","",
                        "","","","","","","","","","","","","","","","","","","","","",""]     
        linea, linea_1, linea_3, linea_4 = " "+color_3+"="*128+Reset , "||"+" "+"*"*124+" "+"||" , "||"+" "*3+"*"+" "*118+"*"+" "*3+"||" , "||"+" "*2+"*"+" "*120+"*"+" "*2+"||"

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
            Dibujo.elementMesa[x] = list[y] 
            return Dibujo.elementMesa

        def intro(x,y):
            print('\n\n\n\t\t\t\t\t\t  ',end="")
            Dibujo.effect("%s%sBIENVENIDO AL JUEGO%s" % (fg('sky_blue_2'), attr('bold'),attr('reset')),x)
            Dibujo.effect('''%s%s                                                                                                                                                               
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
   
        def disegna():
            Dibujo.clear()
            print(Dibujo.color_2+Dibujo.linea+Dibujo.color_2+" ")
            print(Dibujo.color_3+Dibujo.linea_1)
            print(Dibujo.color_3+"||"+" "*2+"*"+Dibujo.elementMesa[32].rjust(53, " ")+"* | JUGADOR | *".ljust(67," ")+"*"+" "*2+"||")
            print(Dibujo.linea_3)
            print(Dibujo.color_3+"||"+" "*2+"*"+" "*82+Dibujo.elementMesa[30].ljust(38," ")+"*"+" "*2+"||")
            print(Dibujo.color_3+"||"+" "+"*"+Dibujo.elementMesa[0].rjust(61, " ")+Dibujo.elementMesa[5].ljust(28, " ")+Dibujo.elementMesa[20].ljust(33, " ")+"*"+" "+"||")
            print(Dibujo.color_3+"||"+" "*2+"*"+Dibujo.elementMesa[1].rjust(60," ")+Dibujo.elementMesa[6].ljust(28," ")+Dibujo.elementMesa[21].ljust(32," ")+"*"+" "*2+"||")
            print(Dibujo.color_3+"||"+" "*3+"*"+Dibujo.elementMesa[2].rjust(59," ")+Dibujo.elementMesa[7].ljust(28," ")+Dibujo.elementMesa[22].ljust(16," ")+Dibujo.elementMesa[42].center(15," ")+"*"+" "*3+"||")
            print(Dibujo.color_3+"||"+" "*2+"*"+Dibujo.elementMesa[3].rjust(60," ")+Dibujo.elementMesa[8].ljust(28," ")+Dibujo.elementMesa[23].ljust(32," ")+"*"+" "*2+"||")
            print(Dibujo.color_3+"||"+" "+"*"+Dibujo.elementMesa[4].rjust(61, " ")+Dibujo.elementMesa[9].ljust(28, " ")+Dibujo.elementMesa[24].ljust(33, " ")+"*"+" "+"||")
            print(Dibujo.linea_4)
            print(Dibujo.color_3+"||"+" "*3+"*"+Dibujo.elementMesa[38].center(118, " ")+"*"+" "*3+"||")
            print(Dibujo.color_3+"||"+" "*2+"*"+Dibujo.elementMesa[35].ljust(120," ")+"*"+" "*2+"||")
            print(Dibujo.color_3+"||"+" "+"*"+Dibujo.elementMesa[40].center(122," ")+"*"+" "+"||")
            print(Dibujo.color_3+"||"+" "*2+"*"+Dibujo.elementMesa[34].ljust(120," ")+"*"+" "*2+"||")
            print(Dibujo.color_3+"||"+" "*3+"* "+">  <<--BACCARAT-->>  <".center(116, "-")+" *"+" "*3+"||")
            print(Dibujo.linea_4)
            print(Dibujo.color_3+"||"+" "+"*"+" "*83+Dibujo.elementMesa[31].ljust(39," ")+"*"+" "+"||")
            print(Dibujo.color_3+"||"+" "*2+"*"+Dibujo.elementMesa[10].rjust(60, " ")+Dibujo.elementMesa[15].ljust(28, " ")+Dibujo.elementMesa[25].ljust(32, " ")+"*"+" "*2+"||")
            print(Dibujo.color_3+"||"+" "*3+"*"+Dibujo.elementMesa[11].rjust(59," ")+Dibujo.elementMesa[16].ljust(28," ")+Dibujo.elementMesa[26].ljust(31," ")+"*"+" "*3+"||")
            print(Dibujo.color_3+"||"+" "*2+"*"+Dibujo.elementMesa[12].rjust(60," ")+Dibujo.elementMesa[17].ljust(28," ")+Dibujo.elementMesa[27].ljust(18," ")+Dibujo.elementMesa[43].ljust(14," ")+"*"+" "*2+"||")
            print(Dibujo.color_3+"||"+" "+"*"+Dibujo.elementMesa[13].rjust(61," ")+Dibujo.elementMesa[18].ljust(28," ")+Dibujo.elementMesa[28].ljust(33," ")+"*"+" "+"||")
            print(Dibujo.color_3+"||"+" "*2+"*"+Dibujo.elementMesa[14].rjust(60, " ")+Dibujo.elementMesa[19].ljust(28, " ")+Dibujo.elementMesa[29].ljust(32, " ")+"*"+" "*2+"||")
            print(Dibujo.linea_3)
            print(Dibujo.color_3+"||"+" "*2+"*"+Dibujo.elementMesa[39].center(120, " ")+"*"+" "*2+"||")
            print(Dibujo.color_3+"||"+" "+"*"+Dibujo.elementMesa[36].ljust(122," ")+"*"+" "+"||")
            print(Dibujo.color_3+"||"+" "*2+"*"+Dibujo.elementMesa[41].center(120," ")+"*"+" "*2+"||")
            print(Dibujo.color_3+"||"+" "*3+"*"+Dibujo.elementMesa[37].ljust(118," ")+"*"+" "*3+"||")
            print(Dibujo.color_3+"||"+" "*2+"*"+(Dibujo.elementMesa[33].rjust(54, " "))+"* | BANCO | *".ljust(66," ")+"*"+" "*2+"||")
            print(Dibujo.linea_1)
            print(Dibujo.linea+Dibujo.color_2+" "+Dibujo.Reset+"\n")
        
        def listasBasias():
            Dibujo.elementMesa = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
            Dibujo.cartas_players = []
            Dibujo.lista_direccion = ["  ","  "]
            jugador.posicion = ""

    def turnos():
        if jugador.posicion == "jugador":
            print('\n\t\t\t\t\t\t\t   ',end="")
            Dibujo.effect("%s%sTurno Jugador%s" % (fg('red_3a'), attr('bold'), attr('reset')), .1)
            jugador.puntoTotales = jugador.puntos(0,1,2,3,4,5,6,7,8,9,38,40,30,20,21,22,23,24,True)
            print('\n\t\t\t\t\t\t\t    ',end="")
            Dibujo.effect("%s%sTurno Banco%s" % (fg('red_3a'), attr('bold'), attr('reset')), .1)
            computer.puntoTotales = computer.puntos(10,11,12,13,14,15,16,17,18,19,39,41,31,25,26,27,28,29,False)
        else:
            print('\n\t\t\t\t\t\t\t    ',end="")
            Dibujo.effect("%s%sTurno Banco%s" % (fg('red_3a'), attr('bold'), attr('reset')), .1)
            jugador.puntoTotales = jugador.puntos(10,11,12,13,14,15,16,17,18,19,39,41,31,25,26,27,28,29,True)
            print('\n\t\t\t\t\t\t\t   ',end="")
            Dibujo.effect("%s%sTurno Jugador%s" % (fg('red_3a'), attr('bold'), attr('reset')), .1)
            computer.puntoTotales = computer.puntos(0,1,2,3,4,5,6,7,8,9,38,40,30,20,21,22,23,24,False)
        jugador.resultado()
        print("\n\n\t\t\t\t\t\t\t    %s%sPress Enter%s" % (fg('sky_blue_2'), attr('bold'),attr('reset')))
        

    #---- Intro
    nombre = input("\n\t\t\t\t\t%s%s        Introduzca su nombre: %s" % (fg('sky_blue_2'), attr('bold'),attr('reset'))).title()
    Dibujo.clear()
    Dibujo.intro(0.01,.0001)
    jugador = Player(0,nombre,fichas)
    computer = Player(0,"Computer")
    
    #---- programa
    while play:
        jugador.acciones()
        if jugador.fichas == 0 or jugador.fichas >= 5000:
            if jugador.fichas >= 5000:
                Dibujo.clear()
                print('\n\t\t\t\t\t\t',end="")
                Dibujo.effect("Has ganado el maximo importe establecido!!",.1)
                print('\n\t\t\t\t\t\t  ',end="")
                Dibujo.effect("Adios "+nombre+"! Vuelva pronto!",.1)
                print('\n\n\n\n\n\n\n\n\n\n\n\n')
                play = False
            else:
                Dibujo.clear()
                print('\n\t\t\t\t\t\t',end="")
                Dibujo.effect("Has perdido todas la fichas",.1)
                print('\n\t\t\t\t\t\t  ',end="")
                Dibujo.effect("Adios "+nombre+"! Vuelva pronto!",.1)
                print('\n\n\n\n\n\n\n\n\n\n\n\n')        
                play = False
        else:
            pass
    
baccarat(500)