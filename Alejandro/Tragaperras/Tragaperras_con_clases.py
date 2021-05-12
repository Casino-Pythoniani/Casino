
import random,time,vlc,playsound
import rueda_traga

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
            rueda_traga.rueda(1,1,1)
            user.Ganar(200)
            print("Has ganado el grande: 200 fichas")
        elif self.azar >= 3 and self.azar <= 12:
            premio.play()
            time.sleep(0.5)
            rueda_traga.rueda(2,2,2)
            user.Ganar(15)
            print("Has ganado: 15 fichas")
        elif self.azar >= 13 and self.azar <= 24:
            premio.play()
            time.sleep(0.5)
            rueda_traga.rueda(3,3,3)
            user.Ganar(5)
            print("Has ganado: 5 fichas")
        else:
            perder.play()
            time.sleep(0.9)
            rueda_traga.aleat()
            print("No has conseguido ninguna ficha")
            perder.stop()
        
    def __str__(self):
        return "Toca: {}".format(self.azar)
        

class usuario:
    def __init__(self,fichas):
        self.fichas = fichas

    def Ganar(self,ganar):
        self.fichas += ganar
        return self.fichas

    def __str__(self):
        return "El jugador tiene {} fichas".format(self.fichas)

def tragaperras_empieza(opcion):
    if jugador.fichas > 4: #Mientras el jugador tenga fichas pregunta
        print("\nPara jugar inserta 5 fichas")
        jugar = str(input("Quieres jugar? (Tecla(Enter) o 'no') "))
        jugar = jugar.lower()

        if jugar == "no":   # Si no quieres jugar dices "no"
            print("Has decidido no jugar a este juego.")
            opcion = int(input("A qué juego quieres ir ahora: "))

        elif jugar != "no" and jugador.fichas > 4: # Si quieres jugar puedes poner cualquier cosa menos "no"
            traga.Toca()
            traga.MasDificil()
            traga.GanaJugador(jugador)
            print(jugador)
    return opcion # Devuelve el valor de "opcion" para que el bucle se mantenga


def pobre(opcion):
    if jugador.fichas <= 0: # Si no te quedan fichas pierdes y te echan del casino
        sin_dinero = vlc.MediaPlayer("sin-dinero.mp3")
        sin_dinero.play()
        print("Has perdido todas tus fichas")
        print("Te van a echar del Casino y vas a morir pobre. O puedes pagar tu deuda con el Casino usando tu cuerpo.")
        opcion = 0
    return opcion

print()
jugador = usuario(100) # El objeto jugador nos permite conocer las fichas que tiene el usuario
print(jugador) # Mostramos la cantidad de fichas que tiene el usuario

traga = juego(100) # El objeto traga crea el juego de la tragaperras y le pasa las posibilidades de ganar

# Has escoguido la TRAGAPERRAS

print("Bienvenido a la Tragaperras") # Aviso para que el jugador sepa que va a perder 2 fichas.
print("Tienes" ,jugador.fichas, "fichas")

opcion = 5
if opcion == 5:
    while opcion == 5: # Mientras la variable opcion sea True el bucle se mantiene
        fondo = vlc.MediaPlayer("fondo.mp3")
        fondo.play()
        opcion = pobre(opcion) # La funcion pobre comprueba si el jugador tiene la cantidad de fichas mínima para jugar.

        # La funcion tragaperras necesita el valor de la opcion para mantener el bucle activo.
        opcion = tragaperras_empieza(opcion)
        time.sleep(0.4)
        fondo.stop()
        
    

