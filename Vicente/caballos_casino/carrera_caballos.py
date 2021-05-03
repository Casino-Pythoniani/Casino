from time import sleep 
import random
import os
from pynput.keyboard import Listener
from dibujo_caballos import dibujo_victoria_caballo
clear = lambda: os.system('cls')    ##Función para borrar la consola

def caballos_elegidos():        ##Esta función mete en la lista vacía 6 nombres y valida que no se repitan
    while len(caballos_a_competir) != 6:
        validar = random.choice(nombres_caballos)
        if validar not in caballos_a_competir:
            caballos_a_competir.append(validar)

def caballo1(detras):      ##Dibujo del caballo Nº1
    delante = 141 - detras 
    print('═'*156+'╦══╗')
    print(' '*detras,'        ,--, ',' '*delante+'║  ║')
    print(' '*detras,'  _ ___/ /\\| ',' '*delante+'║  ║')
    print(' '*detras,' ;( )1 , )   ',' '*delante+'║  ║')
    print(' '*detras,'; // ¯¯`--;  ',' '*delante+'║  ║')
    print(' '*detras,'  \\     |    ',' '*delante+'║  ║')
    print('═'*156+'╩══╝')

def caballo2(detras):      ##Dibujo del caballo Nº2
    delante = 141 - detras 
    print('═'*156+'╦══╗')
    print(' '*detras,'        ,--, ',' '*delante+'║  ║')
    print(' '*detras,'  _ ___/ /\\| ',' '*delante+'║  ║')
    print(' '*detras,' ;( )2 , )   ',' '*delante+'║  ║')
    print(' '*detras,'; // ¯¯`--;  ',' '*delante+'║  ║')
    print(' '*detras,'  \\     |    ',' '*delante+'║  ║')
    print('═'*156+'╩══╝')

def caballo3(detras):      ##Dibujo del caballo Nº3
    delante = 141 - detras 
    print('═'*156+'╦══╗')
    print(' '*detras,'        ,--, ',' '*delante+'║  ║')
    print(' '*detras,'  _ ___/ /\\| ',' '*delante+'║  ║')
    print(' '*detras,' ;( )3 , )   ',' '*delante+'║  ║')
    print(' '*detras,'; // ¯¯`--;  ',' '*delante+'║  ║')
    print(' '*detras,'  \\     |    ',' '*delante+'║  ║')
    print('═'*156+'╩══╝')

def caballo4(detras):      ##Dibujo del caballo Nº4
    delante = 141 - detras 
    print('═'*156+'╦══╗')
    print(' '*detras,'        ,--, ',' '*delante+'║  ║')
    print(' '*detras,'  _ ___/ /\\| ',' '*delante+'║  ║')
    print(' '*detras,' ;( )4 , )   ',' '*delante+'║  ║')
    print(' '*detras,'; // ¯¯`--;  ',' '*delante+'║  ║')
    print(' '*detras,'  \\     |    ',' '*delante+'║  ║')
    print('═'*156+'╩══╝')

def caballo5(detras):      ##Dibujo del caballo Nº5
    delante = 141 - detras 
    print('═'*156+'╦══╗')
    print(' '*detras,'        ,--, ',' '*delante+'║  ║')
    print(' '*detras,'  _ ___/ /\\| ',' '*delante+'║  ║')
    print(' '*detras,' ;( )5 , )   ',' '*delante+'║  ║')
    print(' '*detras,'; // ¯¯`--;  ',' '*delante+'║  ║')
    print(' '*detras,'  \\     |    ',' '*delante+'║  ║')
    print('═'*156+'╩══╝')

def caballo6(detras):      ##Dibujo del caballo Nº6
    delante = 141 - detras 
    print('═'*156+'╦══╗')
    print(' '*detras,'        ,--, ',' '*delante+'║  ║')
    print(' '*detras,'  _ ___/ /\\| ',' '*delante+'║  ║')
    print(' '*detras,' ;( )6 , )   ',' '*delante+'║  ║')
    print(' '*detras,'; // ¯¯`--;  ',' '*delante+'║  ║')
    print(' '*detras,'  \\     |    ',' '*delante+'║  ║')
    print('═'*156+'╩══╝')

