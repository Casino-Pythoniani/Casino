import random, sys   ,time, os
from os import system, name

fichas = 100
play = True
empate = False
cartas_players = []
baraja = ["corazones","picas","trebol","diamantes"]
cartas = [1,2,3,4,5,6,7,8,9,10,"j","q","k"]
dicc_card = {1:"║  1  ║",2:"║  2  ║",3:"║  3  ║",4:"║  4  ║",5:"║  5  ║",6:"║  6  ║",7:"║  7  ║",8:"║  8  ║",9:"║  9  ║",10:"║  10 ║",11:"║  J  ║",12:"║  Q  ║",13:"║  k  ║"}
dicc_palo = {"corazones":"║♥    ║","picas":"║♠    ║","trebol":"║♣    ║","diamantes":"║♦    ║"}
dicc_palo2 = {"corazones":"║    ♥║","picas":"║    ♠║","trebol":"║    ♣║","diamantes":"║    ♦║"}
elementMesa = ["","","","","","","","","","","","","","","","","","","","","","",
                "","","","","","","","","","","","","","","","","","","","","",""]

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def effect(prompt,x):
  for char in prompt:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(x)

def validacion(prompt,min,max):
  go = True
  while go:
      try:
          x = int(input(prompt))
          assert x >= min and x <= max #----Este condicional verifica si las apuesta en mayor del fichas total o mayor de 0, en el caso que no lo sea vuelve a preguntar la apuesta dando un mensaje de apuesta incorecta   
      except ValueError:
          print("\nNo has puesto un numero, vuelve a intentarlo!")
      except:
          print("\nOpción non valida, vuelve a intentarla!") 
      else:
          go = False
          return x
          
def reset(x): #Esta funciones sirve para restableser los singolo punto correcto de las cartas, como de reglas pasados los 9 puntos vuelve a cero, el dato de entrada es el punto y el dato de salida es el punto reseteado segundo reglas.
  if x > 9:
      x = 0
  else:
      pass
  return x

def reset_2(x): #Esta funciones sirve para restableser la suma de los puntos totales de las cartas, como de reglas pasados los 9 puntos vuelve a cero, el dato de entrada son los puntos totales (la suma de los puntos de cada singola carta obtenida) y el dato de salida son los puntos totales reseteados segundo reglas.
  if x > 9:
      x = x - 10
  else:
      pass
  return x

def switch(x,y,list):
  elementMesa[x] = list[y] 
  return elementMesa

def Display(x): #------------------Funciones para printear las cartas, el dato en entrada es el punto de la carta y con una elección random de las barajas tiene como salida los print de las cartas 
  global cartas_players
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

