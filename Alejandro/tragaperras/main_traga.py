
# Programa creado por Alejandro Ruiz de la Asunción
import random,time,vlc,playsound
from Alejandro.tragaperras.rueda_traga import *
from pynput.keyboard import Listener

class juego:
    def __init__(self,probs):
        self.probs = probs
        self.azar = self.Toca()

    def Toca(self):
        self.azar = random.randint(1,self.probs)
        return self.azar

    def MasDificil(self):
        self.probs += 2
        return self.probs

    def GanaJugador(self,user):
        premio = vlc.MediaPlayer("premio.mp3")
        grande = vlc.MediaPlayer("grande.mp3")
        perder = vlc.MediaPlayer("perder.mp3")
        user.fichas -= 5
        if self.azar <= 2:
            grande.play()
            time.sleep(0.5)
            rueda(1,1,1)
            user.Ganar(200)
            print("\t\t\tHas ganado el grande: 200 fichas")
        elif self.azar >= 3 and self.azar <= 12:
            premio.play()
            time.sleep(0.5)
            rueda(2,2,2)
            user.Ganar(15)
            print("\t\t\tHas ganado: 15 fichas")
        elif self.azar >= 13 and self.azar <= 23:
            premio.play()
            time.sleep(0.5)
            rueda(3,3,3)
            user.Ganar(5)
            print("\t\t\tHas ganado: 5 fichas")
        else:
            perder.play()
            time.sleep(0.9)
            aleat()
            print("\t\t\tNo has conseguido ninguna ficha")
            perder.stop()

class usuario:
    def __init__(self,fichas):
        self.fichas = fichas

    def Ganar(self,ganar):
        self.fichas += ganar
        return self.fichas

    def __str__(self):
        return "\t\t\tEl jugador tiene {} fichas\n".format(self.fichas)
       
def tragaperras_empieza(jugador,traga):
    if jugador.fichas > 4: #Mientras el jugador tenga fichas pregunta
        traga.Toca()
        traga.MasDificil()
        traga.GanaJugador(jugador)
        print(jugador)
    return jugador.fichas
    # Devuelve el valor de"jugador.fichas" y "opcion" para que el bucle se mantenga y poder
    # poder sacar la cantidad de fichas del jugador a el programa que compila los juegos


def pobre(fichas):
    if fichas <= 0: # Si no te quedan fichas pierdes y te echan del casino
        sin_dinero = vlc.MediaPlayer("sin-dinero.mp3")
        sin_dinero.play()
        print("\n\t\tHas perdido todas tus fichas")
        print("\tTe van a echar del Casino y vas a morir pobre. O puedes pagar tu deuda con el Casino usando tu cuerpo.")
    
    
def funcion_traga(fichas):
    print()
    jugador = usuario(fichas) # El objeto jugador nos permite conocer las fichas que tiene el usuario
    traga = juego(100) # El objeto traga crea el juego de la tragaperras y le pasa las posibilidades de ganar

    fondo = vlc.MediaPlayer("fondo.mp3")
    fondo.play()
    
    fichas = tragaperras_empieza(jugador,traga) # La funcion devuelve el valor de las fichas que tiene el jugador
    time.sleep(0.4)
    fondo.stop()
    return fichas

def key_recorder(key):
    global tecla
    key = str(key).replace("'","")
    if key == "Key.esc":
        tecla = key
        exit
        
    elif key == "Key.enter":
        tecla = key

    else:
        tecla = key
        
    t.stop()

def menu(fichas):
    print("""
╔══════════════╗                                                                         ╔══════════════╗
║ SALIR  (ESC) ║                                                                         ║ FICHAS:""",fichas,"""\t║
╚══════════════╝                                                                         ╚══════════════╝

              ┬┌┐ ┐┌──┌─┐┌─┐─┬─┌─┐   ┌──   ┌─┐┬┌─┐┬ ┬┌─┐┌─┐   ┌─┐┌─┐┌─┐┌─┐   ┌┬┐┬ ┬┌─┐┌─┐┬─┐
              ││└┐│└─┐├┤ ├┬┘ │ ├┤    └─┐   ├─ ││  ├─┤├─┤└─┐   ├─┘├─┤├┬┘├─┤    │ │ ││ ┬├─┤├┬┘
              ┴└ └┘└─┘└─┘┴└─ ┴ └─┘   └─┘   ┴  ┴└─┘┴ ┴┴ ┴└─┘   ┴  ┴ ┴┴└─┴ ┴   ─┘ └─┘└─┘┴ ┴┴└─

                              ╔═════════════════════════════════════════╗
                              ║          ┌┬┐┬ ┬┌─┐┌─┐┬─┐┌─┐             ║
                              ║           │ │ ││ ┬├─┤├┬┘ ┌┘             ║
                              ║          ─┘ └─┘└─┘┴ ┴┴└─ .     (ENTER)  ║
                              ╚═════════════════════════════════════════╝
    """)

def bienvenido():
    print("""
             ┬─┐┬┌─┐┌┐ ┐┬  ┬┌─┐┌┐ ┐┬ ┬─┐┌─┐   ┌─┐   ┬  ┌─┐   ─┬─┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐
             ├─┤│├┤ │└┐│└┐┌┘├┤ │└┐││ │ ││ │   ├─┤   │  ├─┤    │ ├┬┘├─┤│ ┬├─┤├─┘├┤ ├┬┘├┬┘├─┤└─┐
             ┴─┘┴└─┘└ └┘ └┘ └─┘└ └┘┴ ┴─┘└─┘   ┴ ┴   ┴─┘┴ ┴    ┴ ┴└─┴ ┴└─┘┴ ┴┴  └─┘┴└─┴└─┴ ┴└─┘

""")

def teclado(fichas):
    menu(fichas)
    global t
    with Listener(on_press=key_recorder) as t:
        t.join()
        if tecla == "Key.esc":
            return tecla,fichas

        elif tecla == "Key.enter":
            fichas = funcion_traga(fichas)
            
        return tecla,fichas

def ejecutar_traga(fichas=50,tecla=""):
    bienvenido()
    while tecla != "Key.esc" and fichas != 0:
        tecla,fichas = teclado(fichas)
        pobre(fichas)
    return fichas    

#ejecutar_traga()




