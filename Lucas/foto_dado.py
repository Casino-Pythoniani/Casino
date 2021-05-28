
from random import randrange

dado = {
1:['┏━━━━━━━┓','┃           ┃','┃     ■     ┃','┃           ┃','┗━━━━━━━┛'],
2:['┏━━━━━━━┓','┃  ■        ┃','┃           ┃','┃        ■  ┃','┗━━━━━━━┛'],
3:['┏━━━━━━━┓','┃  ■        ┃','┃     ■     ┃','┃        ■  ┃','┗━━━━━━━┛'],
4:['┏━━━━━━━┓','┃  ■     ■  ┃','┃           ┃','┃  ■     ■  ┃','┗━━━━━━━┛'],
5:['┏━━━━━━━┓','┃  ■     ■  ┃','┃     ■     ┃','┃  ■     ■  ┃','┗━━━━━━━┛'],
6:['┏━━━━━━━┓','┃  ■     ■  ┃','┃  ■     ■  ┃','┃  ■     ■  ┃','┗━━━━━━━┛'],}


for i in range(4):
    a = randrange(1,7)
    b = randrange(1,7)

    for i in range(5):
        print("\t"+dado[a][i]+"\t"*4+dado[b][i])

    print("a=",a,"b=",b)
    
if a==b and a+b==12:
    print("CRAPS")
##    if self.lista[1]==self.apuestas:
##        self.apuestas*=1000
##        self.fichas+=self.apuestas
##        self.casino-=self.apuestas
##    else:
##        self.casino+=self.apuestas
if a+b<=6:
    print("Gana jugador")
##    if self.lista[0]==self.apuestas:
##        self.apuestas*=2 
##        self.fichas+=self.apuestas
##        self.casino-=self.apuestas
##    else:
##        self.casino+=self.apuestas
if a+b>6 and a+b<12:
    print("Gana banca")
##    if self.lista[2]==self.apuestas:
##        self.apuestas*=2 
##        self.fichas+=self.apuestas
##        self.casino-=self.apuestas
##    else:
##        self.casino+=self.apuestas










            