def disegna():
  clear()
  print("\n\n "+"="*128)
  print("||"+" "+"*"*124+" "+"||")
  print("||"+" "*2+"*"+elementMesa[32].rjust(53, " ")+"* | JUGADOR | *".ljust(67," ")+"*"+" "*2+"||")
  print("||"+" "*3+"*"+" "*118+"*"+" "*3+"||")
  print("||"+" "*2+"*"+" "*82+elementMesa[30].ljust(38," ")+"*"+" "*2+"||")
  print("||"+" "+"*"+elementMesa[0].rjust(61, " ")+elementMesa[5].ljust(28, " ")+elementMesa[20].ljust(33, " ")+"*"+" "+"||")
  print("||"+" "*2+"*"+elementMesa[1].rjust(60," ")+elementMesa[6].ljust(28," ")+elementMesa[21].ljust(32," ")+"*"+" "*2+"||")
  print("||"+" "*3+"*"+elementMesa[2].rjust(59," ")+elementMesa[7].ljust(28," ")+elementMesa[22].ljust(16," ")+elementMesa[42].center(15," ")+"*"+" "*3+"||")
  print("||"+" "*2+"*"+elementMesa[3].rjust(60," ")+elementMesa[8].ljust(28," ")+elementMesa[23].ljust(32," ")+"*"+" "*2+"||")
  print("||"+" "+"*"+elementMesa[4].rjust(61, " ")+elementMesa[9].ljust(28, " ")+elementMesa[24].ljust(33, " ")+"*"+" "+"||")
  print("||"+" "*2+"*"+" "*120+"*"+" "*2+"||")
  print("||"+" "*3+"*"+elementMesa[38].center(118, " ")+"*"+" "*3+"||")
  print("||"+" "*2+"*"+elementMesa[35].ljust(120," ")+"*"+" "*2+"||")
  print("||"+" "+"*"+elementMesa[40].center(122," ")+"*"+" "+"||")
  print("||"+" "*2+"*"+elementMesa[34].ljust(120," ")+"*"+" "*2+"||")
  print("||"+" "*3+"* "+">  <<--BACCARAT-->>  <".center(116, "-")+" *"+" "*3+"||")
  print("||"+" "*2+"*"+" "*120+"*"+" "*2+"||")
  print("||"+" "+"*"+" "*83+elementMesa[31].ljust(39," ")+"*"+" "+"||")
  print("||"+" "*2+"*"+elementMesa[10].rjust(60, " ")+elementMesa[15].ljust(28, " ")+elementMesa[25].ljust(32, " ")+"*"+" "*2+"||")
  print("||"+" "*3+"*"+elementMesa[11].rjust(59," ")+elementMesa[16].ljust(28," ")+elementMesa[26].ljust(31," ")+"*"+" "*3+"||")
  print("||"+" "*2+"*"+elementMesa[12].rjust(60," ")+elementMesa[17].ljust(28," ")+elementMesa[27].ljust(18," ")+elementMesa[43].ljust(14," ")+"*"+" "*2+"||")
  print("||"+" "+"*"+elementMesa[13].rjust(61," ")+elementMesa[18].ljust(28," ")+elementMesa[28].ljust(33," ")+"*"+" "+"||")
  print("||"+" "*2+"*"+elementMesa[14].rjust(60, " ")+elementMesa[19].ljust(28, " ")+elementMesa[29].ljust(32, " ")+"*"+" "*2+"||")
  print("||"+" "*3+"*"+" "*118+"*"+" "*3+"||")
  print("||"+" "*2+"*"+elementMesa[39].center(120, " ")+"*"+" "*2+"||")
  print("||"+" "+"*"+elementMesa[36].ljust(122," ")+"*"+" "+"||")
  print("||"+" "*2+"*"+elementMesa[41].center(120," ")+"*"+" "*2+"||")
  print("||"+" "*3+"*"+elementMesa[37].ljust(118," ")+"*"+" "*3+"||")
  print("||"+" "*2+"*"+(elementMesa[33].rjust(54, " "))+"* | BANCO | *".ljust(66," ")+"*"+" "*2+"||")
  print("||"+" "+"*"*124+" "+"||")
  print(" "+"="*128+"\n\n")

def dibujo():
  effect('''                                                                                                                                                             
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
      BBBBBBBBBBBBBB      aaaaaaaa aa   ccccccc        ccccccc     aaaaaaa  aa rrrrrr        aaaaaaaa  aa         ttttttt                                                                                                                                           
                                                                                                                          ''',.001)

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

def turnoJugador():
  carta_1 = carta(0,1,2,3,4)
  carta_2 = carta(5,6,7,8,9)
  time.sleep(3)
  disegna()
  elementMesa[38] = "Puntos: "+str(reset(carta_1))+" "+str(reset(carta_2))
  time.sleep(1.5)
  disegna()
  puntosJugador = reset(carta_1) + reset(carta_2)
  puntosJugador = reset_2(puntosJugador)
  elementMesa[40] = "Puntos totales: "+str(puntosJugador)
  time.sleep(1.5)
  disegna()
  if eleccion == 1 and reset_2(puntosJugador) <= 7: #-Si el usuario es en posición "jugador" y tiene meno de 8 puntos puede elegir una tercera carta.
    time.sleep(1.5) #---------------------------Pausa temporal del modulo TIME para crear "Suspens".
    tercera_jugador = validacion("\nSi quieres una otra carta imprima 1 sino 0: ",0,1)
    if tercera_jugador == 1: #------------------------Si el usuario elige una tercera carta.
      elementMesa[30] = "<*| Carta bonus |*>"
      carta_3 = carta(20,21,22,23,24)    
      elementMesa[38] = "Puntos: "+str(reset(carta_1))+" "+str(reset(carta_2))+" "+str(reset(carta_3))
      puntosJugador = puntosJugador + reset(carta_3)
      puntosJugador = reset_2(puntosJugador) #-Puntos total del jugador
      elementMesa[40] = "Puntos totales: "+str(puntosJugador)
      disegna()
    else:
        pass
  else:
    if reset_2(puntosJugador) <= 4 and reset_2(puntosJugador) < reset_2(puntosBanco):
      # and reset_2(puntosBanco) > reset_2(puntosJugador):
      elementMesa[30] = "<*| Carta bonus |*>"
      carta_3 = carta(20,21,22,23,24)  
      elementMesa[38] = "Puntos: "+str(reset(carta_1))+" "+str(reset(carta_2))+" "+str(reset(carta_3))
      puntosJugador = puntosJugador + reset(carta_3)
      puntosJugador = reset_2(puntosJugador) #-Puntos total del jugador
      elementMesa[40] = "Puntos totales: "+str(puntosJugador)
  time.sleep(1.5)
  disegna()
  time.sleep(1.5)
  time.sleep(5)
  return puntosJugador

