#labaries
import itertools
import random
import csv
from typing import ChainMap
import pandas as pd
from turtle import update
from numpy import roll


#Function to selected a list of Weapns by it's property
def search_weapon_property (property):
    x = []
    for i in dict_weapons: 
        for y in dict_weapons[i]["Properites"]: 
            if y == property: (x.append(i))

    return x    

#global variables
races = []
classes = []
attributes = ["Strength","Dexterity","Constitution","Intelegence","Wisdom","Charsima"]
skills = ["Acrobatics", "Animal Handling", "Arcana", "Atheletics", "Deception", "History", "Insight", "Intimidation","Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuassion", "Religion", "Slight of Hand", "Stealth", "Survival"]
#tools = [Artisan][Gaming Sets][Musical Instruments][Other]
tools = [["Alchemist Tools","Brewer Tools","Calligrapher Tools","Cartographer Tools","Cobbler Tools","Cook Tools","Glassblower Tools","Jewler Tools","Leatherwork Tools","Mason Tools","Painter Tools","Potter Tools","Smith Tools","Tinker Tools","Weaver Tools","Woodcarver Tools"],["Dice","Cards"],["Bagpipes","Drum","Dulcimer","Flute","Lute,","Lyre","Horn","Pan flute","Shawm","Viol"],["Disguise Kit","Forgery Kit","Herbalism Kit","Navigator Tools","Poisoner Kit","Theives Tools"]] 
tools_dwarf = [tools[0][1],tools[0][9],tools[0][12]]
vehicles = ["Land Vehicles","Water Vehicles"]
resistances = ["Acid", "Bludgeoning", "Cold", "Fire", "Force", "Lightening", "Nectrotic", "Piercing", "Poison", "Psychic" , "Radiant", "Slashing", "Thunder"]
weapons = ["Simple","Martial","Longsword","Shortsword","Longbow","Shortbow","Battleaxe","Handaxe","Light hammer","Warhammer","Hand Crossbow","Rapier","Club","Dagger","Dart","Javelin","Mace","Quaterstaff","Scimitar","Sickle","Sling","Spear","Light Crossbow"]
armour = ["Light Armour","Medium Armour","Heavy Armour","Shields"]
languages = ["Common","Evlish","Dwarvish","Giant","Gnomish","Halfling","Orc","Abyssal","Celestial","Draconic","Deep Speech","Infernal","Primordial","Sylvan","Undercommon"]     



#global dictionaries

#dict_char defines the keys for the highest level of the character structure
dict_char = dict.fromkeys([
"Key",
"Characteristics",
"Attributes",
"Proficiencies",
"Languages",
"Feats & Traits",
"Stats",
"Items"
])



#dict_attributesscores determines the attribute score bonuses 

dict_attributesscores = {
1 : -5,
2 : -4,3 : -4,
4 : -3,5 : -3,
6 : -2,7 : -2,
8 : -1,9 : -1,
10 : 0,11 : 0,
12 : 1,13 : 1,
14 : 2,15 : 2,
16 : 3,17 : 3,
18 : 4,19 : 4,
20 : 5,21 : 5,
22 : 6,23 : 6,
24 : 7,25 : 7,
26 : 8,27 : 8,
28 : 9,29 : 9,
30 : 10
}

