# 27 HUECOS
from random import randrange
from time import sleep
from bingo_ascii import titulo_menu_bingo,boton_jugar
from pynput.keyboard import Listener
import os
clear = lambda: os.system('cls') 

def crear_carton():
    carton = [['','','','','','','','',''],
              ['','','','','','','','',''],
              ['','','','','','','','','']]
    
    #PONER LOS HUECOS EN EL CARTÓN
    for i in range(3):
        posicion_huecos = []
        while True:
            huecos = randrange(0,9)
            if huecos not in posicion_huecos:
                posicion_huecos.append(huecos)

            if len(posicion_huecos) == 4:
                break
        
        for x in posicion_huecos:
            carton[i][x] = '  '
     
    #PONER LOS NÚMEROS EN EL CARTÓN
    for i in range(9):
        random = []
        cantidad_numeros = 0
        if carton[0][i] != '  ':
            cantidad_numeros += 1
        if carton[1][i] != '  ':
            cantidad_numeros += 1
        if carton[2][i] != '  ':
            cantidad_numeros += 1

        bucle_random = True
        repes = []
        if cantidad_numeros == 0:
            bucle_random = False
        while bucle_random:
            if i == 0:
                r = randrange(1,10)
            if i == 1:
                r = randrange(10,20)
            if i == 2:
                r = randrange(20,30)
            if i == 3:
                r = randrange(30,40)
            if i == 4:
                r = randrange(40,50)
            if i == 5:
                r = randrange(50,60)
            if i == 6:
                r = randrange(60,70)
            if i == 7:
                r = randrange(70,80)
            if i == 8:
                r = randrange(80,91)

            if r not in repes:
                random.append(r)
                repes.append(r)
                random.sort()
                if len(random) == cantidad_numeros:
                    bucle_random = False

        for j in range(3):
            if carton[j][i] != '  ': 
                carton[j][i] = random[0]
                del random[0]
                            
    return carton

def display_carton(carton): ##ascii:│ ┼ ─ ┬ ┴ ┘ └ ├ ┤ ┌ ┐  
    espacio1 = '│ '
    if carton[0][0] == '  ':
        espacio1 = '│'
    
    espacio2 = '│ '
    if carton[1][0] == '  ':
        espacio2 = '│'

    espacio3 = '│ '
    if carton[2][0] == '  ':
        espacio3 = '│'
    
    print('\t\t\t\t\t┌'+((('─'*4)+'┬')*8)+('─'*4)+'┐')
    print('\t\t\t\t\t'+espacio1,carton[0][0],'│',carton[0][1],'│',carton[0][2],'│',carton[0][3],'│',carton[0][4],'│',carton[0][5]
              ,'│',carton[0][6],'│',carton[0][7],'│',carton[0][8],'│')
    print('\t\t\t\t\t├'+((('─'*4)+'┼')*8)+('─'*4)+'┤')
    print('\t\t\t\t\t'+espacio2,carton[1][0],'│',carton[1][1],'│',carton[1][2],'│',carton[1][3],'│',carton[1][4],'│',carton[1][5]
              ,'│',carton[1][6],'│',carton[1][7],'│',carton[1][8],'│')
    print('\t\t\t\t\t├'+((('─'*4)+'┼')*8)+('─'*4)+'┤')
    print('\t\t\t\t\t'+espacio3,carton[2][0],'│',carton[2][1],'│',carton[2][2],'│',carton[2][3],'│',carton[2][4],'│',carton[2][5]
              ,'│',carton[2][6],'│',carton[2][7],'│',carton[2][8],'│')
    print('\t\t\t\t\t└'+((('─'*4)+'┴')*8)+('─'*4)+'┘')

numeros_cantados = []
def cantar_numero():
    while True:
        r = randrange(1,91)
        
        if len(numeros_cantados) == 90:
            break
        
        if r not in numeros_cantados:
            numeros_cantados.append(r)
            return r
        
        if r in numeros_cantados:
            continue

def comprobar_numeros(carton):
    for i in range(3):
        for x in range(9):
            if carton[i][x] == numeros_cantados[-1]:
                carton[i][x] = '  '
    return carton

def linea(carton):
    contador_l1 = 0
    contador_l2 = 0
    contador_l3 = 0
    for x in range(3):
        for i in carton[x]:
            if x == 0:
                if i == '  ':
                    contador_l1 += 1
                if contador_l1 == 9:
                    return True
            if x == 1:
                if i == '  ':
                    contador_l2 += 1
                if contador_l2 == 9:
                    return True
            if x == 2:
                if i == '  ':
                    contador_l3 += 1
                if contador_l3 == 9:
                    return True

lis = [' BUY ','     ','     ']
posx = 0
romper_bucle = 0
salir = 0