def titulo_carrera_caballos():
    print('''

    ░█████╗░░█████╗░██████╗░██████╗░███████╗██████╗░░█████╗░  ██████╗░███████╗   ░█████╗░░█████╗░██████╗░░█████╗░██╗░░░░░██╗░░░░░░█████╗░░██████╗
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██╔════╝   ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░░░██║░░░░░██╔══██╗██╔════╝
    ██║░░╚═╝███████║██████╔╝██████╔╝█████╗░░██████╔╝███████║  ██║░░██║█████╗░░   ██║░░╚═╝███████║██████╦╝███████║██║░░░░░██║░░░░░██║░░██║╚█████╗░
    ██║░░██╗██╔══██║██╔══██╗██╔══██╗██╔══╝░░██╔══██╗██╔══██║  ██║░░██║██╔══╝░░   ██║░░██╗██╔══██║██╔══██╗██╔══██║██║░░░░░██║░░░░░██║░░██║░╚═══██╗
    ╚█████╔╝██║░░██║██║░░██║██║░░██║███████╗██║░░██║██║░░██║  ██████╔╝███████╗   ╚█████╔╝██║░░██║██████╦╝██║░░██║███████╗███████╗╚█████╔╝██████╔╝
    ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚══════╝   ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝░╚════╝░╚═════╝░

''')

def movimiento_todos_caballos():    ##Función que lleva por un sistema de porcentajes los movimientos de los caballos
    global movimiento_caballo1
    global movimiento_caballo2
    global movimiento_caballo3
    global movimiento_caballo4
    global movimiento_caballo5
    global movimiento_caballo6
    azar = random.choice(range(1,101)) ##Con un random del 1 al 100 creamos el porcentaje
    if azar <= 25:
        movimiento_caballo1 += 10 ##El caballo Nº1 tiene un 25% de avanzar 10
        
    elif azar in range(26,41):
        movimiento_caballo2 += 14 ##El caballo Nº2 tiene un 15% de avanzar 14

    elif azar in range(41,51):
        movimiento_caballo3 += 14 ##El caballo Nº3 tiene un 10% de avanzar 14

    elif azar in range(51,76):
        movimiento_caballo4 += 10 ##El caballo Nº4 tiene un 25% de avanzar 10
    
    elif azar in range(76,91):
        movimiento_caballo5 += 14 ##El caballo Nº5 tiene un 15% de avanzar 14

    elif azar in range(91,101):
        movimiento_caballo6 += 14 ##El caballo Nº6 tiene un 10% de avanzar 14


