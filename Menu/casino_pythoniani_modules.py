import os

from Menu.casino_pythoniani_ascii import *
clear = lambda: os.system('cls') 
from pynput.keyboard import Listener

posx = 0
posy = 0
tecla = ""

def key_recorder(key):
    global posx
    global posy
    global juego
    global tecla
    juego = ""

    key = str(key).replace("'", "")

    if key == 'Key.right' and posx != 3:
        posx += 1

    elif key == 'Key.left' and posx != 0:
        posx -= 1
    
    elif key == 'Key.down' and posy != 1:
        posy += 1

    elif key == 'Key.up' and posy != 0:
        posy -= 1
    
    elif key == 'Key.enter':
        if posx == 0 and posy == 0:
            juego = 'ruleta'
        elif posx == 1 and posy == 0:
            juego =  'bingo'
        elif posx == 2 and posy == 0:
            juego = 'dados'
        elif posx == 3 and posy == 0:
            juego = 'caballos'
        elif posx == 0 and posy == 1:
            juego = 'blackjack'
        elif posx == 1 and posy == 1:
            juego = 'traga'
        elif posx == 2 and posy == 1:
            juego = 'poker'
        elif posx == 3 and posy == 1:
            juego = 'baccarat'

    elif key == "Key.esc":
        tecla = key

    l.stop()

