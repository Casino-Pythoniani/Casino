
# CASINO
# Necesitamos un menú para escoger el juego que queremos jugar
# Necesitamos un contador con la cantidad de dinero que tienes
# Cuando ganas en los juegos obtienes dinero.
# Una tragaperras con al menos un 1% de probabilidades en base a 100.(1%/100%)
# Un Black Jack de cartas.
import random, rueda_traga, time

# Aún hay cosas que aclarar, como las posibilidades, el dinero que se gana por los premios, un contador que he metido, etc.

# He metido todo el programa en funciones para facilidad de uso e implementación en el proyecto final.

def juego(dinero,cont,posibilidades): # Función para comenzar el juego
    print("posibilidades de entre:" ,posibilidades)
    if dinero > 0:  #Mientras el jugador tenga dinero pregunta
        jugar = str(input("\nQuieres jugar? (Tecla(Enter) o 'no') "))
        if jugar == "no":   # Si no quieres jugar dices "no"
            print("Has decidido no jugar a este juego.")
            opcion = int(input("A qué juego quieres ir ahora: "))
            
        elif jugar != "no" and dinero > 0: # Si quieres jugar puedes poner cualquier cosa menos "no"
            dinero -= 2 # Pierdes 2 euros
            cont += 1
            posibilidades += 1 # (opcional) tus posibilidades de ganar algo se reducen un poco
            ganar = random.randint(1,posibilidades)
            if ganar == 80: # Probabilidades del 0.8%
                #time.sleep(1) tiempo hasta saber si ganas
                rueda_traga.rueda(1,1,1) # Llamamos al módulo para poder ver lo que toca
                print("Has ganado el grande: 200€")
                dinero += 200

            elif ganar <= 16: # Probabilidades del 12.8%
                #time.sleep(1)
                rueda_traga.rueda(3,3,3)
                print("Has ganado: 5€")
                dinero += 5

            elif ganar >= 17 and ganar <= 23: # Probabilidades del 4%
                #time.sleep(1)
                rueda_traga.rueda(2,2,2)
                print("Has ganado: 10€")
                dinero += 10
                
            else: # Si el random da cualquier otra cosa que no sea 1 imprime esto
                #time.sleep(1)
                rueda_traga.aleat() # Llamamos al modulo para ver las imágenes aleatorias
                print("No has ganado nada, vuelve a intentarlo.")
            print("Ahora tienes" ,dinero, "€")
                
    return dinero,cont,posibilidades # Devuelve los valores para seguir la autoincrementación de estos

def pobre(dinero, opcion):
    if dinero <= 0: # Si no te queda dinero pierdes y te echan del casino
        print("Has perdido todo tu dinero")
        print("Te han echado del Casino y vas a morir pobre.")
        opcion = 0
    return opcion

cont= 0     # El número de veces que has jugado en total.(por decidir)
dinero = 50    # El dinero que tienes
posibilidades = 79  # El valor original de las posibilidades
tragaperras = True

# Has escoguido la TRAGAPERRAS

print("""Opciones:  5.tragaperras.5""")
        
print("Tienes" ,dinero, "€")
opcion = 5
if opcion == 5:
    while opcion == 5: # Mientras la variable tragaperras sea True el bucle se mantiene
        opcion = pobre(dinero, opcion)
        
        dinero,cont,posibilidades = juego(dinero,cont,posibilidades)
    print("Has jugado" ,cont, "veces")
        


            