def turnoBanco():
  carta_4 = carta(10,11,12,13,14)
  carta_5 = carta(15,16,17,18,19)
  time.sleep(1.5)
  disegna()
  elementMesa[39] = "Puntos: "+str(reset(carta_4))+" "+str(reset(carta_5))
  time.sleep(1.5)
  disegna()
  puntosBanco = reset(carta_4) + reset(carta_5)
  puntosBanco = reset_2(puntosBanco)
  elementMesa[41] = "Puntos totales: "+str(puntosBanco)
  time.sleep(1.5)
  disegna()
  if eleccion == 0 and reset_2(puntosBanco) <= 7: #-Si el usuario es en posición "jugador" y tiene meno de 8 puntos puede elegir una tercera carta.
    time.sleep(1.5) #---------------------------Pausa temporal del modulo TIME para crear "Suspens".
    tercera_jugador = validacion("\nSi quieres una otra carta imprima 1 sino 0: ",0,1)
    if tercera_jugador == 1: #------------------------Si el usuario elige una tercera carta.
      elementMesa[31] = "<*| Carta bonus |*>"
      carta_6 = carta(25,26,27,28,29)
      elementMesa[39] = "Puntos: "+str(reset(carta_4))+" "+str(reset(carta_5))+" "+str(reset(carta_6))
      puntosBanco = puntosBanco + reset(carta_6)
      puntosBanco = reset_2(puntosBanco) #-Puntos total del jugador
      elementMesa[41] = "Puntos totales: "+str(puntosBanco)
      disegna()
    else:
        pass
  else:
    if reset_2(puntosBanco) <= 4 and reset_2(puntosBanco) < reset_2(puntosJugador):
      elementMesa[31] = "<*| Carta bonus |*>"
      carta_6 = carta(25,26,27,28,29)
      elementMesa[39] = "Puntos: "+str(reset(carta_4))+" "+str(reset(carta_5))+" "+str(reset(carta_6))
      puntosBanco = puntosBanco + reset(carta_6)
      puntosBanco = reset_2(puntosBanco) #-Puntos total del jugador
      elementMesa[41] = "Puntos totales: "+str(puntosBanco)
      time.sleep(1.5)
      disegna()
    else:
      pass
  return puntosBanco

def resultado(puntosBanco,puntosJugador):
  global fichas
  if reset_2(puntosBanco) == reset_2(puntosJugador): #-Si el juego es empacto
    empate = True
    while empate:
      time.sleep(1.5)#---------------------------Pausa temporal del modulo TIME para crear "Suspens".
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
      
      if eleccion == 1: #------------------------------Si el usuario es en posición "jugador"...
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
      disegna()   
  if reset_2(puntosBanco) > reset_2(puntosJugador): #-Si los puntos del "banco" son mayores de los puntos del "jugador"
    time.sleep (1.5) #-------------------------Pausa temporal del modulo TIME para crear "Suspens".
    elementMesa[43] = "GANADOR!!"
    elementMesa[42] = "Perdedor..."
    if eleccion == 0: #------------------------------Si el usuario es en posición "banco"...
      fichas = fichas + apuesta #------------------Suma de fichas apostado al fichas actual. 
      elementMesa[37] = "     fichas total: "+str(fichas)
      elementMesa[36] = ""
    else: #------------------------------------------Si el usuario es en posición "jugador"...
      fichas = fichas - apuesta #------------------Resta de fichas apostado al fichas actual. 
      elementMesa[34] = "     fichas total: "+str(fichas)
      elementMesa[35] = ""
    time.sleep(1.5)
    disegna()

  if reset_2(puntosBanco) < reset_2(puntosJugador): #-Si los puntos del "banco" son minores de los puntos del "jugador"
    time.sleep (1.5) #-------------------------Pausa temporal del modulo TIME para crear "Suspens".
    elementMesa[43] = "Perdedor..."
    elementMesa[42] = "GANADOR!!"
    if eleccion == 1: #------------------------------Si el usuario es en posición "jugador"...
      fichas = fichas + apuesta #------------------Suma de fichas apostado al fichas actual.
      elementMesa[34] = "     fichas total: "+str(fichas)
      elementMesa[35] = ""
    else: #------------------------------------------Si el usuario es en posición "banco"...
      fichas = fichas - apuesta #------------------Resta de fichas apostado al fichas actual.
      elementMesa[37] = "     fichas total: "+str(fichas)
      elementMesa[36] = ""
  return 


