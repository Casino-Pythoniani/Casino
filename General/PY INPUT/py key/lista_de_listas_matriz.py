##from time import sleep
##import os
##from pynput.keyboard import Listener
##clear = lambda: os.system('cls')
##
##lista = [[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ']]
##posx = 0
##posy = 0
##
##lista[posx][posy] = 'O'
##def key_recorder(key):
##    global posx
##    global posy
##    global lista
##
##    
##    key = str(key).replace("'", "")
##    
##    if key == 'Key.down' and posy != 4:
##        lista[posx][posy],lista[posx][posy+1] = lista[posx][posy+1],lista[posx][posy]
##        posy = posy + 1
##        if posy >= 4:
##            posy = 4
##            
##    elif key == 'Key.up' and posy != 0:
##        lista[posx][posy],lista[posx][posy-1] = lista[posx][posy-1],lista[posx][posy]
##        posy = posy - 1
##        if posy <= 0:
##            posy = 0
##            
##    elif key == 'Key.right' and posx != 1:
##        lista[posx][posy],lista[posx+1][posy] = lista[posx+1][posy],lista[posx][posy]
##        posx = posx + 1
##        if posx >= 1:
##            posx = 1
##
##    elif key == 'Key.left' and posx != 0:
##        lista[posx][posy],lista[posx-1][posy] = lista[posx-1][posy],lista[posx][posy]
##        posx = posx - 1
##        if posx <= 0:
##            posx = 0
##     
##    l.stop()
##    
##
##def display():
##    global lista
##    print('╔═══╗╔═══╗')
##    print('║',lista[0][0],'║║',lista[1][0],'║')
##    print('╚═══╝╚═══╝')
##    print('╔═══╗╔═══╗')
##    print('║',lista[0][1],'║║',lista[1][1],'║')
##    print('╚═══╝╚═══╝')
##    print('╔═══╗╔═══╗')
##    print('║',lista[0][2],'║║',lista[1][2],'║')
##    print('╚═══╝╚═══╝')
##    print('╔═══╗╔═══╗')
##    print('║',lista[0][3],'║║',lista[1][3],'║')
##    print('╚═══╝╚═══╝')
##    print('╔═══╗╔═══╗')
##    print('║',lista[0][4],'║║',lista[1][4],'║')
##    print('╚═══╝╚═══╝')
##    print(posx,posy)
##
##
##   
##
##
##
##    
##
##
##while True:
##    clear()
##    display()
##    with Listener(on_press=key_recorder) as l:
##        l.join()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

from time import sleep
import os
from pynput.keyboard import Listener
clear = lambda: os.system('cls')

lista = [['   ','   '],['   ','   ']]
posx = 0
posy = 0

lista[posx][posy] = '<=='
def key_recorder(key):
    global posx
    global posy
    global lista

    
    key = str(key).replace("'", "")
    
    if key == 'Key.down' and posy != 4:
        lista[posx][posy],lista[posx][posy+1] = lista[posx][posy+1],lista[posx][posy]
        posy = posy + 1
        if posy >= 4:
            posy = 4
            
    elif key == 'Key.up' and posy != 0:
        lista[posx][posy],lista[posx][posy-1] = lista[posx][posy-1],lista[posx][posy]
        posy = posy - 1
        if posy <= 0:
            posy = 0
            
    elif key == 'Key.right' and posx != 1:
        lista[posx][posy],lista[posx+1][posy] = lista[posx+1][posy],lista[posx][posy]
        posx = posx + 1
        if posx >= 1:
            posx = 1

    elif key == 'Key.left' and posx != 0:
        lista[posx][posy],lista[posx-1][posy] = lista[posx-1][posy],lista[posx][posy]
        posx = posx - 1
        if posx <= 0:
            posx = 0

    
    l.stop()
    

##def display():
##    global lista
##    print('╔═══╗╔═══╗')
##    print('║',lista[0][0],'║║',lista[1][0],'║')
##    print('╚═══╝╚═══╝')
##    print('╔═══╗╔═══╗')
##    print('║',lista[0][1],'║║',lista[1][1],'║')
##    print('╚═══╝╚═══╝')
##    
##    print(posx,posy)


def display():
    global lista
    print('''
    ╔══════╗       ╔══════╗
    ║  5$  ║ '''+lista[0][0]+'''   ║  10$ ║ '''+lista[1][0]+'''
    ╚══════╝       ╚══════╝

    ╔══════╗       ╔══════╗
    ║  25$ ║ '''+lista[0][1]+'''   ║ 100$ ║ '''+lista[1][1]+'''
    ╚══════╝       ╚══════╝ ''')

    #print(posx,posy)





while True:
    clear()
    display()
    with Listener(on_press=key_recorder) as l:
        l.join()























































###xxxxxxxxxxx-mi adaptacion xa apuesta black jack --xxxxxxxxxxxxxxxxxxx
##
##import os
##from pynput.keyboard import Listener
##clear = lambda: os.system('cls')
##
##posx = 0
##posy = 0
##lista = [[' ',' '],[' ',' ']]
##
##lista[posx][posy] = 'O'
##def key_recorder(key):
##    global posx
##    global posy
##    global lista
##    key = str(key).replace("'", "")
##    if key == 'Key.down' and posy != 4:
##        lista[posx][posy],lista[posx][posy+1] = lista[posx][posy+1],lista[posx][posy]
##        posy = posy + 1
##        if posy >= 4:
##            posy = 4
##            
##    elif key == 'Key.up' and posy != 0:
##        lista[posx][posy],lista[posx][posy-1] = lista[posx][posy-1],lista[posx][posy]
##        posy = posy - 1
##        if posy <= 0:
##            posy = 0
##            
##    elif key == 'Key.right' and posx != 1:
##        lista[posx][posy],lista[posx+1][posy] = lista[posx+1][posy],lista[posx][posy]
##        posx = posx + 1
##        if posx >= 1:
##            posx = 1
##
##    elif key == 'Key.left' and posx != 0:
##        lista[posx][posy],lista[posx-1][posy] = lista[posx-1][posy],lista[posx][posy]
##        posx = posx - 1
##        if posx <= 0:
##            posx = 0
##    l.stop()
##     
##
##         
##def display (x):
##    print:'''
##╔═══════╗       ╔═══════╗                     
##║   5$  ║ '''+x[0][0]+'''      ║  10$  ║ '''+x[0][1]+'''
##╚═══════╝       ╚═══════╝
##
##
##╔═══════╗       ╔═══════╗                     
##║  25$  ║ '''+x[1][0]+'''      ║ 100 $ ║ '''+x[1][1]+'''
##╚═══════╝       ╚═══════╝
##'''
##    return x
##
##while True:
##    clear()
##    lista=display(lista)
##    with Listener(on_press=key_recorder) as l:
##        l.join()




