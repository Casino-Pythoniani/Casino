from Vicente.poker_casino.modulos import random_card
from random import randrange
import os
from pynput.keyboard import Listener
clear = lambda: os.system('cls') 

class Baraja:

    def barajar(self):
        self.americana = []
        self.baraja_americana = random_card(52,self.americana) 
        return self.baraja_americana 
    
    def repartir(self,mano):
        mano.append(self.baraja_americana[0])
        del self.baraja_americana[0]

    def quemar(self):
        del self.baraja_americana[0]

ciegas = [10,20]
a_igualar = ciegas[1]
boton = [['╔','═','╗','╚','╝','║'],['┌','─','┐','└','┘','│'],['┌','─','┐','└','┘','│']]
pos = 0
romper_bucle_eleccion = True
apuesta_min = ciegas[1] 


class Jugador:
    def __init__(self,cpu = True,fichas = 500):
        self.mano = []
        self.fichas = fichas
        self.fichas_apostadas = 0
        self.big = False
        self.small = False
        self.seguir_mano = True
        self.seguir_partida = True
        self.victoria = False
        self.cpu = cpu
        self.decidir = '────────'
        self.salir = False
    
    def decision(self): ##ascii:│ ┼ ─ ┬ ┴ ┘ └ ├ ┤ ┌ ┐  ║ ╔ ═ ╗ ╚ ╝ ╞       
        # pos = 0
        global apuesta_min
        global a_igualar
        def key_recorder(key):
            global pos
            global boton
            global apuesta_min
            global a_igualar
            global romper_bucle_eleccion
           
            key = str(key).replace("'", "")

            if key == 'Key.right' and pos != 2:
                boton[pos],boton[pos+1] = boton[pos+1],boton[pos]
                pos += 1
            
            if key == 'Key.left' and pos != 0:
                boton[pos],boton[pos-1] = boton[pos-1],boton[pos]
                pos -= 1

            if apuesta_min < self.fichas:
                if key == 'Key.up' and pos == 2:
                    apuesta_min += 5
                
            if key == 'Key.down' and pos == 2:
                apuesta_min -= 5
                if apuesta_min <= ciegas[1] + 5:
                    apuesta_min = ciegas[1] + 5
            
            if key == 'Key.enter':
                romper_bucle_eleccion = False

            if key == 'Key.esc':
                romper_bucle_eleccion = False
                pos = 3
            
            l.stop()
        
        def display_eleccion():
            global romper_bucle_eleccion
            global apuesta_min
            global a_igualar
            romper_bucle_eleccion = True
            apuesta_min = ciegas[1] +5
            global l
            print('\n'*5)
            while romper_bucle_eleccion:
                if len(str(apuesta_min)) == 2:
                    espacio = '  '
                if len(str(apuesta_min)) == 3:
                    espacio = ' '
                if len(str(apuesta_min)) == 4:
                    espacio = ''
                
                print(("\033[F") * 6)
                print('\t\t\t\t┌'+('─')*62+'┐')  
                print('\t\t\t\t│ '+boton[0][0]+(boton[0][1])*12+boton[0][2],boton[1][0]+(boton[1][1])*12+boton[1][2],boton[2][0]+(boton[2][1])*12+boton[2][2],'   ┌─────┐ ▲    │')
                print('\t\t\t\t│ '+boton[0][5]+'    IRSE    '+boton[0][5],boton[1][5]+'  IGUALAR   '+boton[1][5],boton[2][5]+'   SUBIR    '+boton[2][5]+'    │',str(apuesta_min)+espacio+'│      │')
                print('\t\t\t\t│ '+boton[0][3]+(boton[0][1])*12+boton[0][4],boton[1][3]+(boton[1][1])*12+boton[1][4],boton[2][3]+(boton[2][1])*12+boton[2][4],'   └─────┘ ▼    │')
                print('\t\t\t\t└'+('─')*62+'┘') 
                with Listener(on_press=key_recorder) as l:
                    l.join()
            clear()

        def return_decision():
            global pos
            if pos == 0:
                return 1

            elif pos == 1:
                return 2

            elif pos == 2:
                return 3

            elif pos == 3:
                pos = 0
                return 0

        if self.cpu == False:
            if self.fichas_apostadas > a_igualar:
                a_igualar = self.fichas_apostadas

            display_eleccion()
            decidir = return_decision()

            if decidir == 0:
                self.salir = True

            elif decidir == 1:
                self.decidir = '──Irse──'
                self.seguir_mano = False

            elif decidir == 2:
                self.decidir = 'Igualar─'
                self.fichas = self.fichas - (a_igualar - self.fichas_apostadas)
                self.fichas_apostadas = a_igualar

            elif decidir == 3:
                self.decidir = '─Subir──'
                self.fichas += self.fichas_apostadas
                self.fichas_apostadas += apuesta_min
                self.fichas -= self.fichas_apostadas
                a_igualar = self.fichas_apostadas

        else:
            r = randrange(1,15)
            if r == 1:
                self.decidir = '──Irse──'
                self.seguir_mano = False

            else:
                self.decidir = 'Igualar─'
                self.fichas = self.fichas - (a_igualar - self.fichas_apostadas)
                self.fichas_apostadas = a_igualar
                