def display_menu_casino(fichas): ##ascii:│ ┼ ─ ┬ ┴ ┘ └ ├ ┤ ┌ ┐  ║ ╔ ═ ╗ ╚ ╝ ╞  ▤
    clear()
    global posx
    global posy
    
    #SIN SELECCIONAR
    ruleta = ['┌──────────────────────────────┐','│┌┬┬┬┬┬┬┬┬┬┬┬┬─┬─┬─┬─┬─┬─┬─┬─┐ │','│├           ┼─┼─┼─┼─┼─┼─┼─┼─┤ │',
              '│├     ┼     ┼─┼─┼─┼─┼─┼─┼─┼─┤ │','│├           ┼─┼─┼─┼─┼─┼─┼─┼─┤ │','│└┴┴┴┴┴┴┴┴┴┴┴┴─┴─┴─┴─┴─┴─┴─┴─┘ │',
              '│                              │','└──────────────────────────────┘']
    bingo = ['┌──────────────────────────────┐','│ ┌┬┬┬┬┬┬┐  ┌┬┬┬┬┬┬┐  ┌┬┬┬┬┬┬┐ │','│ ├┼┼┼┼┼┼┤  ├┼┼┼┼┼┼┤  ├┼┼┼┼┼┼┤ │',
             '│ └┴┴┴┴┴┴┘  └┴┴┴┴┴┴┘  └┴┴┴┴┴┴┘ │','│ ┌┬┬┬┬┬┬┐  ┌┬┬┬┬┬┬┐  ┌┬┬┬┬┬┬┐ │','│ ├┼┼┼┼┼┼┤  ├┼┼┼┼┼┼┤  ├┼┼┼┼┼┼┤ │',
             '│ └┴┴┴┴┴┴┘  └┴┴┴┴┴┴┘  └┴┴┴┴┴┴┘ │','└──────────────────────────────┘']
    dados = ['┌──────────────────────────────┐','│   ┏━━━━━━━━━━━┓              │','│   ┃  ■     ┏━━━━━━━━━━━┓     │',
             '│   ┃        ┃  ■     ■  ┃     │','│   ┃  ■     ┃     ■     ┃     │','│   ┗━━━━━━━━┃  ■     ■  ┃     │',
             '│            ┗━━━━━━━━━━━┛     │','└──────────────────────────────┘']
    caballos = ['┌──────────────────────────────┐','│          ,--,          ,--,  │','│    _ ___/ /\|   _ ___/ /\|   │',
                '│  ;( )2 , )    ;( )1 , )      │','│ ; // ¯¯`--;  ; // ¯¯`--;     │','│   \     |      \     |       │',
                '│                              │','└──────────────────────────────┘']
    blackjack = ['┌──────────────────────────────┐','│           ┌──────┐           │','│           │      │           │',
                 '│           └──────┘           │','│   ┌─┐┌─┐            ┌─┐┌─┐   │','│   └─┘└─┘   ┌─┐┌─┐   └─┘└─┘   │',
                 '│            └─┘└─┘            │','└──────────────────────────────┘']
    traga = ['┌──────────────────────────────┐','│    ┌───────────────────┐     │','│    │┌───┐  ┌───┐  ┌───┐│     │',
             '│    ││BAR│  │ ☼ │  │ ☼ ││     │','│    ││ ☼ │  │BAR│  │BAR││     │','│    │└───┘  └───┘  └───┘│     │',
             '│    └───────────────────┘     │','└──────────────────────────────┘']
    poker = ['┌──────────────────────────────┐','│ ┌──┤_├───┤_├───┤_├───┤_├───┐ │','│ │  # #   # #   # #   # #   │ │',
             '│ │     ┌─┐┌─┐┌─┐┌─┐┌─┐      │ │','│ │     └─┘└─┘└─┘└─┘└─┘      │ │','│ │  #_#   #_#   #_#   #_#   │ │',
             '│ └──┤_├───┤_├───┤_├───┤_├───┘ │','└──────────────────────────────┘']
    baccarat = ['┌──────────────────────────────┐','│ ┌────────────┬┬────────────┐ │','│ │   PLAYER   ││   BANKER   │ │',
                '│ │            ││            │ │','│ │ 1 2 3 4 5  ││  6 7 8 9   │ │','│ │            ││            │ │',
                '│ └────────────┴┴────────────┘ │','└──────────────────────────────┘']
    
    #SELECIONADOS
    ruleta_s = ['■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■','█┌┬┬┬┬┬┬┬┬┬┬┬┬─┬─┬─┬─┬─┬─┬─┬─┐ █','█├           ┼─┼─┼─┼─┼─┼─┼─┼─┤ █',
              '█├     ┼     ┼─┼─┼─┼─┼─┼─┼─┼─┤ █','█├           ┼─┼─┼─┼─┼─┼─┼─┼─┤ █','█└┴┴┴┴┴┴┴┴┴┴┴┴─┴─┴─┴─┴─┴─┴─┴─┘ █',
              '█                              █','■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■']
    bingo_s = ['■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■','█ ┌┬┬┬┬┬┬┐  ┌┬┬┬┬┬┬┐  ┌┬┬┬┬┬┬┐ █','█ ├┼┼┼┼┼┼┤  ├┼┼┼┼┼┼┤  ├┼┼┼┼┼┼┤ █',
             '█ └┴┴┴┴┴┴┘  └┴┴┴┴┴┴┘  └┴┴┴┴┴┴┘ █','█ ┌┬┬┬┬┬┬┐  ┌┬┬┬┬┬┬┐  ┌┬┬┬┬┬┬┐ █','█ ├┼┼┼┼┼┼┤  ├┼┼┼┼┼┼┤  ├┼┼┼┼┼┼┤ █',
             '█ └┴┴┴┴┴┴┘  └┴┴┴┴┴┴┘  └┴┴┴┴┴┴┘ █','■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■']
    dados_s = ['■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■','█   ┏━━━━━━━━━━━┓              █','█   ┃  ■     ┏━━━━━━━━━━━┓     █',
             '█   ┃        ┃  ■     ■  ┃     █','█   ┃  ■     ┃     ■     ┃     █','█   ┗━━━━━━━━┃  ■     ■  ┃     █',
             '█            ┗━━━━━━━━━━━┛     █','■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■']
    caballos_s = ['■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■','█          ,--,          ,--,  █','█    _ ___/ /\|   _ ___/ /\|   █',
                '█  ;( )2 , )    ;( )1 , )      █','█ ; // ¯¯`--;  ; // ¯¯`--;     █','█   \     |      \     |       █',
                '█                              █','■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■']
    blackjack_s = ['■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■','█           ┌──────┐           █','█           │      │           █',
                 '█           └──────┘           █','█   ┌─┐┌─┐            ┌─┐┌─┐   █','█   └─┘└─┘   ┌─┐┌─┐   └─┘└─┘   █',
                 '█            └─┘└─┘            █','■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■']
    traga_s = ['■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■','█    ┌───────────────────┐     █','█    │┌───┐  ┌───┐  ┌───┐│     █',
             '█    ││BAR│  │ ☼ │  │ ☼ ││     █','█    ││ ☼ │  │BAR│  │BAR││     █','█    │└───┘  └───┘  └───┘│     █',
             '█    └───────────────────┘     █','■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■']
    poker_s = ['■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■','█ ┌──┤_├───┤_├───┤_├───┤_├───┐ █','█ │  # #   # #   # #   # #   │ █',
             '█ │     ┌─┐┌─┐┌─┐┌─┐┌─┐      │ █','█ │     └─┘└─┘└─┘└─┘└─┘      │ █','█ │  #_#   #_#   #_#   #_#   │ █',
             '█ └──┤_├───┤_├───┤_├───┤_├───┘ █','■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■']
    baccarat_s = ['■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■','█ ┌────────────┬┬────────────┐ █','█ │   PLAYER   ││   BANKER   │ █',
                '█ │            ││            │ █','█ │ 1 2 3 4 5  ││  6 7 8 9   │ █','█ │            ││            │ █',
                '█ └────────────┴┴────────────┘ █','■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■']

    titulo_casino_pythoniani(fichas)
    #PARTE DE ARRIBA
    if posx == 0 and posy == 0:
        for i in range(8):
            print(ruleta_s[i],' '*6,bingo[i],' '*6,dados[i],' '*6,caballos[i])
        print('\n')
        for i in range(8):
            print(blackjack[i],' '*6,traga[i],' '*6,poker[i],' '*6,baccarat[i])
        titulo_ruleta()
    
    if posx == 1 and posy == 0:
        for i in range(8):
            print(ruleta[i],' '*6,bingo_s[i],' '*6,dados[i],' '*6,caballos[i])
        print('\n')
        for i in range(8):
            print(blackjack[i],' '*6,traga[i],' '*6,poker[i],' '*6,baccarat[i])
        titulo_bingo()
    
    if posx == 2 and posy == 0:
        for i in range(8):
            print(ruleta[i],' '*6,bingo[i],' '*6,dados_s[i],' '*6,caballos[i])
        print('\n')
        for i in range(8):
            print(blackjack[i],' '*6,traga[i],' '*6,poker[i],' '*6,baccarat[i])
        titulo_dados()
    
    if posx == 3 and posy == 0:
        for i in range(8):
            print(ruleta[i],' '*6,bingo[i],' '*6,dados[i],' '*6,caballos_s[i])
        print('\n')
        for i in range(8):
            print(blackjack[i],' '*6,traga[i],' '*6,poker[i],' '*6,baccarat[i])
        titulo_caballos()

    #PARTE DE ABAJO
    if posx == 0 and posy == 1:
        for i in range(8):
            print(ruleta[i],' '*6,bingo[i],' '*6,dados[i],' '*6,caballos[i])
        print('\n')
        for i in range(8):
            print(blackjack_s[i],' '*6,traga[i],' '*6,poker[i],' '*6,baccarat[i])
        titulo_blackjack()
    
    if posx == 1 and posy == 1:
        for i in range(8):
            print(ruleta[i],' '*6,bingo[i],' '*6,dados[i],' '*6,caballos[i])
        print('\n')
        for i in range(8):
            print(blackjack[i],' '*6,traga_s[i],' '*6,poker[i],' '*6,baccarat[i])
        titulo_traga()
    
    if posx == 2 and posy == 1:
        for i in range(8):
            print(ruleta[i],' '*6,bingo[i],' '*6,dados[i],' '*6,caballos[i])
        print('\n')
        for i in range(8):
            print(blackjack[i],' '*6,traga[i],' '*6,poker_s[i],' '*6,baccarat[i])
        titulo_poker()
    
    if posx == 3 and posy == 1:
        for i in range(8):
            print(ruleta[i],' '*6,bingo[i],' '*6,dados[i],' '*6,caballos[i])
        print('\n')
        for i in range(8):
            print(blackjack[i],' '*6,traga[i],' '*6,poker[i],' '*6,baccarat_s[i])
        titulo_baccarat()
        

def ejecutar_menu_casino(fichas):
    global l
    display_menu_casino(fichas)
    with Listener(on_press=key_recorder) as l:
        l.join()
    return juego,tecla



 
   
   
