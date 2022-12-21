from locations import locations
import random
import time 
wood = 10
rocks = 10
sticks = 0
AxeDurability = 0
raw_fish = 0
cooked_fish = 0
mushrooms = 0
energy = 10
row = 0
place = 0
house = 0
campfire = 0
axe = 0


#WON--------------------------------
def Won():
    print('Now you have enough materials for house!')
    print('Go to flat terrain and type \'Build\' to build house and end game!')
    


#GO---------------------------------------
def Go():
    global row
    global place
    print(f'''Where you want to go?
                     NORTH
                 WEST stay EAST
                     SOUTH
            ''')
    moove = input(': ')
    if str.lower(moove) == 'north':
        row -= 1
        if row >= 0:
            print(f'Now you {locations[row][place]}')
            Mooove()
        else:
            row += 1
            print('You cant go there')
            Go()
    
    elif str.lower(moove) == 'south':
        row += 1
        if row <= 1:
            print(f'Now you {locations[row][place]}')
            Mooove()
        else:
            row -= 1
            print('You cant go there')
            Go()

    elif str.lower(moove) == 'west':
        place -= 1
        if place >= 0:
            print(f'Now you {locations[row][place]}')
            Mooove()
        else:
            place += 1
            print('You cant go there')
            Go()

    elif str.lower(moove) == 'east':
        place += 1
        if place <= 2:
            print(f'Now you {locations[row][place]}')
            Mooove()
        else:
            place -= 1
            print('You cant go there')
            Go()

    elif str.lower(moove) == 'stay':
        Mooove()


#FISHING--------------------------------
def Fishing():
    global fish
    global raw_fish
    chance = random.randint(1, 4)
    print("Fishing...")
    time.sleep(1)
    print("Fishing...")
    time.sleep(1)
    print("Fishing...")
    time.sleep(1)
    if chance  == 2:
        print("You caught a fish")
        raw_fish += 1
        Mooove()
    else:
        print("The fish swam away..")
        Mooove()


#EAT------------------------------------
def Eat():
    global raw_fish
    global cooked_fish
    global mushrooms
    global energy
    if raw_fish + cooked_fish + mushrooms == 0:
        print('You dont have food')
        Mooove()
    else:
        print(f'Raw Fish: {raw_fish}\nCooked Fish: {cooked_fish}\nMushrooms: {mushrooms}')
        moove = input('What you wanna eat: ')
        if str.lower(moove) == 'raw fish':
            raw_fish -= 1
            chance = random.randint(0, 2)
            if chance == 1:
                energy += 1
                print('You got 1 energy')
                Mooove()
            else:
                energy -= 12
                print('You got poisoned by raw fish and lost 2 energy')
                Mooove()

        elif (str.lower(moove) == 'cooked fish' and cooked_fish >= 1):
            cooked_fish -= 1
            energy += 3
            print('You ate cooked fish and got 3 energy')
            Mooove()

        elif (str.lower(moove) == 'mushroom' and mushrooms >= 1):
            mushrooms -= 1
            energy += 1
            Mooove()
        else:
            print('You dont have that food')
            Mooove()
#CRAFTING-------------------------------
def Craft():
    global wood
    global rocks
    global campfire
    global axe
    print('What you want to craft: ')
    print('Back \nCampfire \nAxe')
    moove = input(': ')
    if str.lower(moove) == 'campfire':
        moove = input(f'To craft campfire you need 4 wood and 3 rocks \nType \'Yes\' or \'No\': ')
        if str.lower(moove) == 'yes':
            if (wood >= 4 and rocks >= 3):
                campfire += 1
                rocks -= 3
                wood -= 4
                print('You crafted campfire, now you can cook')
                Craft()

            else:
                print('You dont have enough materials')
                Craft()

        elif str.lower(moove) == 'no':
            Craft()

        else:
            print('You are lost in thought')
            Craft()
            

    elif str.lower(moove) == 'axe':
        moove = input(f'To craft axe you need 2 wood and 3 rocks \nType \'Yes\' or \'No\': ')
        if str.lower(moove) == 'yes':
            if (wood >= 2 and rocks >= 3):
                axe += 1
                rocks -= 3
                wood -= 2
                print('You crafted axe, now you can get more wood with less energy')
                Craft()
            else:
                print('You dont have enough materials')
                Craft()

        elif str.lower(moove) == 'no':
            Craft()

        else:
            print('You are lost in thought')
            Craft()
    elif str.lower(moove) == 'back':
        Mooove()
    else:
        print('You are lost in thought')
        Craft()
#BACKPACK--------------------------------
#COOKING--------------------------------
#MATERIALS------------------------------
#MAP---------DRAWN BY COAL
#MOOVES-----------------------------------
def Mooove():
    global row
    global place
    if energy <= 0:
        print('You dead')
    else:    
        moove = input('Type what you want to do: ')
        if str.lower(moove) == 'go':
            Go()

        elif str.lower(moove) == 'fish':
            if (row == 0 and place == 1):
                Fishing()
            else:
                print('You cant fish here, there is no river nearby')
            Mooove()  
            
        elif str.lower(moove) == 'eat':
            Eat()
    
        elif str.lower(moove) == 'cheats':
            Cheats()

        elif str.lower(moove) == 'craft':
            Craft()

        else:
          print('Unkown, try again')
          Mooove()


#WIN CHECK------------------------------
def WinOrNot():
    while (wood >= 45 and rocks >= 25 and energy >= 15):
        Won()
    else:
        Mooove()

#CHEATS---------------------------------
def Cheats():
    global raw_fish
    i2 = int(input(':  '))
    raw_fish += i2
    print(f'{raw_fish}')
    Mooove()

WinOrNot()