def tablero_para_apostar():
    global fichas
    esp1 = 23-len(caballos_a_competir[0])  
    esp2 = 23-len(caballos_a_competir[1])
    esp3 = 23-len(caballos_a_competir[2])
    esp4 = 23-len(caballos_a_competir[3])
    esp5 = 23-len(caballos_a_competir[4])
    esp6 = 23-len(caballos_a_competir[5])
    apu1 = ' │'
    apu2 = ' │'
    apu3 = ' │'
    apu4 = ' │'
    apu5 = ' │'
    apu6 = ' │'
    
    if apuesta_caballo1 >= 10:
        apu1 = '│'
    if apuesta_caballo2 >= 10:
        apu2 = '│'
    if apuesta_caballo3 >= 10:
        apu3 = '│'
    if apuesta_caballo4 >= 10:
        apu4 = '│'
    if apuesta_caballo5 >= 10:
        apu5 = '│'
    if apuesta_caballo6 >= 10:
        apu6 = '│'
    if fichas in range(0,10):
        fi = '     │'
    if fichas in range(10,100):
        fi = '    │'
    if fichas in range(100,1000):
        fi = '   │'
    if fichas in range(1000,10000):
        fi = '  │'
    if fichas in range(10000,100000):
        fi = ' │'
    if fichas in range(100000,1000000):
        fi = '│'

        
    titulo_carrera_caballos()
    print('\n\n\n')
    print('\t\t\t                                              ┼──────────────────┼ ')
    print('\t\t\t                                              │ FICHAS ═►',fichas,fi)  
    print('\t\t\t      ┼───────────┼        ┼────────┼         ┼──────────────────┼ ')   
    print('\t\t\t      │ CABALLOS  │        │ CUOTAS │                            ')     
    print('\t\t\t┼───┼─┴───────────┴────────┴────────┴─┼────┼                      ┼────────────────┼')
    print('\t\t\t│ 1 │ ',caballos_a_competir[0],esp1*' ','2.00'+'  │',apuesta_caballo1,apu1,lista_menu_apostar[0],'                 │   CONTROLES    │')
    print('\t\t\t┼───┼─────────────────────────────────┼────┼                      ┼────────────────┼')
    print('\t\t\t│ 2 │ ',caballos_a_competir[1],esp2*' ','4.00'+'  │',apuesta_caballo2,apu2,lista_menu_apostar[1],'                 │Desplazarse: ▲ ▼│')
    print('\t\t\t┼───┼─────────────────────────────────┼────┼                      │                │      ')                
    print('\t\t\t│ 3 │ ',caballos_a_competir[2],esp3*' ','6.00'+'  │',apuesta_caballo3,apu3,lista_menu_apostar[2],'                 │Subir apuesta: ►│')
    print('\t\t\t┼───┼─────────────────────────────────┼────┼                      │                │')
    print('\t\t\t│ 4 │ ',caballos_a_competir[3],esp4*' ','2.00'+'  │',apuesta_caballo4,apu4,lista_menu_apostar[3],'                 │Bajar apuesta: ◄│')
    print('\t\t\t┼───┼─────────────────────────────────┼────┼                      │                │')
    print('\t\t\t│ 5 │ ',caballos_a_competir[4],esp5*' ','4.00'+'  │',apuesta_caballo5,apu5,lista_menu_apostar[4],'                 │Apostar: space  │')
    print('\t\t\t┼───┼─────────────────────────────────┼────┼                      ┼────────────────┼')
    print('\t\t\t│ 6 │ ',caballos_a_competir[5],esp6*' ','6.00'+'  │',apuesta_caballo6,apu6,lista_menu_apostar[5])
    print('\t\t\t┼───┼───────┬─────────────────┬───────┼────┼')
    print('\t\t\t            │     APOSTAR',lista_menu_apostar[6],'│')
    print('\t\t\t            ┼─────────────────┼')
                    
