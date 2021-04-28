#from time import sleep
import os
from pynput.keyboard import Listener
clear = lambda: os.system('cls')

lista = [' ',' ',' ',' ',' ',' ']
pos = 0

lista[pos] = 'O'
def key_recorder(key):
    global pos
    global lista
    global n0
    global n1
    global n2
    global n3
    global n4
    
    key = str(key).replace("'", "")
    
    if key == 'Key.down' and pos != 4:
        lista[pos],lista[pos+1] = lista[pos+1],lista[pos]
        pos = pos + 1
        if pos >= 4:
            pos = 4
            
    elif key == 'Key.up' and pos != 0:
        lista[pos],lista[pos-1] = lista[pos-1],lista[pos]
        pos = pos - 1
        if pos <= 0:
            pos = 0
            
    elif key == 'Key.right':
        if 'O' == lista[0]:
            n0 = n0 + 1
            
        elif 'O' == lista[1]:
            n1 = n1 + 1

        elif 'O' == lista[2]:
            n2 = n2 + 1

        elif 'O' == lista[3]:
            n3 = n3 + 1

        elif 'O' == lista[4]:
            n4 = n4 + 1

    elif key == 'Key.left':
        if 'O' == lista[0]:
            n0 = n0 - 1
            if n0 <= 0:
                n0 = 0
            
        elif 'O' == lista[1]:
            n1 = n1 - 1
            if n1 <= 0:
                n1 = 0
            
        elif 'O' == lista[2]:
            n2 = n2 - 1
            if n2 <= 0:
                n2 = 0
            
        elif 'O' == lista[3]:
            n3 = n3 - 1
            if n3 <= 0:
                n3 = 0
            
        elif 'O' == lista[4]:
            n4 = n4 - 1
            if n4 <= 0:
                n4 = 0
            
    l.stop()
    
n0 = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0

def display():
    global lista
    print('╔═══╗')
    print('║',n0,'║',lista[0])
    print('╚═══╝')
    print('╔═══╗')
    print('║',n1,'║',lista[1])
    print('╚═══╝')
    print('╔═══╗')
    print('║',n2,'║',lista[2])
    print('╚═══╝')
    print('╔═══╗')
    print('║',n3,'║',lista[3])
    print('╚═══╝')
    print('╔═══╗')
    print('║',n4,'║',lista[4])
    print('╚═══╝')
    print(pos)


while True:
    clear()
    display()
    with Listener(on_press=key_recorder) as l:
        l.join()
















