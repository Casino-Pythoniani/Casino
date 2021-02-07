from time import sleep 
import random

nombres_caballos = ['ZeeBullet','Atlantico',"Bannaby's Dream",'Delta Crucis','Run Run','Myaldagoba','Danzing De Saon','Niagara','Lenda Da Torre','Mill Valley','Spinerett']
caballos_a_competir = []        ##En esta lista vacía se añaden 4 nombres de caballos aleatoriamente

def caballos_elegidos():
    while len(caballos_a_competir) != 4:
        validar = random.choice(nombres_caballos)
        if validar not in caballos_a_competir:
            caballos_a_competir.append(validar)

def caballo1(detras):
    delante = 75 - detras 
    print('═'*90+'╦══╗')
    print(' '*detras,'        ,--, ',' '*delante+'║  ║')
    print(' '*detras,'  _ ___/ /\| ',' '*delante+'║  ║')
    print(' '*detras,' ;( )1 , )   ',' '*delante+'║  ║')
    print(' '*detras,'; // ¯¯`--;  ',' '*delante+'║  ║')
    print(' '*detras,'  \     |    ',' '*delante+'║  ║')
    print('═'*90+'╩══╝')

def caballo2(detras):
    delante = 75 - detras 
    print('═'*90+'╦══╗')
    print(' '*detras,'        ,--, ',' '*delante+'║  ║')
    print(' '*detras,'  _ ___/ /\| ',' '*delante+'║  ║')
    print(' '*detras,' ;( )2 , )   ',' '*delante+'║  ║')
    print(' '*detras,'; // ¯¯`--;  ',' '*delante+'║  ║')
    print(' '*detras,'  \     |    ',' '*delante+'║  ║')
    print('═'*90+'╩══╝')

def caballo3(detras):
    delante = 75 - detras 
    print('═'*90+'╦══╗')
    print(' '*detras,'        ,--, ',' '*delante+'║  ║')
    print(' '*detras,'  _ ___/ /\| ',' '*delante+'║  ║')
    print(' '*detras,' ;( )3 , )   ',' '*delante+'║  ║')
    print(' '*detras,'; // ¯¯`--;  ',' '*delante+'║  ║')
    print(' '*detras,'  \     |    ',' '*delante+'║  ║')
    print('═'*90+'╩══╝')

def caballo4(detras):
    delante = 75 - detras 
    print('═'*90+'╦══╗')
    print(' '*detras,'        ,--, ',' '*delante+'║  ║')
    print(' '*detras,'  _ ___/ /\| ',' '*delante+'║  ║')
    print(' '*detras,' ;( )4 , )   ',' '*delante+'║  ║')
    print(' '*detras,'; // ¯¯`--;  ',' '*delante+'║  ║')
    print(' '*detras,'  \     |    ',' '*delante+'║  ║')
    print('═'*90+'╩══╝')

        
def menu_caballos():
    esp1 = 23-len(caballos_a_competir[0])
    esp2 = 23-len(caballos_a_competir[1])
    esp3 = 23-len(caballos_a_competir[2])
    esp4 = 23-len(caballos_a_competir[3])

    linea_vacia="""\t\t\t└─┼───────────────────────────────────┼─┘
    \t\t\t  │                                   │  
    \t\t\t┌─┼───────────────────────────────────┼─┐"""
    
    print('\t\t\t┌─┐                                   ┌─┐')    
    print('\t\t\t│ │BIENVENIDO AL MUNDO DE LAS CARRERAS│ │')
    print('\t\t\t└─┼───────────────────────────────────┼─┘')
    print('\t\t\t  │ En el día de hoy tendremos a los  │\n\t\t\t  │\tsiguientes corredores:        │')
    print('\t\t\t┌─┼───────────────────────────────────┼─┐')
    print('\t\t\t│1│     ',caballos_a_competir[0],esp1*' ','2.00│1│')
    print(linea_vacia)
    print('\t\t\t│2│     ',caballos_a_competir[1],esp2*' ','4.00│2│')
    print(linea_vacia)
    print('\t\t\t│3│     ',caballos_a_competir[2],esp3*' ','6.00│3│')
    print(linea_vacia)
    print('\t\t\t│4│     ',caballos_a_competir[3],esp4*' ','8.00│4│')
    print(linea_vacia)
    print('\t\t\t│ │    La cuota se muestra al lado    │ │')
    print('\t\t\t│ │           del corredor            │ │')
    print('\t\t\t└─┘                                   └─┘')

cuota_caballos2 = 0 + random.choice(range(5,10))

caballos_elegidos()    
while True:
    caballo1()


##while True:
##    detras = detras + 10
##    delante = delante - 10
##    caballo('1')
##    caballo('2')
##    caballo('3')
##    caballo('4')
##    print('\n'*3)
##    sleep(0.4)
##    print('\n'*50)
##    if detras >= 75:
##        break




