#dict_items a dictionary for all the item types in the 5e rule book, this is done through loading in a CSV files here
dict_items = { }
with open ('C:/Users/BK82183/Desktop/DandD_CodeProject/Character_Generator/items/Items.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                #print(f'\t{row[0]}')
                line_count += 1
                dict_items[row[0]] = row [1:]


#dict_weapons is a dictionary for each of the basic weapons in 5e and it's corisponding stats
#{weapon:{properites:[...],damage:[# of dice, size of dice, type of damage],range[min,max]}}
dict_weapons = {
"Club":{"Properites":["Simple","Melee","Light"],"Damage":[1,4,resistances[1]],"Range":[5,5]},
"Dagger":{"Properites":["Simple","Melee","Finesse","Light","Thrown"],"Damage":[1,4,resistances[7]],"Range":[20,60]},
"Greatclub":{"Properites":["Simple","Melee","Two-handed"],"Damage":[1,8,resistances[1]],"Range":[5,5]},
"Handaxe":{"Properites":["Simple","Melee","Light","Thrown"],"Damage":[1,6,resistances[11]],"Range":[20,60]},
"Javelin":{"Properites":["Simple","Melee","Thrown"],"Damage":[1,6,resistances[7]],"Range":[30,120]},
"Light hammer":{"Properites":["Simple","Melee","Light","Thrown"],"Damage":[1,4,resistances[1]],"Range":[20,60]},
"Mace":{"Properites":["Simple","Melee"],"Damage":[1,6,resistances[1]],"Range":[5,5]},
"Quaterstaff":{"Properites":["Simple","Melee",{"Versatile":[1,8,resistances[1]]}],"Damage":[1,6,resistances[1]],"Range":[5,5]},
"Sickle":{"Properites":["Simple","Melee","Light"],"Damage":[1,4,resistances[11]],"Range":[5,5]},
"Spear":{"Properites":["Simple","Melee","Thrown",{"Versatile":[1,8,resistances[7]]}],"Damage":[1,6,resistances[7]],"Range":[20,60]},
"Light Crossbow":{"Properites":["Simple","Ranged","Ammunition","Loading","Two-handed"],"Damage":[1,8,resistances[7]],"Range":[80,320]},
"Dart":{"Properites":["Simple","Ranged","Finesse","Thrown"],"Damage":[1,4,resistances[7]],"Range":[20,60]},
"Shortbow":{"Properites":["Simple","Ranged","Ammunition","Two-handed"],"Damage":[1,6,resistances[7]],"Range":[80,320]},
"Sling":{"Properites":["Simple","Ranged","Ammunition"],"Damage":[1,4,resistances[1]],"Range":[30,120]},
"Battleaxe":{"Properites":["Martial","Melee",{"Versatile":[1,10,resistances[11]]}],"Damage":[1,8,resistances[11]],"Range":[5,5]},
"Flail":{"Properites":["Martial","Melee",],"Damage":[1,8,resistances[1]],"Range":[5,5]},
"Glaive":{"Properites":["Martial","Melee","Heavy","Reach","Two-handed"],"Damage":[1,10,resistances[11]],"Range":[10,10]},
"Greataxe":{"Properites":["Martial","Melee","Heavy","Two-handed"],"Damage":[1,12,resistances[11]],"Range":[5,5]},
"Greatsword":{"Properites":["Martial","Melee","Heavy","Two-handed"],"Damage":[2,6,resistances[11]],"Range":[5,5]},
"Halberd":{"Properites":["Martial","Melee","Heavy","Reach","Two-handed"],"Damage":[1,10,resistances[11]],"Range":[10,10]},
"Lance":{"Properites":["Martial","Melee","Reach","Special"],"Damage":[1,12,resistances[7]],"Range":[10,10]},
"Longsword":{"Properites":["Martial","Melee",{"Versatile":[1,10,resistances[11]]}],"Damage":[1,8,resistances[11]],"Range":[5,5]},
"Maul":{"Properites":["Martial","Melee","Heavy","Two-handed"],"Damage":[2,6,resistances[1]],"Range":[5,5]},
"Pike":{"Properites":["Martial","Melee","Heavy","Reach","Two-handed"],"Damage":[1,10,resistances[7]],"Range":[10,10]},
"Rapier":{"Properites":["Martial","Melee","Finesse"],"Damage":[1,8,resistances[7]],"Range":[5,5]},
"Scimitar":{"Properites":["Martial","Melee","Finesse","Light"],"Damage":[1,6,resistances[11]],"Range":[5,5]},
"Shortsword":{"Properites":["Martial","Melee","Finesse","Light"],"Damage":[1,6,resistances[7]],"Range":[5,5]},
"Trident":{"Properites":["Martial","Melee","Thrown",{"Versatile":[1,8,resistances[7]]}],"Damage":[1,6,resistances[7]],"Range":[20,60]},
"War pick":{"Properites":["Martial","Melee"],"Damage":[1,8,resistances[7]],"Range":[5,5]},
"Warhammer":{"Properites":["Martial","Melee",{"Versatile":[1,10,resistances[1]]}],"Damage":[1,8,resistances[1]],"Range":[5,5]},
"Whip":{"Properites":["Martial","Melee","Finesse","Reach"],"Damage":[1,4,resistances[11]],"Range":[10,10]},
"Blowgun":{"Properites":["Martial","Ranged","Ammunition","Loading"],"Damage":[1,1,resistances[7]],"Range":[25,100]},
"Hand Crossbow":{"Properites":["Martial","Ranged","Ammunition","Light","Loading"],"Damage":[1,6,resistances[7]],"Range":[30,120]},
"Heavy Crossbow":{"Properites":["Martial","Ranged","Ammunition","Heavy","Loading"],"Damage":[1,10,resistances[7]],"Range":[100,400]},
"Longbow":{"Properites":["Martial","Ranged","Ammmunition","Heavy","Two-handed"],"Damage":[1,8,resistances[7]],"Range":[150,600]},
"Net":{"Properites":["Martial","Ranged","Special","Thorwn"],"Damage":[0,0,resistances[1]],"Range":[5,15]}
}
"""for key in dict_weapons:
    print(key,  " : ",  dict_weapons[key])"""

dict_starting_items_kits = {
"Burgler's Pack" : {"Backpack":1,"Ball Bearings (Bag)":1,"String (10ft)":1,"Bell":1,"Candle":5,"Crowbar":1,"Hammer":1,"Piton":1,"Latern (Hooded)":1,"Oil (Flask)":2,"Ration":5,"Tinderbox":1,"Waterskin":1,"Rope, Hempen (50ft)":1},
"Diplomat's Pack" : {"Chest":1,"Case (Map/Scroll)":2,"Clothes (Fine)":1,"Ink (Bottle)":1,"Ink Pen":1, "Lamp":1,"Oil  (Flask)":2,"Paper (Sheet)":5,"Vial (Perfume)":1,"Sealing Wax":1},
"Dungeoneer's Pack" : {"Backpack":1,"Crowbar":1,"Hammer":1,"Piton":10,"Tourch":10,"Ration":10,"Waterskin":1,"Rope, Hempen (50ft)":1},
"Entertainer's Pack": {"Backpack":1,"Bedroll":1,"Clothes (Costume)":2,"Candle":5,"Ration":5,"Waterskin":1,"Disguise Kit":1},
"Explorer's Pack" : {"Backpack":1,"Bedroll":1,"Mess Kit":1,"Tinderbox":1,"Torch":10,"Ration":10,"Waterskin":1,"Rope, Hempen (50ft)":1},
"Priest's Pack" : {"Backpack":1,"Bedroll":1,"Candle":10,"Tinderbox":1,"Alms Box":1,"Block of Incense":1,"Censer":1,"Rations":2,"Clothes (Vestments)":2,"Waterskin":1},
"Scholar's Pack" : {"Backpack":1,"Book of Lore":1,"Ink Pen":1,"Ink (Bottle)":1,"Parchment":10,"Small Bag of Sand":1,"Knife":1}
}


#dict_race = {race:[attributes][skills][tools][vehicles][resistances][weapons][armour][languages][traits/abilities/feats]}
dict_race = {
"Dragonborn (Black)":[[2,0,0,0,0,1,0,30,'Medium'],[],[],[],[resistances[0]],[],[],[languages[0],languages[9]],[]],
"Dragonborn (Blue)":[[2,0,0,0,0,1,0,30,'Medium'],[],[],[],[resistances[5]],[],[],[languages[0],languages[9]],[]],
"Dragonborn (Brass)":[[2,0,0,0,0,1,0,30,'Medium'],[],[],[],[resistances[3]],[],[],[languages[0],languages[9]],[]],
"Dragonborn (Copper)":[[2,0,0,0,0,1,0,30,'Medium'],[],[],[],[resistances[0]],[],[],[languages[0],languages[9]],[]],
"Dragonborn (Gold)":[[2,0,0,0,0,1,0,30,'Medium'],[],[],[],[resistances[3]],[],[],[languages[0],languages[9]],[]],
"Dragonborn (Green)":[[2,0,0,0,0,1,0,30,'Medium'],[],[],[],[resistances[8]],[],[],[languages[0],languages[9]],[]],
"Dragonborn (Red)":[[2,0,0,0,0,1,0,30,'Medium'],[],[],[],[resistances[3]],[],[],[languages[0],languages[9]],[]],
"Dragonborn (Silver)":[[2,0,0,0,0,1,0,30,'Medium'],[],[],[],[resistances[2]],[],[],[languages[0],languages[9]],[]],
"Dragonborn (White)":[[2,0,0,0,0,1,0,30,'Medium'],[],[],[],[resistances[2]],[],[],[languages[0],languages[9]],[]],
"Dwarf (Hill)":[[0,0,2,0,0,1,0,25,'Medium'],[],[random.choice(tools_dwarf)],[],[resistances[8]],[weapons[6],weapons[7],weapons[8],weapons[9]],[],[languages[0],languages[2]],[]],
"Dwarf (Mountain)":[[2,0,2,0,0,0,0,25,'Medium'],[],[random.choice(tools_dwarf)],[],[resistances[8]],[weapons[6],weapons[7],weapons[8],weapons[9]],[armour[0],armour[2]],[languages[0],languages[1]],[]],
"Elf (Eladrin)":[[0,2,0,1,0,0,0,30,'Medium'],[skills[11]],[],[],[],[weapons[2],weapons[3],weapons[4],weapons[5]],[],[languages[0],languages[1]],[]],
"Elf (High)":[[0,2,0,1,0,0,0,30,'Medium'],[skills[11]],[],[],[],[weapons[2],weapons[3],weapons[4],weapons[5]],[],[languages[0],languages[1],random.choice(languages[2:])],[]],
"Elf (Wood)":[[0,2,0,0,1,0,0,35,'Medium'],[skills[11]],[],[],[],[weapons[2],weapons[3],weapons[4],weapons[5]],[],[languages[0],languages[1]],[]],
"Gnome (Deep)":[[0,1,0,0,2,0,0,25,'Small'],[],[],[],[],[],[],[languages[0],languages[5],languages[14]],[]],
"Gnome (Rock)":[[0,0,1,0,2,0,0,25,'Small'],[],[tools[0][13]],[],[],[],[],[languages[0],languages[5]],[]],
"Half-Elf":[[0,0,0,0,0,2,2,30,'Medium'],random.sample(skills,k=2),[],[],[],[],[],[languages[0],languages[1],random.choice(languages[2:])],[]],
"Halfling (Lightfoot)":[[0,2,0,0,0,1,0,25,'Small'],[],[],[],[],[],[],[languages[0],languages[5]],[]],
"Halfling (Stout)":[[0,2,1,0,0,0,0,25,'Small'],[],[],[],[resistances[8]],[],[],[languages[0],languages[5]],[]],
"Half-Orc":[[2,0,1,0,0,0,0,30,'Medium'],[skills[7]],[],[],[],[],[],[languages[0],languages[6]],[]],
"Human (Standard)":[[1,1,1,1,1,1,0,30,'Medium'],[],[],[],[],[],[],[languages[0],random.choice(languages[1:])],[]],
"Human (Variant)":[[0,0,0,0,0,0,2,30,'Medium'],[random.choice(skills)],[],[],[],[],[],[languages[0],random.choice(languages[1:])],[]],
"Tiefling":[[0,0,0,1,0,2,0,30,'Medium'],[],[],[],[resistances[3]],[],[],[languages[0],languages[11]],[]],
}


"""for k,v in dict_race.items():
    print(k,v)"""

#dict_class = {class:[hit_die],skills#,[saving throws][skills][tools][vehicles][resistances][weapons][armour][languages][traits/abilities/feats][spells][items]]}

dict_class = {
"Barbarian":[12,2,[attributes[0],attributes[2]],[skills[1],skills[3],skills[7],skills[10],skills[11],skills[17]],[],[],[],[weapons[0],weapons[1]],[armour[0],armour[1],armour[3]],[],[],[],],
"Bard":[8,3,[attributes[1],attributes[5]],skills,[],random.sample(tools[2],k=3),[],[weapons[0],weapons[2],weapons[3],weapons[10],weapons[11]],[armour[0]],[],[],[]],
"Cleric":[8,2,[attributes[4],attributes[5]],[skills[5],skills[6],skills[9],skills[13],skills[14]],[],[],[],[weapons[0]],[armour[0],armour[1],armour[3]],[],[],[]],
"Druid":[8,2,[attributes[3],attributes[4]],[skills[1],skills[2],skills[6],skills[9],skills[10],skills[11],skills[14],skills[17]],[tools[3][2]],[],[],[weapons[12],weapons[13],weapons[14],weapons[15],weapons[16],weapons[17],weapons[18],weapons[19],weapons[20]],[armour[0],armour[1],armour[3]],[],[]],
"Fighter":[10,2,[attributes[0],attributes[2]],[skills[0],skills[1],skills[3],skills[5],skills[6],skills[7],skills[11],skills[17]],[],[],[],[weapons[0],weapons[1]],armour,[],[],[]],
"Monk":[8,2,[attributes[0],attributes[1]],[skills[0],skills[3],skills[5],skills[6],skills[14],skills[16]],[random.choice(list(itertools.chain(tools[0],tools[2])))],[],[],[weapons[0],weapons[3]],[],[],[],[]],
"Paladin":[10,2,[attributes[4],attributes[5]],[skills[3],skills[6],skills[7],skills[8],skills[13],skills[14]],[],[],[],[weapons[0],weapons[1]],armour,[],[],[]],
"Ranger":[10,3,[attributes[0],attributes[2]],[skills[1],skills[3],skills[6],skills[7],skills[8],skills[10],skills[11],skills[16],skills[17]],[],[],[],[weapons[0],weapons[1]],[armour[0],armour[1],armour[3]],[],[],[]],
"Rogue":[8,4,[attributes[1],attributes[3]],[skills[0],skills[3],skills[4],skills[6],skills[7],skills[8],skills[11],skills[12],skills[13],skills[15],skills[16]],[tools[3][5]],[],[],[weapons[0],weapons[10],weapons[11],weapons[2],weapons[3]],[armour[0]],[],[],[]],
"Sorcerer":[6,2,[attributes[2],attributes[5]],[skills[2],skills[4],skills[6],skills[7],skills[13],skills[14]],[],[],[],[weapons[13],weapons[14],weapons[17],weapons[22]],[],[],[],[]],
"Warlock":[8,2,[attributes[4],attributes[5]],[skills[2],skills[4],skills[5],skills[7],skills[8],skills[10],skills[14]],[],[],[],[weapons[0]],[armour[0]],[],[],[]],
"Wizard":[6,2,[attributes[3],attributes[4]],[skills[2],skills[5],skills[6],skills[8],skills[9],skills[14]],[],[],[],[weapons[13],weapons[14],weapons[17],weapons[22]],[],[],[]]
}
#print (dict_class["Barbarian"])
#need fixing - Barbarian 1(B) 2(B)

"""for k,v in dict_class.items():
    print(k,v)"""

#dict_background = {background:[[skills],tools#,[tools][vehicles],languages#,[languages][traits/abilities/feats][personality trait][ideal][bond][flaw][equipment]]}
dict_background = {
"Acolyte":[[skills[6],skills[14]],0,[],[],2,languages,[],[],[],[],[],[]],
"Charlatan":[[skills[4],skills[15]],2,[tools[3][0],tools[3][1]],[],0,[],[],[],[],[],[],[]],
"Criminal/Spy":[[skills[4],skills[16]],1,tools[1],[],0,[],[],[],[],[],[],[]],
"Entertainer":[[skills[0],skills[12]],2,[tools[3][0],random.choice(tools[2])],[],0,[],[],[],[],[],[],[],[]],
"Folk Hero":[[skills[1],skills[17]],1,tools[0],[vehicles[0]],0,[],[],[],[],[],[],[]],
"Guild Artisan":[[skills[6],skills[11]],1,tools[0],[],1,languages,[],[],[],[],[],[]],
"Hermit":[[skills[9],skills[14]],1,[tools[3][2]],[],1,languages,[],[],[],[],[],[]],
"Noble":[[skills[5],skills[13]],1,tools[1],[],1,languages,[],[],[],[],[],[]],
"Outlander":[[skills[3],skills[17]],1,tools[2],[],1,languages,[],[],[],[],[],[]],
"Sage":[[skills[2],skills[5]],0,[],[],2,languages,[],[],[],[],[],[]],
"Sailor":[[skills[3],skills[11]],1,[tools[3][3]],[vehicles[1]],0,[],[],[],[],[],[],[]],
"Soldier":[[skills[3],skills[7]],1,tools[1],[vehicles[0]],0,[],[],[],[],[],[],[]],
"Urchin":[[skills[15],skills[16]],2,[tools[3][0],tools[3][4]],[],0,[],[],[],[],[],[],[]]
}


"""for k,v in dict_background.items():
    print(k,v)"""

#Function to roll dice
def roll_dice (n=1,s=20,d=0,a = "n/a"):
    #n = number of dice to roll
    #s = size of dice to roll (d6,d8,d12)
    #d = number of dice to drop (0,1,2...)
    #a = droping higher (h) or lower (l)

    # Generate list of dice rolls
    x = [random.randint(1,s) for i in range (0,n)]
    x.sort(reverse = True)
    #if 'h' drop high numbers, if 'l' drop low numbers, else do nothing
    if a == 'h':
        x.pop(0)
    if a == 'l':
        x.pop (n-1)
    return x

#Get the users to input the first and last names of the character they wish to create
def char_name ():
    #f_name = input ("What is your characters first name?\n")
    #s_name = input ("What is you characters second name?\n")
    f_name = 'Test'
    s_name = 'Name'
    f_name = f_name + " " + s_name
    return f_name

#Function to select a random key from a dictionary
def random_dict_key (dict_x): 
    #fill up the possible dict_list[] from the selected dictionary
    dict_keys = []
    for key in dict_x:
        dict_keys.append(key)
    selection = random.choice(dict_keys)
    return selection

#Function to randomly generate attributes using the 4d6 drop 1 method
def roll_attributes (race,char_class):
    dict_attributes = dict.fromkeys(attributes)
    
    #roll attributes
    for key in dict_attributes:
        dict_attributes [key] = sum(roll_dice(4,6,1,"l"))
    
    #print(dict_attributes)
    
    #add racial bonus's, this is jank, they're has to be a better solution

    dict_attributes ["Strength"] = dict_attributes ["Strength"] + dict_race [race][0][0]
    dict_attributes ["Dexterity"] = dict_attributes ["Dexterity"] + dict_race [race][0][1]
    dict_attributes ["Constitution"] = dict_attributes ["Constitution"] + dict_race [race][0][2]
    dict_attributes ["Intelegence"] = dict_attributes ["Intelegence"] + dict_race [race][0][3]
    dict_attributes ["Wisdom"] = dict_attributes ["Wisdom"] + dict_race [race][0][4]
    dict_attributes ["Charsima"] = dict_attributes ["Charsima"] + dict_race [race][0][5]

    #add unassigned attributes
    bonus_attributes = dict_race [race][0][6]
    for x in range (bonus_attributes):
        selection = random.choice(attributes)
        dict_attributes [selection] = dict_attributes [selection] + 1
        #print (selection) 
    
    dict_attributes ["Saving Throws"] = dict_class [char_class][2]
    #print(dict_attributes)

    return dict_attributes

#Function the assign skill proffecenies
def char_proficiencies (race,char_class,background):
    
    #varriables flattening proficienies into one list
    flatten_tools = [val for sublist in tools for val in sublist]
    proficiencies = [skills,flatten_tools,vehicles,weapons,armour]
    proficiencies = [val for sublist in proficiencies for val in sublist]
    
    #create a dictionary of priciencies
    dict_proficiencies = {}
      
    for key in proficiencies:
        dict_proficiencies [key] = 0
    
    
    ##################################### - SKILLS - #####################################
    
    #define character skills with a baseline from there race and profession
    char_skills = dict_race[race][1]
    char_skills.extend(dict_background[background][0])

    #remove any duplicates
    char_skills = list(dict.fromkeys(char_skills))

    class_skills = dict_class[char_class][3]
    #print (class_skills)
    
    #remove any class spesific skills that are covered by previously defined character skills
    for x in char_skills :
        for y in class_skills :
            if y == x:
                class_skills.remove(y)
    
    #combines the char_skills with class skills
    char_skills.extend(random.sample(class_skills, k = dict_class[char_class][1]))

    ##################################### - TOOLS - #####################################
    
    #defines character tool proficancies
    char_tools = dict_race[race][2]
    char_tools.extend(dict_class[char_class][4])
    background_tools = dict_background[background][2]
    #remove any background spesific tool proficencies that are covered by previously defined character tool proficencies
    for x in char_tools :
        for y in background_tools :
            if y == x:
                background_tools.remove(y)
    try:
        char_tools.extend(random.sample(background_tools,k = dict_background[background][1]))
    except:
        print ("Background tools have already been learned")
    #print (char_tools)

    ##################################### - Vehicles - #####################################
    char_vehicles = dict_background[background][3]

    ##################################### - Weapoms (Not Completed) - #####################################
    char_weapons = dict_race[race][5]
    char_weapons.extend(dict_class[char_class][7])

    ##################################### - Weapoms (Not Completed) - #####################################
    char_armour = dict_race[race][6]
    char_armour.extend(dict_class[char_class][8])
    ##################################### - Create 1 consolidated dictionary - #####################################


    char_proficiencies = char_skills
    char_proficiencies.extend(char_tools)
    char_proficiencies.extend(char_vehicles)
    char_proficiencies.extend(char_weapons)
    char_proficiencies.extend(char_armour)
    #print(char_proficiencies)
    #this loop makes sure that each skills that the character is given in is given a score of 1
    #proficency is tracked by using this figure, so a figure of 1 = add proficeny 1 times, 0.5 = adding half proficeny and so on
    

    for x in char_proficiencies :
        dict_proficiencies [x] = dict_proficiencies [x] + 1

    #print (dict_skills)

    ##################################### - Delete Proficenies = 0 (Might Remove Later?) - #####################################   
    keys_to_be_removed = []
    for key in dict_proficiencies:
        if dict_proficiencies[key] == 0:
            keys_to_be_removed.append(key)
    for key in keys_to_be_removed:
        dict_proficiencies.pop(key)

    return dict_proficiencies

#Function to assign known laungages
def char_languages (race,background):
    race_languages = dict_race[race][7]
    background_languages = dict_background[background][5]

    for x in race_languages :
        for y in background_languages :
            if y == x:
                background_languages.remove(y)
    background_languages = random.sample(background_languages,k = dict_background[background][4])

    char_languages = list(itertools.chain(race_languages,background_languages))
    return char_languages

#Function to calculate level 1 stats

def char_stats_lvl1 (attributes,race,char_class):
    stats = {}
    #calculate HP and Hit die
    stats ["Maximum HP"] = dict_class[char_class][0] + dict_attributesscores[attributes["Constitution"]]
    stats ["Current HP"] = stats ["Maximum HP"]
    stats ["Temporary HP"] = 0
    stats ["Maximum Hit Die"] = {dict_class[char_class][0]:1}
    stats ["Current Hit Die"] = {dict_class[char_class][0]:1}

    #calculate un-armored defense
    if char_class in ["Barbarian","Monk"]:
        if char_class == "Barbarian":
            stats ["AC"] = 10 + dict_attributesscores[attributes["Dexterity"]] + dict_attributesscores[attributes["Constitution"]]
        if char_class == "Monk": 
            stats ["AC"] = 10 + dict_attributesscores[attributes["Dexterity"]] + dict_attributesscores[attributes["Wisdom"]]
    else:
        stats ["AC"] = 10 + dict_attributesscores[attributes["Dexterity"]]
    
    #calculate speed
    stats ["Speed"] = dict_race[race][0][7]


    return stats
    
#Function to generate inventory based on class and background

def char_items (char_class,background,char_proficiencies):
    #create a list of proficenies the character has based of there proficiencies dictionary
    starting_items = {}
    proficiencies = []
    for x in char_proficiencies:
        proficiencies.append(x)



    ####### THIS Code is and example of how to do a single line IF statement for searching for multiple potential status######
    #w = ["Warhammer" if "Warhammer" in proficiencies or "Martial" in proficiencies  else "Mace"]
    #print (w)

    ####### THIS Code is and example of how to do a single line IF statement for searching for multiple potential status######

    #dictionary for each of the different starting items you can aquire by class {Item : # of Item}
    dict_starting_items_class = {
        "Barbarian" : 
            [random.choice([{"Greataxe":1},{random.choice(search_weapon_property("Martial")):1}]),
            random.choice([{"Handaxe":2},{random.choice(search_weapon_property("Simple")):1}]),
            {"Javelin":4},
            dict_starting_items_kits["Explorer's Pack"]],
        "Bard" : 
            [random.choice([{"Rapier":1},{"Longsword":1},{random.choice(search_weapon_property("Simple")):1}]),
            random.choice([{"Lute":2},{random.choice(tools[2]):1}]),
            {"Leather Armour":1},{"Dagger":1},
            random.choice([dict_starting_items_kits["Diplomat's Pack"],dict_starting_items_kits["Entertainer's Pack"]])],
        "Cleric" : 
            [random.choice([{"Mace":1},[{"Warhammer":1} if "Warhammer" in proficiencies or "Martial" in proficiencies  else {"Mace":1}]]), #only if prof
            random.choice([{"Scail Mail":1},{"Leather Armour":1},{"Chain Mail":1}]), #only if prof
            random.choice([[{"Light Crossbow":1},{"Crossbow Bolts":20}],{random.choice(search_weapon_property("Simple")):1}]),
            {"Shield":1},random.choice([{"Amulet (Holy Symbol)":1},{"Emblem (Holy Symbol)":1},{"Reliquart (Holy Symbol)":1}]),
            random.choice([dict_starting_items_kits["Priest's Pack"],dict_starting_items_kits["Explorer's Pack"]])],
        "Druid" :
        #note "wooden shield might need to be added as an item, also currently only searching for Simple instead of simple melee"
            [random.choice([{"Wooden Shield":1},{random.choice(search_weapon_property("Simple")):1}]),
            random.choice([{"Scimitar":1},{random.choice(search_weapon_property("Simple")):1}]),
            {"Leather Armour":1},random.choice([{"Sprig of Mistletoe":1},{"Totem":1},{"Wooden Staff":1},{"Yew Wand":1}]),
            dict_starting_items_kits["Explorer's Pack"]],
        "Fighter" :
            [random.choice([{"Chain Shirt":1},[{"Leather Armour":1},{"Longbow":1},{"Arrows":20}]]),
            #random.choice(random.choice([[{random.choice(search_weapon_property("Martial")):1},{"Wooden Shield":1}],[{random.choice(search_weapon_property("Martial")):1},{random.choice(search_weapon_property("Martial")):1}]])),
            random.choice([[{random.choice(search_weapon_property("Martial")):1},{"Wooden Shield":1}],[{random.choice(search_weapon_property("Martial")):1},{random.choice(search_weapon_property("Martial")):1}]]),
            random.choice([[{"Light Crossbow":1},{"Crossbow Bolts":20}],{"Handaxe":2}]),
            random.choice([dict_starting_items_kits["Dungeoneer's Pack"],dict_starting_items_kits["Explorer's Pack"]])],
        "Monk" :
            [random.choice([{"Shortsword":1},{random.choice(search_weapon_property("Simple")):1}]),
            {"Darts":10},
            random.choice([dict_starting_items_kits["Dungeoneer's Pack"],dict_starting_items_kits["Explorer's Pack"]])],
        "Paladin" :
            [random.choice([[{random.choice(search_weapon_property("Martial")):1},{"Wooden Shield":1}],[{random.choice(search_weapon_property("Martial")):1},{random.choice(search_weapon_property("Martial")):1}]]),
            random.choice([{"Javerlin":5},{random.choice(search_weapon_property("Simple")):1}]),
            {"Chain Mail":1},
            random.choice([{"Amulet (Holy Symbol)":1},{"Emblem (Holy Symbol)":1},{"Reliquart (Holy Symbol)":1}]),
            random.choice([dict_starting_items_kits["Priest's Pack"],dict_starting_items_kits["Explorer's Pack"]])],
        "Ranger" : 
            [random.choice([{"Scale Mail":1},{"Leather Armour":1}]),
            random.choice([{"Shortsword":2},[{random.choice(search_weapon_property("Simple")):1},{random.choice(search_weapon_property("Simple")):1}]]),
            {"Longbow":1},{"Arrows":20},
            random.choice([dict_starting_items_kits["Dungeoneer's Pack"],dict_starting_items_kits["Explorer's Pack"]])],
        "Rogue" :
            [random.choice([{"Rapier":1},{"Shorsword":1}]),
            random.choice([[{"Shortbow":1},{"Arrows":20}],[{"Shortsword":1}]]),
            {"Leather Armour":1},{"Dagger":2},{"Theives Tools":1},
            random.choice([dict_starting_items_kits["Burgler's Pack"],dict_starting_items_kits["Dungeoneer's Pack"],dict_starting_items_kits["Explorer's Pack"]])],
        "Sorcerer" :
            [random.choice([[{"Light Crossbow":1},{"Crossbow Bolts":20}],{random.choice(search_weapon_property("Simple")):1}]),
            random.choice([{"Component Pouch":1},{"Arcane Focus":1}]),
            {"Dagger":2},
            random.choice([dict_starting_items_kits["Dungeoneer's Pack"],dict_starting_items_kits["Explorer's Pack"]])],
        "Warlock" :
            [random.choice([[{"Light Crossbow":1},{"Crossbow Bolts":20}],{random.choice(search_weapon_property("Simple")):1}]),
            random.choice([{"Component Pouch":1},{"Arcane Focus":1}]),
            {"Dagger":2},{"Leather Armour":1},{random.choice(search_weapon_property("Simple")):1},
            random.choice([dict_starting_items_kits["Dungeoneer's Pack"],dict_starting_items_kits["Scholar's Pack"]])],
        "Wizard" :
            [random.choice([{"Quaterstaff":1},{"Dagger":1}]),
            random.choice([{"Component Pouch":1},{"Arcane Focus":1}]),
            {"Spellbook":1},
            random.choice([dict_starting_items_kits["Explorer's Pack"],dict_starting_items_kits["Scholar's Pack"]])]
            
        }   
    
    #print (proficiencies)
    classes_items = dict_starting_items_class.keys()
    print (classes_items)

    # This code is for flattening out each of dictionary enteries once they have been assigned then adding them to the starting items dictionary
   
    
    #for each value (list) in this dictionary
    for i in classes_items:
        #create a blank variable for redudent data
        redudent = []
        print (i)
        #for each element of that list attached to that dictionary entry
        for x in (dict_starting_items_class[i]):  
            #if that element is a list itself...
            if isinstance(x, list):
                #iterate through each element of that list and append it to the end of the existing larger list
                for y in x:
                    #print (y)
                    dict_starting_items_class[i].append(y)    
                redudent.append(x)
        #remove redudent nested list from items list
        for s in redudent:
            dict_starting_items_class[i].remove(s)       
        #print (dict_starting_items_class[i])
        #flattens the dicttionaries into 1 dictionary
        new_items = {}
        for y in dict_starting_items_class[i]:
            #print (y)
            new_items.update(y)
        print (new_items)

    
    
    #print (dict_starting_items_class["Druid"])


    """inventory = {}
    for key in dict_starting_items_class[char_class]:
        inventory.update(key)
    print (inventory)"""

###########################################################################
#BODY OF CODE#
###########################################################################

#print(dict_char)

#generate the "key" infomation about the character
dict_char ["Key"] = {
"Name":char_name(), 
"Race": random_dict_key(dict_race),
#"Race" : "Elf (Wood)",
#"Class": random_dict_key(dict_class),
"Class" : "Druid",
"Background": random_dict_key(dict_background)
}

#generate 
dict_char ["Attributes"] = roll_attributes(dict_char["Key"]["Race"],dict_char["Key"]["Class"])
dict_char ["Proficiencies"] = char_proficiencies(dict_char["Key"]["Race"],dict_char["Key"]["Class"],dict_char["Key"]["Background"])
dict_char ["Languages"] = char_languages(dict_char["Key"]["Race"],dict_char["Key"]["Background"])
dict_char ["Stats"] = char_stats_lvl1(dict_char["Attributes"],dict_char["Key"]["Race"],dict_char["Key"]["Class"])
#print (dict_starting_items["Barbarian"])
dict_char ["Inventory"] = char_items(dict_char["Key"]["Race"],dict_char["Key"]["Background"],dict_char["Proficiencies"])
#print (dict_char)

"""character = []
character.append(char_name())
character.append(random_dict_key(dict_race))
character.append(random_dict_key(dict_class))
character.append(random_dict_key(dict_background))
print(character)
print(roll_dice())"""