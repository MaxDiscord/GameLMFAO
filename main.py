import random
import time
import pygame

# pygame.init()  
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
screenx = 1400
screeny = 1400
# display_surface = pygame.display.set_mode((screenx, screeny )) 

x=3
y=3
maxx=5
maxy=5
energy = 0
money = 600
solarcost = 80
minercost = 30
refinercost = 100
solars = 0
miners = 0
refiners = 0
unrefined = 0
fabricatorcost= 500
ore = 0
bars = 0
allowFabrication=False
allowRadar =False
gridname = [[0 for x in range(maxx)] for y in range(maxy)]

gridname[0][0]="Plains"
gridname[0][1]="Plains"
gridname[0][2]="Plains"
gridname[0][3]="Plains"
gridname[0][4]="Plains"
gridname[1][0]="Plains"
gridname[1][1]="Plains"
gridname[1][2]="Plains"
gridname[1][3]="Plains"
gridname[1][4]="Plains"
gridname[2][0]="Plains"
gridname[2][1]="Plains"
gridname[2][2]="Plains"
gridname[2][3]="Plains"
gridname[2][4]="Plains"
gridname[3][0]="Plains"
gridname[3][1]="Plains"
gridname[3][2]="Plains"
gridname[3][3]="Plains"
gridname[3][4]="Plains"
gridname[4][0]="Plains"
gridname[4][1]="Plains"
gridname[4][2]="Plains"
gridname[4][3]="Plains"
gridname[4][4]="Plains"