contador_blind = 0

def resetear_turno(blind):
    global ciegas
    global contador_blind
    global a_igualar
    a_igualar = ciegas[1]
    lista = []
    contador_blind += 1
    for i in blind:
        i.big = False
        i.small = False
        i.seguir_mano = True
        i.mano.clear()
        i.victoria = False

    for i in blind:
        if i.seguir_partida == True:
            lista.append(i)

    if contador_blind == len(lista):
        ciegas = [ciegas[0]*2,ciegas[1]*2]
        a_igualar = ciegas[1]
        contador_blind = 0

    blind.clear()
    blind.append(lista[-1])
    del lista [-1]  
    lista.insert(0,blind[0])
    lista[0].big = True
    lista[0].fichas_apostadas = ciegas[1]
    lista[0].fichas = lista[0].fichas - ciegas[1]
    lista[1].small = True   
    lista[1].fichas_apostadas = ciegas[0]
    lista[1].fichas = lista[1].fichas - ciegas[0]
    return lista

def resetear_apuestas():
    global a_igualar
    a_igualar = 0

def limpiar_elementos(lista):
    for i in lista:
        i.decidir = '────────'
    return lista

def valores(lista,mesa):
    todos_valores = []

    for i in range(len(lista)):
        comprobar = []
        comprobar.extend(lista[i].mano)
        comprobar.extend(mesa)

        numeros = [comprobar[0][1],comprobar[1][1],comprobar[2][1],comprobar[3][1],comprobar[4][1],comprobar[5][1],comprobar[6][1]]
        palos = [comprobar[0][0],comprobar[1][0],comprobar[2][0],comprobar[3][0],comprobar[4][0],comprobar[5][0],comprobar[6][0]]

        palos.sort()
        numeros.sort(reverse=True)

        #ESCALERA DE COLOR
        def escalera_color(palos,numeros):
            for x in palos:
                if palos.count(x) >= 5:
                    if numeros[0] == numeros[1] + 1:
                        if numeros[0] == numeros[2] + 2:
                            if numeros[0] == numeros[3] + 3:
                                if numeros[0] == numeros[4] + 4:
                                    return [True,'escalera_color',sum(numeros)]
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                
                    if numeros[1] == numeros[2] + 1:
                        if numeros[1] == numeros[3] + 2:
                            if numeros[1] == numeros[4] + 3:
                                if numeros[1] == numeros[5] + 4:
                                    return [True,'escalera_color',sum(numeros)]
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass

                    if numeros[2] == numeros[3] + 1:
                        if numeros[2] == numeros[4] + 2:
                            if numeros[2] == numeros[5] + 3:
                                if numeros[2] == numeros[6] + 4:
                                    return [True,'escalera_color',sum(numeros)]
                                else:
                                    return [False]
                            else:
                                return [False]
                        else:
                            return [False]
                    else:
                        return [False]
                else:
                    return[False]
        
        if escalera_color(palos,numeros)[0] == True:
            anyadir = [escalera_color(palos,numeros)[1],escalera_color(palos,numeros)[2]]
            todos_valores.append(anyadir)
            continue
        
        #POKER
        def poker(numeros):
            for x in numeros:
                if numeros.count(x) == 4:
                    return [True,'poker',sum(numeros)]    
            return [False]
        
        if poker(numeros)[0] == True:
            anyadir = [poker(numeros)[1],poker(numeros)[2]]
            todos_valores.append(anyadir)
            continue
        
        #FULL HOUSE
        def full_house(numeros):
            full = []
            for x in numeros:
                if numeros.count(x) == 3:
                    full.append(x)

                if numeros.count(x) == 2:
                    full.append(x)

            if len(full) == 5:
                return [True,'full',sum(full)]

            return [False]
        
        if full_house(numeros)[0] == True:
            anyadir = [full_house(numeros)[1],full_house(numeros)[2]]
            todos_valores.append(anyadir)
            continue
        
        #COLOR
        def color(palos,numeros):
            for x in palos:
                if palos.count(x) >= 5:
                    return [True,'color',sum(numeros)]
            return [False]
        
        if color(palos,numeros)[0] == True:
            anyadir = [color(palos,numeros)[1],color(palos,numeros)[2]]
            todos_valores.append(anyadir)
            continue
        
        #ESCALERA    
        def escalera(numeros):
            if numeros[0] == numeros[1] + 1:
                if numeros[0] == numeros[2] + 2:
                    if numeros[0] == numeros[3] + 3:
                        if numeros[0] == numeros[4] + 4:
                            return [True,'escalera',sum(numeros)]
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        
            if numeros[1] == numeros[2] + 1:
                if numeros[1] == numeros[3] + 2:
                    if numeros[1] == numeros[4] + 3:
                        if numeros[1] == numeros[5] + 4:
                            return [True,'escalera',sum(numeros)]
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass

            if numeros[2] == numeros[3] + 1:
                if numeros[2] == numeros[4] + 2:
                    if numeros[2] == numeros[5] + 3:
                        if numeros[2] == numeros[6] + 4:
                            return [True,'escalera',sum(numeros)]
                        else:
                            return [False]
                    else:
                        return [False]
                else:
                    return [False]
            else:
                return [False]
        
        if escalera(numeros)[0] == True:
            anyadir = [escalera(numeros)[1],escalera(numeros)[2]]
            todos_valores.append(anyadir)
            continue
            
        #TRIO
        def trio(numeros):
            for x in numeros:
                if numeros.count(x) == 3:
                    return [True,'trio',sum(numeros)]
            return [False]
        
        if trio(numeros)[0] == True:
            anyadir = [trio(numeros)[1],trio(numeros)[2]]
            todos_valores.append(anyadir)
            continue

        #DOBLE PAREJA
        def doble_pareja(numeros):
            doblepareja = []
            for i in numeros:
                if (numeros.count(i) == 2):
                    doblepareja.append(i)
                if len(doblepareja) == 4:
                    return [True,'doble_pareja',sum(doblepareja)]
            return [False]
        
        if doble_pareja(numeros)[0] == True:
            anyadir = [doble_pareja(numeros)[1],doble_pareja(numeros)[2]]
            todos_valores.append(anyadir)
            continue
            
        #PAREJA
        def pareja(numeros):
            pareja_lista = []
            for x in numeros:
                if numeros.count(x) == 2:
                    pareja_lista.append(x)

                if len(pareja_lista) == 2:
                    return [True,'pareja',sum(pareja_lista)]
            return [False]

        if pareja(numeros)[0] == True:
            anyadir = [pareja(numeros)[1],pareja(numeros)[2]] 
            todos_valores.append(anyadir)
            continue
        
        #CARTA ALTA
        def carta_alta(numeros):
            return ['carta_alta',max(numeros)]
        
        todos_valores.append(carta_alta(numeros))

    validar = []
    diccionario = {'escalera_color':9,'poker':8,'full':7,'color':6,'escalera':5,'trio':4,
                   'doble_pareja':3,'pareja':2,'carta_alta':1}

    for i in todos_valores:
        validar.append(diccionario[i[0]])
    
    for i in range(len(lista)):
        if lista[i].seguir_mano == True:
            todos_valores[i][0] = diccionario[todos_valores[i][0]]
        else:
            todos_valores[i][0] = False

    valor_alto = 0
    for i in validar:
        if i > valor_alto:
            valor_alto = i
    
    for i in todos_valores:
        if i[0] < valor_alto:
            i[0] = False
        
    comprobar_valores = 0
    for i in todos_valores:
        if i[0] != False:
            comprobar_valores += 1
    
    for i in todos_valores:
        if i[0] != False and comprobar_valores == 1:
            i[0] = True
    
    for i in range(len(lista)):
        if todos_valores[i][0] == True:
            lista[i].victoria = True
            return lista
    
    if comprobar_valores > 1:
        for i in todos_valores:
            if i[0] != False:
                i[0] = True

    comprobar_valores = 0
    for i in todos_valores:
        if i[0] == True:
            if i[1] > comprobar_valores:
                comprobar_valores = i[1]
    
    for i in todos_valores:
        if i[1] == comprobar_valores:
            i[1] = True

    for i in range(len(lista)):
        if todos_valores[i][0] == True and todos_valores[i][1] == True:
            lista[i].victoria = True
    return lista

