
import os
from time import sleep
from random import choice
import playsound
import vlc


clear = lambda: os.system("cls")

def ruleta_total():
    lista_ruleta=[]
    for i in range(9):
        lista_ruleta.append([])  
    for x in range(12):
        lista_ruleta[0].append('   ')
    for v in range(1,8):
        for c in range(2):
            lista_ruleta[v].append('   ')
    for x in range(12):
        lista_ruleta[8].append('   ')

    # Se consigue El valor de random del archivo taleromovimiento.py
    archivo1 = open("./Ruleta_Europea/archivo1.txt","r")
    random = int(archivo1.read())
    archivo1.close()

    def ruleta():
        print('''
        ┌─────────┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬─────────┐
        │         │   │   │   │   │   │   │   │   │   │   │         │
        │   15    │  3│ 24│ 36│ 13│ 1 │ 00│ 27│ 10│ 25│ 29│    12   │
        │     ╔═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╗     │
        │     ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║     │
        │     ║'''+lista_ruleta[0][0]+'''║'''+lista_ruleta[0][1]+'''║'''+lista_ruleta[0][2]+'''║'''+lista_ruleta[0][3]+'''║'''+lista_ruleta[0][4]+'''║'''+lista_ruleta[0][5]+'''║'''+lista_ruleta[0][6]+'''║'''+lista_ruleta[0][7]+'''║'''+lista_ruleta[0][8]+'''║'''+lista_ruleta[0][9]+'''║'''+lista_ruleta[0][10]+'''║'''+lista_ruleta[0][11]+'''║     │
        ├─────╫═══╬═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╬═══╫─────┤
        │     ║   ║                                       ║   ║     │
        │  34 ║'''+lista_ruleta[1][0]+'''║                                       ║'''+lista_ruleta[1][1]+'''║ 8   │
        ├─────╫═══╣                                       ╠═══╫─────┤
        │     ║   ║                                       ║   ║     │
        │  22 ║'''+lista_ruleta[2][0]+'''║                                       ║'''+lista_ruleta[2][1]+'''║ 19  │
        ├─────╫═══╣                                       ╠═══╫─────┤
        │     ║   ║                    █                  ║   ║     │
        │   5 ║'''+lista_ruleta[3][0]+'''║                    █                  ║'''+lista_ruleta[3][1]+'''║ 31  │
        ├─────╫═══╣                    █                  ╠═══╫─────┤
        │     ║   ║                  █████                ║   ║     │
        │  17 ║'''+lista_ruleta[4][0]+'''║           ▀▀▀▀▀▀▀█████▀▀▀▀▀▀▀         ║'''+lista_ruleta[4][1]+'''║ 18  │
        ├─────╫═══╣                    █                  ╠═══╫─────┤
        │     ║   ║                    █                  ║   ║     │    
        │  32 ║'''+lista_ruleta[5][0]+'''║                    █                  ║'''+lista_ruleta[5][1]+'''║ 6   │
        ├─────╫═══╣                                       ╠═══╫─────┤
        │     ║   ║                                       ║   ║     │
        │  20 ║'''+lista_ruleta[6][0]+'''║                                       ║'''+lista_ruleta[6][1]+'''║ 21  │
        ├─────╫═══╣                                       ╠═══╫─────┤
        │     ║   ║                                       ║   ║     │
        │   7 ║'''+lista_ruleta[7][0]+'''║                                       ║'''+lista_ruleta[7][1]+'''║ 33  │
        ├─────╫═══╬═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╬═══╫─────┤
        │     ║'''+lista_ruleta[8][0]+'''║'''+lista_ruleta[8][1]+'''║'''+lista_ruleta[8][2]+'''║'''+lista_ruleta[8][3]+'''║'''+lista_ruleta[8][4]+'''║'''+lista_ruleta[8][5]+'''║'''+lista_ruleta[8][6]+'''║'''+lista_ruleta[8][7]+'''║'''+lista_ruleta[8][8]+'''║'''+lista_ruleta[8][9]+'''║'''+lista_ruleta[8][10]+'''║'''+lista_ruleta[8][11]+'''║     │
        │     ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║     │
        │     ╚═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╝     │
        │   11    │ 30│ 26│  9│ 28│  0│  2│ 14│ 35│ 23│  4│    16   │
        │         │   │   │   │   │   │   │   │   │   │   │         │
        └─────────┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴─────────┘

        ''')

    #Fila de arriba
    if random == 15:
        p1 = 0
        p2 = 0 
    elif random == 3:
        p1 = 0
        p2 = 1
    elif random == 24:
        p1 = 0
        p2 = 2
    elif random == 36:
        p1 = 0
        p2 = 3
    elif random == 13:
        p1 = 0
        p2 = 4
    elif random == 1:
        p1 = 0
        p2 = 5
    elif random == 00:
        p1 = 0
        p2 = 6
    elif random == 27:
        p1 = 0
        p2 = 7
    elif random == 10:
        p1 = 0
        p2 = 8
    elif random == 25:
        p1 = 0
        p2 = 9
        
    elif random == 29:
        p1 = 0
        p2 = 10
    elif random == 12:
        p1 = 0
        p2 = 11
    
    #Fila de la derecha
    elif random == 8:
        p1 = 1
        p2 = 1
    elif random == 19:
        p1 = 2
        p2 = 1
    elif random == 31:
        p1 = 3
        p2 = 1
    elif random == 18:
        p1 = 4
        p2 = 1
    elif random == 6:
        p1 = 5
        p2 = 1
    elif random == 21:
        p1 = 6
        p2 = 1
    elif random == 33:
        p1 = 7
        p2 = 1

    # Fila de abajo
    elif random == 11:
        p1 = 8
        p2 = 0 
    elif random == 30:
        p1 = 8
        p2 = 1
    elif random == 26:
        p1 = 8
        p2 = 2
    elif random == 9:
        p1 = 8
        p2 = 3
    elif random == 28:
        p1 = 8
        p2 = 4
    elif random == 0:
        p1 = 8
        p2 = 5
    elif random == 2:
        p1 = 8
        p2 = 6
    elif random == 14:
        p1 = 8
        p2 = 7
    elif random == 35:
        p1 = 8
        p2 = 8
    elif random == 23:
        p1 = 8
        p2 = 9
    elif random == 4:
        p1 = 8
        p2 = 10
    elif random == 16:
        p1 = 8
        p2 = 11
    #Fila de la izquierda
    elif random == 34:
        p1 = 1
        p2 = 0
    elif random == 22:
        p1 = 2
        p2 = 0
    elif random == 5:
        p1 = 3
        p2 = 0
    elif random == 17:
        p1 = 4
        p2 = 0
    elif random == 32:
        p1 = 5
        p2 = 0
    elif random == 20:
        p1 = 6
        p2 = 0
    elif random == 7:
        p1 = 7
        p2 = 0

    # Movimiento de la pelota en el tablero
    vida = 1

    c_veces = [2,3]
    veces = choice(c_veces)
    contador1 = veces-1
    volumen = 80

    velocidad_vueltas = 0.05
    clear()

    #Sonido del giro de la ruleta
    if veces == 2:
            p = vlc.MediaPlayer("./Ruleta_Europea/musica/sonido_ruleta.mp3")
            p.audio_set_volume(volumen)
            p.play()
    else:
        p = vlc.MediaPlayer("./Ruleta_Europea/musica/sonido_ruleta_3vueltas.mp3")
        p.audio_set_volume(volumen)
        p.play()

    for a in range(veces):

        velocidad_rotacion = velocidad_vueltas

        posx = 0
        posy = 6

        for a in range(6):
            
            lista_ruleta[posx][posy] = ' ● '
            lista_ruleta[posx][posy-1] = '   '
            print("\033[A"*38)
            ruleta()
            sleep(velocidad_rotacion)
            if posx == p1 and posy == p2 and contador1 == 0 or vida == 0 and contador1 == 0:
                vida = 0
                if random in [00,27,10,25,29,12]:
                    print("\033[A"*38)

                    ruleta()
                    sleep(2)
                    p.stop()
                break
                
            posy += 1

        # break
        # sleep(3)

        if lista_ruleta[0][11] == ' ● ':
            lista_ruleta[0][11] = '   '
            
            for b in range(1,8):
                posx = b 
                posy = 1

                # clear()
                
                lista_ruleta[b][1] = ' ● '
                lista_ruleta[b-1][1] = '   '
                print("\033[A"*38)
                ruleta()
                sleep(velocidad_rotacion)

                if posx == p1 and posy == p2 and contador1 == 0 or vida == 0 and contador1 == 0:
                    vida = 0
                    if random in [8,19,31,18,6,21,33]:
                        # clear()
                        print("\033[A"*38)
                        ruleta()
                        p.stop()
                        sleep(1)
                        
                    break


        for a in range(12-1,-1,-1):
            

            # clear()
            print("\033[A"*38)
            if posx == p1 and posy == p2 and contador1 == 0 or vida == 0 and contador1 == 0:
                vida = 0
                if random in [11,30,26,9,28,0,2,14,35,23,4,16]:
                    print("\033[A"*38)
                    ruleta()
                    p.stop()
                    sleep(1)
                    
                break
            if lista_ruleta[7][1] == ' ● ':
                lista_ruleta[7][1] = '   '
                lista_ruleta[8][11] = ' ● '
            else:
                lista_ruleta[8][a] = ' ● '
                lista_ruleta[8][a+1] = '   '

            posx = 8
            posy = a
            
            print("\033[A"*38)
            ruleta()
            sleep(velocidad_rotacion)

        for a in range(8-1,-1,-1):
            # clear()
            if posx == p1 and posy == p2  and contador1 == 0 or vida == 0 and contador1 == 0:
                vida = 0
                if random in [15,34,22,5,17,32,20,7,11]:
                    print("\033[A"*38)
                    ruleta()
                    p.stop()
                    sleep(1)
                   
                break
            if lista_ruleta[8][0] == ' ● ':
                lista_ruleta[8][0] = '   '
                lista_ruleta[7][0] = ' ● '
            else:
                lista_ruleta[a][0] = ' ● '
                lista_ruleta[a+1][0] = '   '
            
            posx = a
            posy = 0

            print("\033[A"*38)
            ruleta()
            sleep(velocidad_rotacion)

        for a in range(1,6):
            # clear()
            if posx == p1 and posy == p2 and contador1 == 0 or vida == 0 and contador1 == 0:
                vida = 0
                if random in [15,3,24,36,13,1]:
                    print("\033[A"*38)
                    ruleta()
                    p.stop()
                    sleep(1)
                    
                break
            if lista_ruleta[0][0] == ' ● ':
                lista_ruleta[0][0] = '   '
                lista_ruleta[0][1] = ' ● '
            else:
                lista_ruleta[0][a] = ' ● '
                lista_ruleta[0][a-1] = '   '
            
            posx = 0
            posy = a

            print("\033[A"*38)
            ruleta()
            sleep(velocidad_rotacion)
        velocidad_vueltas += 0.05
        
        contador1 -= 1
    clear()