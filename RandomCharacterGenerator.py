#labaries
import itertools
import random



#global variables
races = []
classes = []
attributes = ["Strength","Dexterity","Constitution","Intelegence","Wisdom","Charsima"]
skills = ["Acrobatics", "Animal Handling", "Arcana", "Atheletics", "Deception", "History", "Insight", "Intimidation","Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuassion", "Religion", "Slight of Hand", "Stealth", "Survival"]
#tools = [Artisan][Gaming Sets][Musical Instruments][Other]
tools = [["Alchemist","Brewer","Calligrapher","Cartographer","Cobbler","Cook","Glassblower","Jewler","Leatherwork","Mason","Painter","Potter","Smith","Tinker","Weaver","Woodcarver"],["Dice","Cards"],["Bagpipes","Drum","Dulcimer","Flute","Lute,","Lyre","Horn","Pan flute","Shawm","Viol"],["Disguise","Forgery","Herbalism","Navigator","Poisoners","Theives"]] 
tools_dwarf = [tools[0][1],tools[0][9],tools[0][12]]
vehicles = ["Land","Water"]
resistances = ["Acid", "Bludgeoning", "Cold", "Fire", "Force", "Lightening", "Nectrotic", "Piercing", "Poison", "Psychic" , "Radiant", "Slashing" "Thunder"]
weapons = ["Simple","Martial","Longsword","Shortsword","Longbow","Shortbow","Battleaxe","Handaxe","Lighthammer","Warhammer","Hand Crossbow","Rapier","Club","Dagger","Dart","Javelin","Mace","Quaterstaff","Scimitar","Sickle","Sling","Spear","Light Crossbow"]
armour = ["Light","Medium","Heavy","Shields"]
languages = ["Common","Evlish","Dwarvish","Giant","Gnomish","Halfling","Orc","Abyssal","Celestial","Draconic","Deep Speech","Infernal","Primordial","Sylvan","Undercommon"]     


#global dictionaries

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
"Elf (Eladrin)":[[0,2,0,1,0,0,0,30,'Medium'],[skills[10]],[],[],[],[weapons[2],weapons[3],weapons[4],weapons[5]],[],[languages[0],languages[1]],[]],
"Elf (High)":[[0,2,0,1,0,0,0,30,'Medium'],[skills[10]],[],[],[],[weapons[2],weapons[3],weapons[4],weapons[5]],[],[languages[0],languages[1],random.choice(languages[2:])],[]],
"Elf (Wood)":[[0,2,0,0,1,0,0,35,'Medium'],[skills[10]],[],[],[],[weapons[2],weapons[3],weapons[4],weapons[5]],[],[languages[0],languages[1]],[]],
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

#dict_class = {class:[hit_die,skills#,[saving throws][skills][tools][vehicles][resistances][weapons][armour][languages][traits/abilities/feats][spells]]}
dict_class = {
"Barbarian":[12,2,[attributes[0],attributes[2]],[skills[1],skills[3],skills[7],skills[10],skills[11],skills[17]],[],[],[],[weapons[0],weapons[1]],[armour[0],armour[1],armour[3]],[],[],[]],
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


"""for k,v in dict_class.items():
    print(k,v)"""

#dict_background = {background:[[skills],tools#,[tools][vehicles],languages#,[languages][traits/abilities/feats][personality trait][ideal][bond][flaw][equipment]]}
dict_background = {
"Acolyte":[[skills[6],skills[14]],0,[],2,languages,[],[],[],[],[],[]],
"Charlatan":[[skills[4],skills[15]],2,[tools[3][0],tools[3][1]],0,[],[],[],[],[],[],[]],
"Criminal/Spy":[[skills[4],skills[16]],1,tools[1],0,[],[],[],[],[],[],[]],
"Entertainer":[[skills[0],skills[12]],2,[tools[3][0],random.choice(tools[2])],[],0,[],[],[],[],[],[],[],[]],
"Folk Hero":[[skills[1]],[skills[17]],1,tools[0],[vehicles[0]],0,[],[],[],[],[],[],[]],
"Guild Artisan":[[skills[6],skills[11]],1,tools[0],[],1,languages,[],[],[],[],[],[]],
"Hermit":[[skills[9],skills[14]],1,[tools[3][2]],[],1,languages,[],[],[],[],[],[]],
"Noble":[[skills[5],skills[13]],1,tools[1],[],1,languages,[],[],[],[],[],[]],
"Outlander":[[skills[3],skills[17]],1,tools[2],[],1,languages,[],[],[],[],[],[]],
"Sage":[[skills[2],skills[5]],0,[],[],2,languages,[],[],[],[],[],[]],
"Sailor":[[skills[3],skills[11]],1,[tools[3][3]],[vehicles[1]],0,[],[],[],[],[],[],[]],
"Soldier":[[skills[3],skills[7]],1,tools[1],[vehicles[0]],0,[],[],[],[],[],[],[]],
"Urchin":[[skills[15],skills[16]],2,[tools[3][0],tools[3][4]],0,[],[],[],[],[],[],[]]
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





###########################################################################
#BODY OF CODE#
###########################################################################
character = []
character.append(char_name())
character.append(random_dict_key(dict_race))
character.append(random_dict_key(dict_class))
character.append(random_dict_key(dict_background))
print(character)
print(roll_dice())