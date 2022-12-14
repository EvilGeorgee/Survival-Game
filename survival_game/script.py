from locations import locations
import random
import time 
wood = 0
rocks = 0
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

#MOOVES---------------------------------
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

        elif str.lower(craft):
            Crafting()

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