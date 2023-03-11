import random
rundor=0#basvärde rundor
rundval = "Välj antal rundor fighten ska pågå(3-10):"

while rundor<3 or rundor>10:#loop tills rätt antal rundor
    rundor=input(rundval)
    if rundor.isdigit == False:
        print ("du kan bara använda dig av siffror")
        rundor=input(rundval)
    elif int(rundor)<3 or int(rundor) >10: #felkod
        print ("rundor är utanför valbart spann")
    rundor = int(rundor)
    
    


spelarenamn="a"# basvärde utanför while loop

while len(spelarenamn)<3 or len(spelarenamn)>10: #funktion för att namnge spelare
    spelarenamn=input("Vad vill du att din spelare ska heta? 3-10 tecken: ")
    if len(spelarenamn)<3 or len (spelarenamn)>10:
        print ("Felaktigt antal tecken")

namnlista=["Boris","George","Jakob"]#lista med namn det slumpas från
datornamn=random.choice(namnlista)#slumpa namn ur lista


saldo=100 #basvärde för saldo
print("ditt saldo är ", saldo)
o=0#basvärde för att kunna ge global värde om satsning senare
def betting():
    satstning=9999**9999
    
    while satstning>saldo:#loop tills rätt värden på satsning
        satstning=int(input("Hur mycket vill du satsa? "))
        if satstning>saldo:
            print ("Du kan inte satsa mer än du har, försök igen ")
            satstning=int(input("Hur mycket vill du satsa? "))
            if satstning>saldo:
                print ("Du kan inte satsa mer än du har,du får ett sista försök ")
                satstning=int(input("Hur mycket vill du satsa? "))

                
        if saldo>=satstning:#kod för att göra satsningen utanför def 
            global o
            o=satstning
        return()

y="a"#basvärde för att kunna ge global värde om vem som är vinnare senare

def spelrunda():#funktion som avgör vem som kommer vinna spelet
        
      
        spelare1hp=30
        spelare2hp=30
        runda=1
        while spelare1hp>=0 or spelare2hp>=0 or runda<=rundor:
            print ("runda", runda, "av", rundor)#varvräknare
            #spelare slag
            typ_av_slag=input("Skriv H om du slå hårt med dålig träffsäkerhet annars slår du automatiskt lösare med bättre träffsäkerhet: ")
            if typ_av_slag=="h"or typ_av_slag=="H":
                print (f"{spelarenamn} Slog hårt")
                träffa_2=random.randint(1,100)
                if träffa_2>50:#träff
                    slag2=random.randint(10,15)
                    miss2=1
                    
                elif träffa_2<50:#miss 
                    slag2=0
                    miss2=0
                
            if not typ_av_slag =="h" or typ_av_slag=="H":
                 träffa_2=random.randint(1,100)
                 if träffa_2<75:#25%chans att missa
                    slag2=random.randint(1,10)#slag mot spelare1
                    miss2=1
                 elif träffa_2>=25:
                    slag2=0
                    miss2=0

            critical_hit=random.randint(1,100)#slumpad chans att göra mer skada
            if critical_hit>97:
                slag2=slag2*1.5
                print(f"{spelarenamn} Critical hit")

            #dator slag
            slag=("hårt","löst")#sorters slag
             
            datorslag=random.choice(slag)
            if datorslag=="löst":
                print (datornamn,"slog löst men träffsäkert")
                träffa_1=random.randint(1,100)
                if träffa_1<75:#25%chans att missa
                    miss1=1
                    slag1=random.randint(1,10)#slag mot spelare1
                elif träffa_1>=25:
                    miss1=0
                    slag1=0
            if datorslag=="hårt":
                print (f"{datornamn} Slog hårt")
                träffa_1=random.randint(1,100)
                if träffa_1>50:#träff
                    slag1=random.randint(10,15)
                    miss1=1
                            

                elif träffa_1<50:#miss 
                    slag1=0
                    miss1=0

            critical_hit=random.randint(1,100)#slumpad chans att göra mer skada
            if critical_hit>97:
                slag1=slag1*1.5
                print(f"{datornamn} Critical hit")
    

            
            #utskrift efter varje runda vad som händer 
            spelare1hp=spelare1hp-slag1
            if spelare1hp<0: 
                spelare1hp=0
            if miss1==0:
                print (datornamn,"Missade slitt slag ")
            if miss1==1:
                print (datornamn,"träffade sitt slag")
            print (f"{spelarenamn} blev av med {slag1} HP och har {spelare1hp} HP kvar")
            spelare2hp=spelare2hp-slag2
            if spelare2hp<0:
                 spelare2hp=0
            if miss2==0:
                print (spelarenamn,"Missade sitt slag ")
            if miss2==1:
                print (spelarenamn,"Träffade sitt slag")
            print (f"{datornamn} blev av med {slag2} HP och har {spelare2hp} HP kvar")
            runda=runda+1
            print ()
            #avgör om antal rundor som är slut
            if runda==rundor+1:
                print ("Antal rundor är slut vinnaren är spelaren med mest HP ")
                if spelare1hp>spelare2hp:
                    print (spelarenamn, "har vunnit över", datornamn)
                    vinnare=spelarenamn
                    break
                elif spelare2hp>spelare1hp:
                    print(datornamn,"har vunnit över ",spelarenamn)
                    vinnare=datornamn
                    break
                elif spelare1hp==spelare2hp:
                    print ("Matchen oavgjort båda spelare har lika mycket HP kvar")
                    vinnare="oavgjort"
                    break
            #avgör om det är knock out
            if spelare1hp <=0 and spelare2hp<=0:
                vinnare="oavgjort"
                print ("Det blev oavgjort båda spelare har 0 HP")
                break
            elif spelare1hp<=0 and spelare2hp>=1:
                vinnare=datornamn
                print (f"{datornamn} vann och har {spelare2hp} HP kvar, {spelarenamn} har 0 HP")
                break
            elif spelare2hp<=0 and spelare1hp>=1:
                vinnare=spelarenamn
                print (f"{spelarenamn} vann och har {spelare1hp} HP kvar, {datornamn} har 0 HP")
                break
        global y
        y=vinnare
       
       
     
betting()

spelrunda()
#utskrift för att se vinnare och uträkning av saldo
if spelarenamn==y:
    saldo=saldo+o
    print (f"Du vann,ditt nuvarande saldo är {saldo}")
elif datornamn==y:
    saldo=saldo-o
    print (f"Du förlorade, ditt nuvarande saldo är {saldo}")
igen=True#basvärde för att spela igen
while igen==True:#loop för att köra igen

    
     #kod för att spela igen och fortsätta med upparbetat saldo
    igen=input ("Vill du spela igen? om ja tryck på J vill du avsluta tryck på N: ")
    if igen=="j" or igen=="J":
         betting()
         spelrunda()
         igen=True
    elif igen=="n" or igen=="N":
         igen=False
         
         
    else:
         print ("Felaktigt val försök igen")
         igen=input ("Vill du spela igen? om ja tryck på J vill du avsluta tryck på N: ")
         igen=True

