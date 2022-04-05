#labaries
import itertools
import random

from numpy import roll



#global variables
races = []
classes = []
attributes = ["Strength","Dexterity","Constitution","Intelegence","Wisdom","Charsima"]
skills = ["Acrobatics", "Animal Handling", "Arcana", "Atheletics", "Deception", "History", "Insight", "Intimidation","Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuassion", "Religion", "Slight of Hand", "Stealth", "Survival"]
#tools = [Artisan][Gaming Sets][Musical Instruments][Other]
tools = [["Alchemist Tools","Brewer Tools","Calligrapher Tools","Cartographer Tools","Cobbler Tools","Cook Tools","Glassblower Tools","Jewler Tools","Leatherwork Tools","Mason Tools","Painter Tools","Potter Tools","Smith Tools","Tinker Tools","Weaver Tools","Woodcarver Tools"],["Dice","Cards"],["Bagpipes","Drum","Dulcimer","Flute","Lute,","Lyre","Horn","Pan flute","Shawm","Viol"],["Disguise Kit","Forgery Kit","Herbalism Kit","Navigator Tools","Poisoners Kit","Theives Tools"]] 
tools_dwarf = [tools[0][1],tools[0][9],tools[0][12]]
vehicles = ["Land Vehicles","Water Vehicles"]
resistances = ["Acid", "Bludgeoning", "Cold", "Fire", "Force", "Lightening", "Nectrotic", "Piercing", "Poison", "Psychic" , "Radiant", "Slashing" "Thunder"]
weapons = ["Simple Weapons","Martial Weapons","Longsword","Shortsword","Longbow","Shortbow","Battleaxe","Handaxe","Lighthammer","Warhammer","Hand Crossbow","Rapier","Club","Dagger","Dart","Javelin","Mace","Quaterstaff","Scimitar","Sickle","Sling","Spear","Light Crossbow"]
armour = ["Light Armpur","Medium Armour","Heavy Armour","Shields"]
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



#dict_attributesscores determines the attribute score bonuses b

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

#dict_class = {class:[hit_die],skills#,[saving throws][skills][tools][vehicles][resistances][weapons][armour][languages][traits/abilities/feats][spells]]}
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

    ##################################### - Create 1 consolidated dictionary - #####################################


    char_proficiencies = char_skills
    char_proficiencies.extend(char_tools)
    char_proficiencies.extend(char_vehicles)
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
    

###########################################################################
#BODY OF CODE#
###########################################################################

#print(dict_char)

#generate the "key" infomation about the character
dict_char ["Key"] = {
"Name":char_name(), 
"Race": random_dict_key(dict_race),
#"Race" : "Elf (Wood)",
"Class": random_dict_key(dict_class),
"Background": random_dict_key(dict_background)
}

#generate 
dict_char ["Attributes"] = roll_attributes(dict_char["Key"]["Race"],dict_char["Key"]["Class"])
dict_char ["Proficiencies"] = char_proficiencies(dict_char["Key"]["Race"],dict_char["Key"]["Class"],dict_char["Key"]["Background"])
dict_char ["Languages"] = char_languages(dict_char["Key"]["Race"],dict_char["Key"]["Background"])
dict_char ["Stats"] = char_stats_lvl1(dict_char["Attributes"],dict_char["Key"]["Race"],dict_char["Key"]["Class"])

print (dict_char)

"""character = []
character.append(char_name())
character.append(random_dict_key(dict_race))
character.append(random_dict_key(dict_class))
character.append(random_dict_key(dict_background))
print(character)
print(roll_dice())"""