status=0
while status==0:
    print (gridname[x][y])
    print ("You have",money,"$")
    print ("You have",energy, "energy")
    print ("You have",unrefined, "unrefined ore")
    print ("You have",ore,"ore ore")
    print ("You have",solars,"extra Solars.")
    print ("You have",miners,"extra miners.")
    print ("You have",refiners,"extra refiners")
    enter = input ("> ")
    if enter=="n":
        y=y-1
    elif enter=="s":
        y=y+1
    elif enter=="w":
        x=x-1
    elif enter=="e":
        x=x+1
    elif x<0:
        x=0
        print("This area can not be explored yet.")
    if enter=="give":
        give = input ("What do you want to give? ")
        if give == ("Solars"):
            count = input ("How many Solars do you want to give? ")
            count = int(count)
            solars = solars + count
            count = 0
        if give == ("Miners"):
            count = input ("How many miners do you want to give? ")
            count = int(count)
            miners = miners +count
            count=0
        if give == ("Refiners"):
            count = input ("How many refiners do you want to give? ")
            count = int(count)
            refiners = refiners+count
            count=0
    if x>maxx-1:
        x=maxx-1
        print("This area can not be explored yet.")
    elif y<0:
        y=0
        print("This area can not be explored yet.")
    elif y>maxy-1:
        y=maxy-1
        print("This area can not be explored yet.")
    if enter =="shop":
        shop = input ("What do you want to buy? ")
        if shop == ("Solars"):
            how = input ("How many Solars do you want to buy? ")
            how = int(how)
            if money < solarcost*how:
                print ("You do not have enough money")
            else:
                money = money - (solarcost * how)
                if how >1:
                    print ("You are buying more than one Solar, the other",how-1,"will go to your inventory. Use the place command to place these at a new tile")
                    solars = solars + (how-1)
                    how=0
                else:
                    how = 0
                    if gridname[x][y] != "Plains":
                        print ("There is already a",gridname[x][y], "at that location")
                        delete = input ("Do you want to delete it? ")
                        if delete == "yes":
                            gridname[x][y] = "Plains"
     
                print ("Building")
                time.sleep(2)
                gridname[x][y] = 'Solars'
                print ("Built")
                
        elif shop == ("miners"):
            how = input ("How many miners do you want to buy? ")
            how = int(how)
            if money < minercost*how:
                print ("You do not have enough money")
            else:
                money = money - (minercost * how)
                if how >1:
                    print ("You are buying more than one miner, the other",how-1,"will go to your inventory. Use the place command to place these at a new tile")
                    miners = miners + (how-1)
                    how=0
                else:
                    how=0
                    if gridname[x][y] != "Plains":
                        print ("There is already a",gridname[x][y], "at that location")
                        delete = input ("Do you want to delete it? ")
                        if delete == "yes":
                            gridname[x][y] = "Plains"
                        
                print ("Building")
                time.sleep(2)
                gridname[x][y] = 'Miner'
                print ("Built")

        elif shop == ("refiners"):
            how = input ("How many refiners do you want to buy? ")
            how = int(how)
            if money < refinercost*how:
                print ("You do not have enough money")
            else:
                money = money - (refinercost * how)
                if how >1:
                    print ("You are buying more than one refiner, the other",how-1,"will go to your inventory. Use the place command to place these at a new tile")
                    refiners = refiners + (how-1)
                    how=0
                else:
                    how=0
                    if gridname[x][y] != "Plains":
                        print ("There is already a",gridname[x][y], "at that location")
                        delete = input ("Do you want to delete it? ")
                        if delete == "yes":
                            gridname[x][y] = "Plains"
                        
                print ("Building")
                time.sleep(2)
                gridname[x][y] = 'Refiner'
                print ("Built")

        elif shop == ('fabricator'):
            
            if money < fabricatorcost:
                print ("You do not have enough money")
            else:
                money = money - fabricatorcost
                allowFabrication = True
                if gridname[x][y] != "Plains":
                        print ("There is already a",gridname[x][y], "at that location")
                        delete = input ("Do you want to delete it? ")
                        if delete == "yes":
                            gridname[x][y] = "Plains"
                else:
                    gridname[x][y] = 'Fabricator'
                            
   # Count energy  ----------
    print ("----------------")
    for b in range(0,maxy):
        for a in range (0,maxx):
            if gridname[a][b]== 'Solars':
                energy = energy + 5
            if gridname[a][b]== 'Miner':
                energy = energy -1
                mine = random.randint (5,12)
                unrefined = unrefined + mine
            if gridname[a][b] == 'Refiner':
                energy = energy - 2
                refine = random.randint(4,mine)
                unrefined = unrefined - refine
                ore = ore + refine
    if allowRadar == True:
            for b in range(0,maxy):
                for a in range (0,maxx):
                    if b==y and a==x:
                        print ("Player",end=" ")
                    else:
                        if gridname[a][b]== "Solars":
                            print("Solar",end=" ")
                        if gridname[a][b] == "Miner":
                            print ("Miner",end=" ")
                        if gridname[a][b] == "Refiner":
                            print ("Refiner",end=" ")
                        if gridname[a][b] == "Fabricator":
                            print ("Radar",end=" ")
                        if gridname[a][b] == "Radar":
                            print (">",end=" ")
                        if gridname[a][b] == "Plains":
                            print ('Plains',end=" ")
                print("")
    print ("----------------")              
    if enter == ("place"):
        place = input ("What do you want to place? ")
        if place == ("Solars"):
            ask = input ("How many? ")
            ask = int (ask)
            if ask > solars:
                print ("You do not have enough Solars for that.")
            else:
                if gridname[x][y] != 'Plains':
                    print ("There is already a",gridname[x][y], "there")
                else:
                    gridname[x][y] = 'Solars'
                    solars = solars - ask
        if place == ("miner"):
            ask = input ("How many? ")
            ask = int (ask)
            if ask > miners:
                print ("You do not have enough miners for that.")
            else:
                if gridname[x][y] != 'Plains':
                    print ("There is already a",gridname[x][y], "there")
                else:
                    gridname[x][y] = 'Miner'
                    miners = miners - ask


        if place == ("refiner"):
            ask = input ("How many? ")
            ask = int (ask)
            if ask > refiners:
                print ("You do not have enough refiners for that.")
            else:
                if gridname[x][y] != 'Plains':
                    print ("There is already a",gridname[x][y],"there")
                else:
                    gridname[x][y] = 'Refiner'
                    refiners = refiners -ask
    if enter == ("sell"):
        sell = input ("What do you want to sell? ")
        if sell == ("unrefined"):
            price = random.randint (4,8)
            print ("The ally leagon has offered you $",price,"do you accept?")
            accept = input (" ")
            p = input ("How many unrefined ore do you want to sell? ")
            p = int (p)
            if accept == "yes":
                money = money+ (price*p)
                unrefined = unrefined - p
            if accept == "no":
                print ("Offer declined")
        if sell == ("ore"):
            pric = random.randint (8,16)
            print ("The ally leagon has offered you$",pric, "do you accept?")
            accept = input (" ")
            l = input ("How much ore ore do you want to sell? ")
            l = int (l)
            if accept == "yes":
                money = money + (pric*l)
                ore = ore - l
        if sell == ("bars"):
            if allowFabrication == True:
                pri = random.randint (800,1600)
                print ("The ally leagon has offered you $",pri, "do you accept?")
                accept = input ("")
                o = input ("How many bars do you want to sell? ")
                o = int (o)
                if accept == "yes":
                    money = money + (pri*o)
                    bars = bars - o
        
    if enter == ("fabricate"):
        if allowFabrication == True:
            fabricat = input ("What do you want to fabricate? ")
            if fabricat == ("bar"):
                count = input ("How many bars do you want to make? ")
                count = int (count)
                if count > ore:
                    print ("You do not have enough ore ore. You need 100 for 1 bar.")
                else:
                    ore = ore - (count *100)
                    energy = energy - 10
                    bars = bars + count
            if fabricat == ("launcher"):
                if bars == 0:
                    print ("You need to get a ore bar to be able to make a launcher")
                elif ore <70:
                    print ("You need to get more  ore (70 total)")
                elif energy <30:
                    print ("You need to get more energy (30 total)")
                else:
                    print ("You have enough recources to make a launcher!")
                    bars = bars-1
                    ore = ore - 70
                    energy = energy - 30
                    gridname[x][y] = 'Launcher'
            if fabricat == ("radar"):
                if ore <30:
                    print ("You need more ore")
                elif energy<10:
                    print ("You need more energy")
                else:
                    ore = ore - 30
                    energy = energy-10
                    gridname[x][y] = 'Radar'
                    allowRadar= True
                    
                    
                    
                
        else:
            print ("You do not have a fabricator yet.")
                    
                
            
            
            