def display_tablero_poker(jugador,cpu1,cpu2,cpu3,cpu4,cpu5,mesa,bote):
    
    carta_boca_abajo = ['╔═════╗','║?¿?¿?║','║?¿?¿?║','║¿?¿?¿║','╚═════╝']
    carta_vacia = ['       ','       ','       ','       ','       ']     

    palos = {'diamantes':['║♦    ║','║    ♦║'],
             'corazones':['║♥    ║','║    ♥║'],
                'trebol':['║♣    ║','║    ♣║'],
                 'picas':['║♠    ║','║    ♠║']}
    numeros = {1:'║  2  ║',
               2:'║  3  ║',
               3:'║  4  ║',
               4:'║  5  ║',
               5:'║  6  ║',
               6:'║  7  ║',
               7:'║  8  ║',
               8:'║  9  ║',
               9:'║  10 ║',
              10:'║  J  ║',
              11:'║  Q  ║',
              12:'║  K  ║',
              13:'║  A  ║'}

    if jugador.seguir_mano == False:
        carta_1_jugador = carta_vacia
        carta_2_jugador = carta_vacia
    else:
        carta_1_jugador = ['╔═════╗',palos[jugador.mano[0][0]][0],numeros[jugador.mano[0][1]],palos[jugador.mano[0][0]][1],'╚═════╝']
        carta_2_jugador = ['╔═════╗',palos[jugador.mano[1][0]][0],numeros[jugador.mano[1][1]],palos[jugador.mano[1][0]][1],'╚═════╝']
        
    carta_1_mesa = carta_vacia
    carta_2_mesa = carta_vacia
    carta_3_mesa = carta_vacia
    carta_4_mesa = carta_vacia
    carta_5_mesa = carta_vacia
    
    if len(mesa) == 3:
        carta_1_mesa = ['╔═════╗',palos[mesa[0][0]][0],numeros[mesa[0][1]],palos[mesa[0][0]][1],'╚═════╝']
        carta_2_mesa = ['╔═════╗',palos[mesa[1][0]][0],numeros[mesa[1][1]],palos[mesa[1][0]][1],'╚═════╝']
        carta_3_mesa = ['╔═════╗',palos[mesa[2][0]][0],numeros[mesa[2][1]],palos[mesa[2][0]][1],'╚═════╝']

    if len(mesa) == 4:
        carta_1_mesa = ['╔═════╗',palos[mesa[0][0]][0],numeros[mesa[0][1]],palos[mesa[0][0]][1],'╚═════╝']
        carta_2_mesa = ['╔═════╗',palos[mesa[1][0]][0],numeros[mesa[1][1]],palos[mesa[1][0]][1],'╚═════╝']
        carta_3_mesa = ['╔═════╗',palos[mesa[2][0]][0],numeros[mesa[2][1]],palos[mesa[2][0]][1],'╚═════╝']
        carta_4_mesa = ['╔═════╗',palos[mesa[3][0]][0],numeros[mesa[3][1]],palos[mesa[3][0]][1],'╚═════╝']
    
    if len(mesa) == 5:
        carta_1_mesa = ['╔═════╗',palos[mesa[0][0]][0],numeros[mesa[0][1]],palos[mesa[0][0]][1],'╚═════╝']
        carta_2_mesa = ['╔═════╗',palos[mesa[1][0]][0],numeros[mesa[1][1]],palos[mesa[1][0]][1],'╚═════╝']
        carta_3_mesa = ['╔═════╗',palos[mesa[2][0]][0],numeros[mesa[2][1]],palos[mesa[2][0]][1],'╚═════╝']
        carta_4_mesa = ['╔═════╗',palos[mesa[3][0]][0],numeros[mesa[3][1]],palos[mesa[3][0]][1],'╚═════╝']
        carta_5_mesa = ['╔═════╗',palos[mesa[4][0]][0],numeros[mesa[4][1]],palos[mesa[4][0]][1],'╚═════╝']
    
    
    #CPU1
    carta_1_cpu1,carta_2_cpu1 = carta_boca_abajo,carta_boca_abajo
        
    if cpu1.seguir_mano == False or cpu1.seguir_partida == False:
        carta_1_cpu1,carta_2_cpu1 = carta_vacia,carta_vacia

    #CPU2
    carta_1_cpu2,carta_2_cpu2 = carta_boca_abajo,carta_boca_abajo

    if cpu2.seguir_mano == False or cpu2.seguir_partida == False:
        carta_1_cpu2,carta_2_cpu2 = carta_vacia,carta_vacia

    #CPU3
    carta_1_cpu3,carta_2_cpu3 = carta_boca_abajo,carta_boca_abajo

    if cpu3.seguir_mano == False or cpu3.seguir_partida == False:
        carta_1_cpu3,carta_2_cpu3 = carta_vacia,carta_vacia

    #CPU4
    carta_1_cpu4,carta_2_cpu4 = carta_boca_abajo,carta_boca_abajo

    if cpu4.seguir_mano == False or cpu4.seguir_partida == False:
        carta_1_cpu4,carta_2_cpu4 = carta_vacia,carta_vacia

    #CPU5
    carta_1_cpu5,carta_2_cpu5 = carta_boca_abajo,carta_boca_abajo

    if cpu5.seguir_mano == False or cpu5.seguir_partida == False:
        carta_1_cpu5,carta_2_cpu5 = carta_vacia,carta_vacia

    if jugador.big == True:
        big_small_6 = '│BB│'
    elif jugador.small == True:
        big_small_6 = '│SB│'
    else:
        big_small_6 = '    '

    if cpu5.big == True:
        big_small_5 = '│BB│'
    elif cpu5.small == True:
        big_small_5 = '│SB│'
    else:
        big_small_5 = '    '

    if cpu4.big == True:
        big_small_4 = '│BB│'
    elif cpu4.small == True:
        big_small_4 = '│SB│'
    else:
        big_small_4 = '    '

    if cpu3.big == True:
        big_small_3 = '│BB│'
    elif cpu3.small == True:
        big_small_3 = '│SB│'
    else:
        big_small_3 = '    '
    
    if cpu2.big == True:
        big_small_2 = '│BB│'
    elif cpu2.small == True:
        big_small_2 = '│SB│'
    else:
        big_small_2 = '    '
    
    if cpu1.big == True:
        big_small_1 = '│BB│'
    elif cpu1.small == True:
        big_small_1 = '│SB│'
    else:
        big_small_1 = '    '

    fichas_1 = (6-len(str(cpu1.fichas)))*'─'
    fichas_2 = (6-len(str(cpu2.fichas)))*'─'
    fichas_3 = (6-len(str(cpu3.fichas)))*'─'
    fichas_4 = (6-len(str(cpu4.fichas)))*'─'
    fichas_5 = (6-len(str(cpu5.fichas)))*'─'
    fichas_6 = (6-len(str(jugador.fichas)))*'─'

    apuesta_1 = (6-len(str(cpu1.fichas_apostadas)))*' '
    apuesta_2 = (6-len(str(cpu2.fichas_apostadas)))*' '
    apuesta_3 = (6-len(str(cpu3.fichas_apostadas)))*' '
    apuesta_4 = (6-len(str(cpu4.fichas_apostadas)))*' '
    apuesta_5 = (6-len(str(cpu5.fichas_apostadas)))*' '
    apuesta_6 = (6-len(str(jugador.fichas_apostadas)))*' '

    m_apuesta_1 = str(cpu1.fichas_apostadas)
    m_apuesta_2 = str(cpu2.fichas_apostadas)
    m_apuesta_3 = str(cpu3.fichas_apostadas)
    m_apuesta_4 = str(cpu4.fichas_apostadas)
    m_apuesta_5 = str(cpu5.fichas_apostadas)
    m_apuesta_6 = str(jugador.fichas_apostadas)

    if cpu1.fichas_apostadas == 0:
        m_apuesta_1 = ' '
    if cpu2.fichas_apostadas == 0:
        m_apuesta_2 = ' '
    if cpu3.fichas_apostadas == 0:
        m_apuesta_3 = ' '
    if cpu4.fichas_apostadas == 0:
        m_apuesta_4 = ' '
    if cpu5.fichas_apostadas == 0:
        m_apuesta_5 = ' '
    if jugador.fichas_apostadas == 0:
        m_apuesta_6 = ' '
    
    if cpu1.victoria == True:
        carta_1_cpu1 = ['╔═════╗',palos[cpu1.mano[0][0]][0],numeros[cpu1.mano[0][1]],palos[cpu1.mano[0][0]][1],'╚═════╝']
        carta_2_cpu1 = ['╔═════╗',palos[cpu1.mano[1][0]][0],numeros[cpu1.mano[1][1]],palos[cpu1.mano[1][0]][1],'╚═════╝']
    
    if cpu2.victoria == True:
        carta_1_cpu2 = ['╔═════╗',palos[cpu2.mano[0][0]][0],numeros[cpu2.mano[0][1]],palos[cpu2.mano[0][0]][1],'╚═════╝']
        carta_2_cpu2 = ['╔═════╗',palos[cpu2.mano[1][0]][0],numeros[cpu2.mano[1][1]],palos[cpu2.mano[1][0]][1],'╚═════╝']
    
    if cpu3.victoria == True:
        carta_1_cpu3 = ['╔═════╗',palos[cpu3.mano[0][0]][0],numeros[cpu3.mano[0][1]],palos[cpu3.mano[0][0]][1],'╚═════╝']
        carta_2_cpu3 = ['╔═════╗',palos[cpu3.mano[1][0]][0],numeros[cpu3.mano[1][1]],palos[cpu3.mano[1][0]][1],'╚═════╝']
    
    if cpu4.victoria == True:
        carta_1_cpu4 = ['╔═════╗',palos[cpu4.mano[0][0]][0],numeros[cpu4.mano[0][1]],palos[cpu4.mano[0][0]][1],'╚═════╝']
        carta_2_cpu4 = ['╔═════╗',palos[cpu4.mano[1][0]][0],numeros[cpu4.mano[1][1]],palos[cpu4.mano[1][0]][1],'╚═════╝']
    
    if cpu5.victoria == True:
        carta_1_cpu5 = ['╔═════╗',palos[cpu5.mano[0][0]][0],numeros[cpu5.mano[0][1]],palos[cpu5.mano[0][0]][1],'╚═════╝']
        carta_2_cpu5 = ['╔═════╗',palos[cpu5.mano[1][0]][0],numeros[cpu5.mano[1][1]],palos[cpu5.mano[1][0]][1],'╚═════╝']
    
    print('╔══════════════╗'+' '*7+'┌'+'──'+str(cpu4.fichas)+fichas_4+'┐'+' '*22+'┌'+'──'+str(cpu3.fichas)+fichas_3+'┐'+' '*22+'┌'+'──'+str(cpu2.fichas)+fichas_2+'┐          BIG:',ciegas[1])
    print('║ SALIR  (ESC) ║'+' '*7+'│'+('   ▄▄   ')+'│'+' '*22+'│'+('   ▄▄   ')+'│'+' '*22+'│'+('   ▄▄   ')+'│        SMALL:',ciegas[0])
    print('╚══════════════╝'+' '*7+'│'+('   ▀▀   ')+'│'+' '*22+'│'+('   ▀▀   ')+'│'+' '*22+'│'+('   ▀▀   ')+'│')
    print('┌'+'─'*22+'┤'+('  ████  ')+'├'+'─'*22+'┤'+('  ████  ')+'├'+'─'*22+'┤'+('  ████  ')+'├'+'─'*22+'┐')
    print('│'+' '*22+'└'+cpu4.decidir+'┘'+' '*22+'└'+cpu3.decidir+'┘'+' '*22+'└'+cpu2.decidir+'┘'+' '*22+'│')
    for i in range(5):
        print('│'+' '*19+carta_1_cpu4[i]+'  '+carta_2_cpu4[i]+' '*16+carta_1_cpu3[i]+'  '+carta_2_cpu3[i]+' '*16+carta_1_cpu2[i]+'  '+carta_2_cpu2[i]+' '*19+'│')
    print('│'+' '*25+big_small_4+' '*28+big_small_3+' '*28+big_small_2+' '*25+'│')
    print('│'+(' '*118)+'│')
    print('│'+' '*25+m_apuesta_4+apuesta_4+' '*26+m_apuesta_3+apuesta_3+' '*26+m_apuesta_2+apuesta_2+' '*23+'│')
    for i in range(5): 
        print('│'+' '*38+carta_1_mesa[i]+'  '+carta_2_mesa[i]+'  '+carta_3_mesa[i]+'  '+carta_4_mesa[i]+'  '+carta_5_mesa[i]+' '*37+'│')
    
    print('│'+' '*25+m_apuesta_5+apuesta_5+' '*26+m_apuesta_6+apuesta_6+' '*26+m_apuesta_1+apuesta_1+' '*23+'│')
    print('│'+(' '*118)+'│')
    print('│'+' '*25+big_small_5+' '*28+big_small_6+' '*28+big_small_1+' '*25+'│')
    for i in range(5):
        print('│'+' '*19+carta_1_cpu5[i]+'  '+carta_2_cpu5[i]+' '*16+carta_1_jugador[i]+'  '+carta_2_jugador[i]+' '*16+carta_1_cpu1[i]+'  '+carta_2_cpu1[i]+' '*19+'│')
    print('│'+' '*22+'┌'+cpu5.decidir+'┐'+' '*22+'┌'+jugador.decidir+'┐'+' '*22+'┌'+cpu1.decidir+'┐'+' '*22+'│')
    print('└'+'─'*22+'┤'+('   ▄▄   ')+'├'+'─'*22+'┤'+('   ▄▄   ')+'├'+'─'*22+'┤'+('   ▄▄   ')+'├'+'─'*22+'┘')
    print(' '*23+'│'+('   ▀▀   ')+'│'+' '*22+'│'+('   ▀▀   ')+'│'+' '*22+'│'+('   ▀▀   ')+'│')
    print(' '+' '*22+'│'+('  ████  ')+'│'+' '*22+'│'+('  ████  ')+'│'+' '*22+'│'+('  ████  ')+'│     BOTE:',bote)
    print(' '+' '*22+'└'+'──'+str(cpu5.fichas)+fichas_5+'┘'+' '*22+'└'+'──'+str(jugador.fichas)+fichas_6+'┘'+' '*22+'└'+'──'+str(cpu1.fichas)+fichas_1+'┘'+' '*22+' ')
