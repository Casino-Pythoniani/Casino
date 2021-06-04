
import random
#from playsound import playsound

# Las intrucciones para imprimir las imagenes del tragaperras.
# Flata implementarla en el tragaperras como un modulo.

def rueda(pri,seg,ter): # Requerimos de 3 valores para sacar las imagenes.
    print("\t\t\t ╔" + "═"*11 + "╗\t ╔" + "═"*11 + "╗\t ╔" + "═"*11 + "╗") # primera linea
    for x in range(6): # Bucle for para sacar la imagen entera
        print("\t\t\t",dicc[pri][x],"\t",dicc[seg][x],"\t",dicc[ter][x]) 
    print("\t\t\t ╚" + "═"*11 + "╝\t ╚" + "═"*11 + "╝\t ╚" + "═"*11 + "╝") # ultima linea

# El bucle usa los numeros para imprimir la variable del diccionario.
# Ejemplo: diccionario con clave[1] y valor numerico[0] imprime la variable (0) de la clave (1)
# Explicación: Le damos un valor que la funcion recoge como una clave del diccionario y este imprime la imagen.

def aleat(): # Una función para mostrar aleatoriamente las imagenes que te da el juego.
    # Los valores se dan de esta forma debido a que no se puede hacer usando un bucle.
    pri=random.randint(1,3) 
    seg=random.randint(1,3)
    ter=random.randint(1,3)
    if pri==seg==ter: # Valida si todos las imagenes son iguales.
        seg += 1 # Le suma 1 al valor de la segunda imagen, para que sea diferente del resto.
        if seg not in dicc: # Si el valor de la segunda imagen no esta asociado a ninguna clave del diccionario hace esta acción.
            seg -= 2 # Le resta 2 al valor de la segunda imagen, para que sea diferente del resto.
    rueda(pri,seg,ter) # Llama a la función que muestra las imagenes.
    return


# Lista para mostrar un diamante
diamante=["║ " + "╔"+"═"*7+"╗"+ " ║","║ " + "╚╗"+" "*5+"╔╝" + " ║","║  " + "╚╗"+" "*3+"╔╝" + "  ║","║   " + "╚╗"+" "+"╔╝" "   ║","║    " + "╚"+"═"+"╝" + "    ║","║" + " "*11 + "║"]

# Lista para mostrar una fresa
fresa=["║ " + " "*5+"╔═╗" + "  ║","║ " + "╔"+"═"*4+"╝ ╚╗" + " ║","║ " + "║"+" "*5+"╔═╝" + " ║","║ " +"║"+" "*5+"║" + "   ║","║ " +"╚"+"═"*5+"╝" + "   ║","║" + " "*11 + "║"]

# Lista para mostrar otra imagen
otro=["║ "+"╗"+" "*7+"╔"+" ║","║ "+"╚═╗"+" "*3+"╔═╝"+" ║","║   "+"╚═╗"+"═╝"+" "*2+" ║","║   "+"╔═╝"+"═╗"+" "*2+" ║","║ "+"╔═╝"+" "*3+"╚═╗"+" ║","║ "+"╝"+" "*7+"╚"+" ║"]

dicc={1:diamante,2:fresa,3:otro}


rueda(1,2,3)
aleat()
# playsound(musica.mp3) #Importa el módulo playsound usando el fichero musica.mp3