def bingo(carton):
    contador = 0
    for x in range(3):
        for i in carton[x]:
            if i == '  ':
                contador += 1
            if contador == 27:
                numeros_cantados.clear()
                return True

def display_numeros():
    diccionario = {'1':[' __ ','/_ |',' | |',' | |',' | |',' |_|'],
                    '2':[' ___  ','|__ \ ','   ) |','  / / ',' / /_ ','|____|'],
                    '3':[' ____  ','|___ \ ','  __) |',' |__ < ',' ___) |','|____/ '],
                    '4':[' _  _   ','| || |  ','| || |_ ','|__   _|','   | |  ','   |_|  '],
                    '5':[' _____ ','| ____|','| |__  ','|___ \ ',' ___) |','|____/ '], 
                    '6':['   __  ','  / /  ',' / /_  ','|  _ \ ','| (_) |',' \___/ '], 
                    '7':[' ______ ','|____  |','    / / ','   / /  ','  / /   ',' /_/    '], 
                    '8':['  ___  ',' / _ \ ','| (_) |',' > _ < ','| (_) |',' \___/ '], 
                    '9':['  ___  ',' / _ \ ','| (_) |',' \__, |','   / / ',' /_/   '], 
                    '0':['  ___  ',' / _ \ ','| | | |','| | | |','| |_| |',' \___/ ']}
    
    nums = cantar_numero()
    nums = str(nums)
    for x in range(6):         
        for i in nums: 
            print(diccionario[i][x],end = ' ')  
        print()

def key_recorder(key):
    global posx
    global romper_bucle
    global salir

    key = str(key).replace("'", "")

    if key == 'Key.right' and posx != 2:
        lis[posx+1] = ' BUY '
        lis[posx] = '     '
        posx += 1
        if posx >= 2:
            posx = 2
        
    elif key == 'Key.left' and posx != 0:
        lis[posx-1] = ' BUY '
        lis[posx] = '     '
        posx -= 1
        if posx <= 0:
            posx = 0

    elif key == 'Key.enter':
        romper_bucle = 1
    
    elif key == 'Key.esc':
        romper_bucle = 1
        salir = 1
        
        # Key.esc
        # Key.enter
    l.stop()

# bucle_menu             

def menu_bingo_dibujo(fichas): ##ascii:│ ┼ ─ ┬ ┴ ┘ └ ├ ┤ ┌ ┐  ║ ╔ ═ ╗ ╚ ╝ ╞
    titulo_menu_bingo(fichas)
    print('''
                        ┌────────────────────────┐   ┌────────────────────────┐   ┌────────────────────────┐
                        │        1 CARTÓN        │   │       2 CARTONES       │   │       3 CARTONES       │ 
                        │        50 Fichas       │   │       100 Fichas       │   │       150 Fichas       │
                        │        ┌┬┬┬┬┬┬┐        │   │  ┌┬┬┬┬┬┬┐    ┌┬┬┬┬┬┬┐  │   │  ┌┬┬┬┬┬┬┐    ┌┬┬┬┬┬┬┐  │ 
                        │        ├┼┼┼┼┼┼┤        │   │  ├┼┼┼┼┼┼┤    ├┼┼┼┼┼┼┤  │   │  ├┼┼┼┼┼┼┤    ├┼┼┼┼┼┼┤  │
                        │        └┴┴┴┴┴┴┘        │   │  └┴┴┴┴┴┴┘    └┴┴┴┴┴┴┘  │   │  └┴┴┴┴┴┴┘    └┴┴┴┴┴┴┘  │
                        │                        │   │                        │   │        ┌┬┬┬┬┬┬┐        │
                        ╞═════╗                  │   ╞═════╗                  │   ╞═════╗  ├┼┼┼┼┼┼┤        │
                        │'''+lis[0]+'''║                  │   │'''+lis[1]+'''║                  │   │'''+lis[2]+'''║  └┴┴┴┴┴┴┘        │
                        ╘═════╝──────────────────┘   ╘═════╝──────────────────┘   ╘═════╝──────────────────┘
    ''')
    boton_jugar()
    

def menu_bingo_ejecucion(fichas):
    global l
    global romper_bucle
    while True:
        clear()
        menu_bingo_dibujo(fichas)
        with Listener(on_press=key_recorder) as l:
            l.join()
            if romper_bucle == 1:
                romper_bucle = 0
                break
            
            
def numero_de_cartones():
    global salir
    if salir == 1:
        salir = 0
        return 0

    if lis[0] == ' BUY ':
        return 1
    
    if lis[1] == ' BUY ':
        return 2
    
    if lis[2] == ' BUY ':
        return 3
    
    