def movimiento_tablero_apostar(key):
    global pos_cab 
    global lista_menu_apostar
    global apuesta_caballo1
    global apuesta_caballo2
    global apuesta_caballo3
    global apuesta_caballo4
    global apuesta_caballo5
    global apuesta_caballo6
    global bucle_carrera_caballos
    global fichas
    key = str(key).replace("'", "")
    
    if key == 'Key.down' and pos_cab != 6:
        lista_menu_apostar[pos_cab],lista_menu_apostar[pos_cab+1] = lista_menu_apostar[pos_cab+1],lista_menu_apostar[pos_cab]
        pos_cab += 1
        if pos_cab >= 6:
            pos_cab = 6
            
    elif key == 'Key.up' and pos_cab != 0:
        lista_menu_apostar[pos_cab],lista_menu_apostar[pos_cab-1] = lista_menu_apostar[pos_cab-1],lista_menu_apostar[pos_cab]
        pos_cab -= 1
        if pos_cab <= 0:
            pos_cab = 0
            
    elif key == 'Key.right':
        if '◄══' == lista_menu_apostar[0]:
            apuesta_caballo1 += 5
            fichas -= 5
            
            if apuesta_caballo1 > 95:
                apuesta_caballo1 = 95
                fichas += 5
            
        elif '◄══' == lista_menu_apostar[1]:
            apuesta_caballo2 += 5
            fichas -= 5
            
            if apuesta_caballo2 > 95:
                apuesta_caballo2 = 95
                fichas += 5

        elif '◄══' == lista_menu_apostar[2]:
            apuesta_caballo3 += 5
            fichas -= 5
            
            if apuesta_caballo3 > 95:
                apuesta_caballo3 = 95
                fichas += 5

        elif '◄══' == lista_menu_apostar[3]:
            apuesta_caballo4 += 5
            fichas -= 5
            
            if apuesta_caballo4 > 95:
                apuesta_caballo4 = 95
                fichas += 5

        elif '◄══' == lista_menu_apostar[4]:
            apuesta_caballo5 += 5
            fichas -= 5
            
            if apuesta_caballo5 > 95:
                apuesta_caballo5 = 95
                fichas += 5
            
        elif '◄══' == lista_menu_apostar[5]:
            apuesta_caballo6 += 5
            fichas -= 5
            
            if apuesta_caballo6 > 95:
                apuesta_caballo6 = 95
                fichas += 5

    elif key == 'Key.left':
        if '◄══' == lista_menu_apostar[0]:
            apuesta_caballo1 -= 5
            fichas += 5
            
            if apuesta_caballo1 < 0:
                apuesta_caballo1 = 0
                fichas -= 5
                
            
        elif '◄══' == lista_menu_apostar[1]:
            apuesta_caballo2 -= 5
            fichas += 5
            
            if apuesta_caballo2 < 0:
                apuesta_caballo2 = 0
                fichas -= 5
            
        elif '◄══' == lista_menu_apostar[2]:
            apuesta_caballo3 -= 5
            fichas += 5
            
            if apuesta_caballo3 < 0:
                apuesta_caballo3 = 0
                fichas -= 5
            
        elif '◄══' == lista_menu_apostar[3]:
            apuesta_caballo4 -= 5
            fichas += 5
            
            if apuesta_caballo4 < 0:
                apuesta_caballo4 = 0
                fichas -= 5
            
        elif '◄══' == lista_menu_apostar[4]:
            apuesta_caballo5 -= 5
            fichas += 5
            
            if apuesta_caballo5 < 0:
                apuesta_caballo5 = 0
                fichas -= 5

        elif '◄══' == lista_menu_apostar[5]:
            apuesta_caballo6 -= 5
            fichas += 5
            
            if apuesta_caballo6 < 0:
                apuesta_caballo6 = 0
                fichas -= 5
                
    elif key == 'Key.space' and pos_cab == 6:
        bucle_carrera_caballos = False
                
    l.stop()


    
