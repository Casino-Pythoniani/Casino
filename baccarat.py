import random
import time
dinero = 100
final = True
pos = [0,1]

while final:
    if dinero == 0 or dinero >= 1000:
        if dinero >= 1000:
            print("\nHas ganado.")
        else:
            print("\nHas perdido.")
        final = False
    else:
        time.sleep (0.5)
        elecc = int(input("\nElige tu posicion (1 por Jugador, 0 por Banco): "))
        if elecc in pos:
            print("\nDinero total: ",dinero)
            time.sleep (0.5)
            apu = int(input("\nDinero a apostar: "))
            time.sleep (0.5)
            if apu <= dinero:
                PP = 0
                time.sleep (2)
                print("\nMano Jugador: ")              
                n1 = random.randrange(2,13)
                n2 = random.randrange(2,13)
                time.sleep (1)
                if n1 > 9:
                    n1 = 0
                elif n2 > 9:
                    n2 = 0
                print("\nPuntos",n1,n2)
                PP = n1 + n2
                if PP > 9:
                    PP = PP - 10
                    time.sleep (2)
                print("\nPuntaje: ",PP)
                PB = 0
                time.sleep (2)
                print("\nMano Banco: ")
                N1 = random.randint(2,13)
                N2 = random.randint(2,13)
                time.sleep (1)
                if N1 > 9:
                    N1 = 0
                elif N2 > 9:
                    N2 = 0
                print("\nPuntos",N1,N2)
                PB = N1 + N2
                if PB > 9:
                    PB = PB -10
                time.sleep (2)
                print("\nPuntaje: ",PB)
                if PP > PB:
                    time.sleep (2)
                    print("\nGanador: Jugador")
                    if elecc == 1:
                        dinero = dinero + apu
                    else:
                        dinero = dinero - apu
                elif PB > PP:
                    time.sleep (2)
                    print("\nGanador: Banco")
                    if elecc == 0:
                        dinero = dinero + apu
                    else:
                        dinero = dinero - apu
                else:
                    print("\nHas empactado")
            else:
                print("\nApuesta invalida")
