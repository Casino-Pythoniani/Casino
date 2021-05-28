
import os
from pynput.keyboard import Listener
from random import randrange
from time import sleep
clear = lambda: os.system('cls') 
#Clase que tiene todas las caracterisiticas del juego
class craps:

    def __init__(self, fichas=500):
        self.dado = {1:['╔═════════╗','║         ║','║    O    ║','║         ║','╚═════════╝'],2:['╔═════════╗','║ O       ║','║         ║','║       O ║','╚═════════╝'],3:['╔═════════╗','║ O       ║','║    O    ║','║       O ║','╚═════════╝']}
        self.fichas = fichas
        self.lista = [' ',' ',' ']
        self.posx=0
        self.ejex=19
        self.ejexx=17
        self.ejey=19
        self.ejeyy=17
        self.ejez=19
        self.ejezz=17
        self.cont=0
        self.comp=True
        self.variable=True
        self.apuestas=0
        self.apu=True
        self.a = randrange(1,7)
        self.b = randrange(1,7)
        self.key=''
        self.casino=500000
    #la funcion apuesta esta creada para que el tablero se adapte a las fichas introducidas 
    def apuesta(self):
        if self.lista[0]!=' ':
            if self.lista[0]>0:
                if self.apuestas<9:
                    self.ejex=19
                    self.ejexx=17
                    self.ejey=19
                    self.ejeyy=17
                    self.ejez=19
                    self.ejezz=17
                if self.apuestas>9:
                    self.ejex=18
                    self.ejexx=17
                    self.ejey=19
                    self.ejeyy=17
                    self.ejez=19
                    self.ejezz=17
                if self.apuestas>99:
                    self.ejex=18
                    self.ejexx=16
                    self.ejey=19
                    self.ejeyy=17
                    self.ejez=19
                    self.ejezz=17
                if self.apuestas>999:
                    self.ejex=17
                    self.ejexx=16
                    self.ejey=19
                    self.ejeyy=17
                    self.ejez=19
                    self.ejezz=17
                if self.apuestas>9999:
                    self.ejex=16
                    self.ejexx=16
        if self.lista[1]!=' ':
            if self.lista[1]>0:
                if self.apuestas<9:
                    self.ejey=19
                    self.ejeyy=17
                    self.ejex=19
                    self.ejexx=17
                    self.ejez=19
                    self.ejezz=17
                if self.apuestas>9:
                    self.ejey=18
                    self.ejeyy=17
                    self.ejex=19
                    self.ejexx=17
                    self.ejez=19
                    self.ejezz=17
                if self.apuestas>99:
                    self.ejey=18
                    self.ejeyy=16
                    self.ejex=19
                    self.ejexx=17
                    self.ejez=19
                    self.ejezz=17
                if self.apuestas>999:
                    self.ejey=17
                    self.ejeyy=16
                    self.ejex=19
                    self.ejexx=17
                    self.ejez=15
                    self.ejezz=21
                if self.apuestas>9999:
                    self.ejey=16
                    self.ejeyy=16
        if self.lista[2]!=' ':
            if self.lista[2]>0:
                if self.apuestas<9:
                    self.ejey=19
                    self.ejeyy=17
                    self.ejex=19
                    self.ejexx=17
                    self.ejez=19
                    self.ejezz=17
                if self.apuestas>9:
                    self.ejey=19
                    self.ejeyy=17
                    self.ejex=19
                    self.ejexx=17
                    self.ejez=19
                    self.ejezz=16
                if self.apuestas>99:
                    self.ejey=20
                    self.ejeyy=16
                    self.ejex=19
                    self.ejexx=17
                    self.ejez=18
                    self.ejezz=16
                if self.apuestas>999:
                    self.ejey=20
                    self.ejeyy=16
                    self.ejex=19
                    self.ejexx=17
                    self.ejez=18
                    self.ejezz=15
                if self.apuestas>9999:
                    self.ejez=17
                    self.ejezz=15
    #la funcion tablero printea el tablero,con sus correspondientes ejes eje x,y,z para que se adapte a las fichas 
    def tablero(self):

        clear()
        print("\n"+"\n"+
        " "*45+"FICHAS =",self.fichas," "*30+"CASINO =",self.casino,"\n"+"\n"+
        " "*47+"Presione la tecla h para acceder al menu de instrucciones\n"+"\n"
        "╔"+"═"*40+"╗"+" "*12+"╔"+"═"*40+"╗"+" "*14+"╔"+"═"*40+"╗\n"
        "║"+" "*16+"JUGADOR"+" "*17+"║"+" "*12+"║"+" "*18+"CRAPS"+" "*17+"║"+" "*14+"║"+" "*18+"BANCA"+" "*17+"║\n"+
        "╠"+"═"*40+"╣"+" "*11+" "+"╠"+"═"*40+"╣"+" "*13+" "+"╠"+"═"*40+"╣\n"
        "║"+" "*40+"║"+" "*11+" "+"║"+" "*40+"║"+" "*13+" "+"║"+" "*40+"║\n"
        "║"+" "*3+"╔══ ╔══╗ ╔══╗ ╔╗╔╗      ══╗"+" "*10+"║"+" "*12+"║"+" "*9+"╔═╗ ╔══╗ ╔══╗ ║   ╔══ "+" "*9+"║"+" "*14+"║"+" "*3+"╔══ ╔══╗ ╔══╗ ╔╗╔╗      ══╗"+" "*10+"║\n"+
        "║"+" "*3+"╠═  ╠══╣ ║  ║ ║╚╝║      ╔═╝"+" "*10+"║"+" "*12+"║"+" "*9+"║ ║ ║  ║ ╠══╣ ║   ╠══ "+" "*9+"║"+" "*14+"║"+" "*3+"╠═  ╠══╣ ║  ║ ║╚╝║        ║"+" "*10+"║\n"+
        "║"+" "*3+"║   ║  ╚ ╚══╝ ╝  ╚      ╚══"+" "*10+"║"+" "*12+"║"+" "*9+"╚═╝ ╚══╝ ╚══╝ ╚══ ╚══ "+" "*9+"║"+" "*14+"║"+" "*3+"║   ║  ╚ ╚══╝ ╝  ╚        ║"+" "*10+"║\n"+
        "║"+" "*40+"║"+" "*11+" "+"║"+" "*40+"║"+" "*13+" "+"║"+" "*40+"║\n"
        "║"+" "*10+"   ══╦══  ╔══╗     ╔══"+" "*8+"║"+" "*12+"║"+" "*18+ "╔══"+" "*19+"║"+" "*14+"║"+" "*9+"   ══╦══  ╔══╗     ═╗ ═╗"+" "*7+"║\n"+
        "║"+" "*10+"     ║    ║  ║     ╠══╗"+" "*7+"║"+" "*12+"║"+" "*18+"╠══╗"+" "*18+"║"+" "*14+"║"+" "*11+"   ║    ║  ║      ║  ║"+" "*7+"║\n"+
        "║"+" "*10+"     ║    ╚══╝     ╚══╝"+" "*7+"║"+" "*12+"║"+" "*18+"╚══╝"+" "*18+"║"+" "*14+"║"+" "*11+"   ║    ╚══╝      ║  ║"+" "*7+"║\n"+
        "║"+" "*40+"║"+" "*12+"║"+" "*40+"║" +" "*14+"║"+" "*40+"║\n"
        "╠"+"═"*40+"╣"+" "*12+"╠"+"═"*40+"╣" +" "*14+"╠"+"═"*40+"╣\n"
        "║"+" "*self.ejex,self.lista[0]," "*self.ejexx,"║"+" "*12+"║"+" "*self.ejey,self.lista[1]," "*self.ejeyy,"║"+" "*14+"║"+" "*self.ejez,self.lista[2]," "*self.ejezz,"║\n"
        "╚"+"═"*40+"╝"+" "*12+"╚"+"═"*40+"╝" +" "*14+"╚"+"═"*40+"╝\n")
    #la funcion info printea informacion sobre como jugar al juego y como realizar las apuestas
    def info(self):
        print(
        "╔"+"═"*40+"╗\n"
        "║"+" "*14+"COMO APOSTAR"+" "*14+"║\n"
        "╠"+"═"*40+"╣\n"
        "║"+" "*40+"║\n"
        "║"+" "*2+"Q=1"+" "*6+" "+"W=5"+" "*6+" "+"E=25"+" "*6+" "+"R=100"+" "*2+"║\n"
        "║"+" "*40+"║\n"
        "╠"+"═"*40+"╣\n"
        "║"+" "*40+"║\n"
        "║"+" "*5+"Una vez realizada la apuesta "+" "*6+"║\n"
        "║"+" "*40+"║\n"
        "║"+" "*4+"presione la tecla Enter-Intro"+" "*7+"║\n"
        "║"+" "*40+"║\n"
        "║"+" "*8+"para comenzar el juego"+" "*10+"║\n"
        "║"+" "*40+"║\n"
        "╠"+"═"*40+"╣\n"
        "║"+" "*40+"║\n"
        "║"+" "*3+"Use para desplazarse   <-         ->"+" "*3+"║\n"
        "║"+" "*40+"║\n"
        "╚"+"═"*40+"╝")

    #la funcion tirar dado como su nombre indica tira dos dados que muestra por pantalla y coge el valor de su suma,ademas de esto compara su suma con el reglamento del juego y comprueba si has ganado o no
    def tirar_dado(self): # ┌ ┐ │ └ ┘ ─   「 」 ﹁ ﹂

        self.dado = {
            1:['┏━━━━━━━┓','┃           ┃','┃     ■     ┃','┃           ┃','┗━━━━━━━┛'],
            2:['┏━━━━━━━┓','┃  ■        ┃','┃           ┃','┃        ■  ┃','┗━━━━━━━┛'],
            3:['┏━━━━━━━┓','┃  ■        ┃','┃     ■     ┃','┃        ■  ┃','┗━━━━━━━┛'],
            4:['┏━━━━━━━┓','┃  ■     ■  ┃','┃           ┃','┃  ■     ■  ┃','┗━━━━━━━┛'],
            5:['┏━━━━━━━┓','┃  ■     ■  ┃','┃     ■     ┃','┃  ■     ■  ┃','┗━━━━━━━┛'],
            6:['┏━━━━━━━┓','┃  ■     ■  ┃','┃  ■     ■  ┃','┃  ■     ■  ┃','┗━━━━━━━┛'],}
        
        for i in range(4):
            self.tablero()
            a = randrange(1,7)
            b = randrange(1,7)
            for i in range(5):
                print("\t"*5+self.dado[a][i]+"\t"*5+self.dado[b][i])
            sleep(0.5)
            
        if a+b==12:
            print("CRAPS")
            if self.lista[1]==self.apuestas:
                self.apuestas*=1000
                self.fichas+=self.apuestas
                self.casino-=self.apuestas
            else:
                self.casino+=self.apuestas
        if a+b<=6:
            print("Gana jugador")
            if self.lista[0]==self.apuestas:
                self.apuestas*=2 
                self.fichas+=self.apuestas
                self.casino-=self.apuestas
            else:
                self.casino+=self.apuestas
        if a+b>6 and a+b<12:
            print("Gana banca")
            if self.lista[2]==self.apuestas:
                self.apuestas*=2 
                self.fichas+=self.apuestas
                self.casino-=self.apuestas
            else:
                self.casino+=self.apuestas
        sleep(3)
        self.apuestas=0
        self.ejex=19
        self.ejexx=17
        self.ejey=19
        self.ejeyy=17
        self.ejez=19
        self.ejezz=17
        self.comp=True
        
    #funcion que se dedica a leer las teclas de tu teclado con ella leemos el teclado y realizamos apuestas navegamos por el juego etc...
    def key_recorder(self,key):
        self.key=str(key).replace("'", "")
        if self.key=="h" and self.cont<1:
            self.cont+=1
            self.info()
        
        else:
            self.cont=0
            l.stop()
        if self.fichas>0 and self.apuestas<10000:
            if self.apu==False:
                if self.key=='q':
                    self.apuestas+=1
                    self.fichas-=1
                if self.key=='w':
                    self.apuestas+=5
                    self.fichas-=5
                if self.key=='e':
                    self.apuestas+=25
                    self.fichas-=25
                if self.key=='r':
                    self.apuestas+=100
                    self.fichas-=100
            if self.apuestas>0 and self.key=="Key.enter":
                self.tirar_dado()
            if self.posx>3:
                self.posx=3
            if self.posx<1:
                self.posx=0
            if self.key=='Key.right' and self.comp==True:
                self.posx+=1
                self.apu=False
            if self.key=='Key.left' and self.comp==True:
                self.posx-=1
                self.apu=False
            if self.posx==1:
                if self.comp==True:
                    self.lista[1]=' '
                    self.lista[2]=' '
                    self.lista[0]=self.apuestas
            if self.lista[0]!=" ":
                if self.lista[0]>0:
                    self.pos=1
                    self.comp=False
                    self.lista[0]=self.apuestas

            if self.posx==2:
                if self.comp==True:
                    self.lista[2]=' '
                    self.lista[0]=' '
                    self.lista[1]=self.apuestas
                if self.lista[1]!=' ':
                    if self.lista[1]>0:
                        self.pos=2
                        self.comp=False
                        self.lista[1]=self.apuestas

            if self.posx==3:
                if self.comp==True:
                    self.lista[1]=' '
                    self.lista[0]=' '
                    self.lista[2]=self.apuestas
                if self.lista[2]!=' ':
                    if self.lista[2]>0 :
                        self.comp=False
                        self.lista[2]=self.apuestas



def ejecutar_dados(fichas):
    juego=craps(fichas)
    #el bucle while sirve para las funciones de limpiado del tablero y una vez se rompe se sale del programa
    while juego.key!= "Key.esc":
        juego.apuesta()
        juego.tablero()
        global l
        with Listener(on_press=juego.key_recorder) as l:
            l.join()
        clear()
    return juego.fichas


#ejecutar_dados(500)























        