fichas = 500
clear()
while True:    
    
    ##Lista con varios nombres de caballos
    nombres_caballos = ['Obelix Da Torre','Haajoos','Speedful','Luanco','Kamidia','Karibbean Dream','Lady Marengo','Melampo','Trece','Rockola','Nader','Mr Hobbs','Tacio','Anfion','Chapman Billy','Yaneda','Costa Esmeralda','Gormaz','ZeeBullet','Atlantico',"Cannaby's Dream",'Delta Crucis','Run Run','Myaldagoba','Danzing De Saon','Niagara','Lenda Da Torre','Mill Valley','Spinerett']
    caballos_a_competir = []        ##En esta lista vacía se añaden 6 nombres de caballos aleatoriamente

    movimiento_caballo1 = 0         ##Movimiento del caballo Nº1
    movimiento_caballo2 = 0         ##Movimiento del caballo Nº2
    movimiento_caballo3 = 0         ##Movimiento del caballo Nº3
    movimiento_caballo4 = 0         ##Movimiento del caballo Nº4
    movimiento_caballo5 = 0         ##Movimiento del caballo Nº5
    movimiento_caballo6 = 0         ##Movimiento del caballo Nº6

    apuesta_caballo1 = 0
    apuesta_caballo2 = 0
    apuesta_caballo3 = 0
    apuesta_caballo4 = 0
    apuesta_caballo5 = 0
    apuesta_caballo6 = 0

    pos_cab = 0
    
    lista_menu_apostar = ['◄══','   ','   ','   ','   ','   ','   ']    

    caballos_elegidos()

    bucle_carrera_caballos = True
    
    while bucle_carrera_caballos == True:
        clear()
        tablero_para_apostar()
        
        with Listener(on_press=movimiento_tablero_apostar) as l:
            l.join()
            
    print('\n'*42)
    while True:
        movimiento_todos_caballos()
        print(("\033[F") * 43)
        caballo1(movimiento_caballo1)   
        caballo2(movimiento_caballo2)
        caballo3(movimiento_caballo3)
        caballo4(movimiento_caballo4)
        caballo5(movimiento_caballo5)
        caballo6(movimiento_caballo6)
        
        if movimiento_caballo1 >= 140:
            movimiento_caballo1 = 140
            print(("\033[F") * 43)
            caballo1(movimiento_caballo1)   
            caballo2(movimiento_caballo2)
            caballo3(movimiento_caballo3)
            caballo4(movimiento_caballo4)
            caballo5(movimiento_caballo5)
            caballo6(movimiento_caballo6)
            fichas = fichas + (apuesta_caballo1*2)
            sleep(5)
            clear()
            dibujo_victoria_caballo(caballos_a_competir[0],1,apuesta_caballo1*2)
            sleep(5)
            bucle_carrera_caballos = True
            break
            
        if movimiento_caballo2 >= 140:
            movimiento_caballo2 = 140
            print(("\033[F") * 43)
            caballo1(movimiento_caballo1)   
            caballo2(movimiento_caballo2)
            caballo3(movimiento_caballo3)
            caballo4(movimiento_caballo4)
            caballo5(movimiento_caballo5)
            caballo6(movimiento_caballo6)
            fichas = fichas + (apuesta_caballo2*4)
            sleep(5)
            clear()
            dibujo_victoria_caballo(caballos_a_competir[1],2,apuesta_caballo2*4)
            sleep(5)
            bucle_carrera_caballos = True
            break
            
        if movimiento_caballo3 >= 140:
            movimiento_caballo3 = 140
            print(("\033[F") * 43)
            caballo1(movimiento_caballo1)   
            caballo2(movimiento_caballo2)
            caballo3(movimiento_caballo3)
            caballo4(movimiento_caballo4)
            caballo5(movimiento_caballo5)
            caballo6(movimiento_caballo6)
            fichas = fichas + (apuesta_caballo3*6)
            sleep(5)
            clear()
            dibujo_victoria_caballo(caballos_a_competir[2],3,apuesta_caballo3*6)
            sleep(5)
            bucle_carrera_caballos = True
            break
            
            
        if movimiento_caballo4 >= 140:
            movimiento_caballo4 = 140
            print(("\033[F") * 43)
            caballo1(movimiento_caballo1)   
            caballo2(movimiento_caballo2)
            caballo3(movimiento_caballo3)
            caballo4(movimiento_caballo4)
            caballo5(movimiento_caballo5)
            caballo6(movimiento_caballo6)
            fichas = fichas + (apuesta_caballo4*2)
            sleep(5)
            clear()
            dibujo_victoria_caballo(caballos_a_competir[3],4,apuesta_caballo4*2)
            sleep(5)
            bucle_carrera_caballos = True
            break
            
            
        if movimiento_caballo5 >= 140:
            movimiento_caballo5 = 140
            print(("\033[F") * 43)
            caballo1(movimiento_caballo1)   
            caballo2(movimiento_caballo2)
            caballo3(movimiento_caballo3)
            caballo4(movimiento_caballo4)
            caballo5(movimiento_caballo5)
            caballo6(movimiento_caballo6)
            fichas = fichas + (apuesta_caballo5*4)
            sleep(5)
            clear()
            dibujo_victoria_caballo(caballos_a_competir[4],5,apuesta_caballo5*4)
            sleep(5)
            bucle_carrera_caballos = True
            break
            
            
        if movimiento_caballo6 >= 140:
            movimiento_caballo6 = 140
            print(("\033[F") * 43)
            caballo1(movimiento_caballo1)   
            caballo2(movimiento_caballo2)
            caballo3(movimiento_caballo3)
            caballo4(movimiento_caballo4)
            caballo5(movimiento_caballo5)
            caballo6(movimiento_caballo6)
            fichas = fichas + (apuesta_caballo6*6)
            sleep(5)
            clear()
            dibujo_victoria_caballo(caballos_a_competir[5],6,apuesta_caballo6*6)
            sleep(5)
            bucle_carrera_caballos = True
            break
                
        sleep(.1)





