print('\n\t\t\t\t\t\t  ',end="")
effect("BIENVENIDO AL JUEGO",.1)
time.sleep(1.5)
dibujo()
time.sleep(1.5)
disegna()
time.sleep(1.5)
nombre = input("\n\n\t\t\t\t\t\t  Introduzca su nombre: ").capitalize()
  
while play:
  if fichas == 0 or fichas >= 1000:
    if fichas >= 1000:
      print('\n\t\t\t\t\t\t\t',end="")
      effect(nombre+" has ganado!!",.1)
    else:
      print('\n\t\t\t\t\t\t\t',end="")
      effect(nombre+" has perdido...",.1)
    play = False
  else:
    time.sleep(1.5)
    eleccion = validacion("\n\n\t\t\t\t"+nombre+" elige tu posicion (1 por Jugador, 0 por Banco): ",0,1) #-Llama la función del modulo por elegir la posición de juego.
    elementMesa[34],elementMesa[35],elementMesa[36],elementMesa[37] = "","","",""
    if eleccion == 1:
      elementMesa[32] = nombre+" --> "
      elementMesa[33] = "Computer --> "
      elementMesa[34] = "     Fichas total: "+str(fichas)
    else:
      elementMesa[33] = nombre+" --> "
      elementMesa[32] = "Computer --> "
      elementMesa[37] = "     Fichas total: "+str(fichas)
    time.sleep(1.5)
    disegna()
    time.sleep(1.5)
    apuesta = validacion("\n\t\t\t\t\t\t\tFichas a apostar: ",1,fichas) #-Llama la función del modulo por elegir el fichas de apostar. 
    if eleccion == 1:
      elementMesa[35] = ("     Apuesta: "+str(apuesta))
    else:
      elementMesa[36] = ("       Apuesta: "+str(apuesta))
    time.sleep(1.5)
    disegna()
    if eleccion == 1:
      print('\n\t\t\t\t\t\t\t',end="")
      effect("Turno: Jugador",.1)
      puntosJugador =  turnoJugador()
      print('\n\t\t\t\t\t\t\t',end="")
      effect("Turno: Banco",.1)
      puntosBanco = turnoBanco()
    else:
      print('\n\t\t\t\t\t\t\t',end="")
      effect("Turno: Banco",.1)
      puntosBanco = turnoBanco()
      print('\n\t\t\t\t\t\t\t',end="")
      effect("Turno: Jugador",.1)
      puntosJugador =  turnoJugador()
    time.sleep(5) 
    resultado(puntosBanco,puntosJugador)
    time.sleep(1.5)
    disegna()
    time.sleep (1.5) #----------------------------Pausa temporal del modulo  TIME para crear "Suspens".
    parar = validacion("\nImprima '1' para jugar o '0' para parar: ",0,1) #-Llama la función del modulo por elegir si seguir jugando o parar.
    if parar == 0: #-------------------------------------Si el player elige de parar.
      clear()
      print('\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t  ',end="")
      effect("fichas actual "+str(fichas)+"£",.1)
      print('\n\t\t\t\t\t\t  ',end="")
      effect("Adios "+nombre+"! Vuelva pronto!",.1)
      print('\n\n\n\n\n\n\n\n\n\n\n\n')
      play = False
    else:
      elementMesa = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
      cartas_players = []
      disegna()