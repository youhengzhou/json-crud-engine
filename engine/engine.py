# CRUDIPIE 2021 6 27
# engine imports
import os
import json
import random
import names

# add games to use the engine here
# import space_prison

# JSON DICTIONARY DATABASE ENGINE
#
#   database
#       JSON goes here
#   
#   engine.py

# database path
path = os.getcwd() + '\\database\\'

# set database path
def set_path(string):
    path = os.getcwd() + string

# call python random number generator
def random_num(number):
    return(random.randint(1, int(number)))

# CRUPD
def create(dictionary_name):
    blank_dictionary = {}
    with open(path + dictionary_name + '.json', 'w') as outfile:
        json.dump(blank_dictionary, outfile, indent=4)

def retrieve(dictionary_name):
    with open(path + dictionary_name + '.json', 'r') as f:
        return(json.load(f))

def update(dictionary, dictionary_name):
    with open(path + dictionary_name + '.json', 'w') as outfile:
        json.dump(dictionary, outfile, indent=4)

def patch(dictionary, dictionary_name):
    with open(path + dictionary_name + '.json', 'r') as f:
        data=(json.load(f))
        data.update(dictionary)
        with open(path + dictionary_name + '.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)

def delete(dictionary_name):
    if os.path.exists(path + dictionary_name + '.json'):
        os.remove(path + dictionary_name + '.json')
    else:
        print('The selected file does not exist')

# IEO
def input_atr(dictionary, string):
    for i in range(len(string)):
            if string[i] == " ":
                word1=string[:i]
                word2=string[i+1:]
                print('i ' + word1)
                print('i ' + word2)
                dictionary[word1] = word2
                return(dictionary)

def erase_atr(dictionary, string):
    print('e ' + string)
    print('e ' + dictionary.pop(string,'atr_not_found'))
    return(dictionary)

def output_atr(dictionary, string):
    print('o '+ string)
    print('o ' + dictionary[string])
    return(dictionary[string])

# CYOA
# on an engine level, create a copy of the dictionary as the dict_template
def generate(dict_input, gender):
    dict_output=dict(dict_input)
    keylist=[]
    for key in dict_input:
        keylist.append(key)
    for i in range(0, len(dict_input), 1):
        r = random.randint(0, len(dict_input[keylist[i]])-1)
        dict_output[keylist[i]] = dict_input[keylist[i]][r]
    if gender == 'male':
        dict_output['name'] = mname()
    if gender == 'female':
        dict_output['name'] = fname()
    return(dict_output)

# generate names
def mname():
    return(names.get_full_name(gender='male'))

def fname():
    return(names.get_full_name(gender='female'))

# runner of engine.py which stores the create, read, update, patch and delete logic
# CRUPD offers create, retrieve, update, patch, delete
# IEO offers input, erase, output
def run():
    games=['sp']
    mem={} 
    sel = ''
    while (sel != 'q' and 'quit' and 'exit'):
        print(mem)
        sel = input('\ninput selection: ')

        # generates a random number from 1 up to that number
        if sel.isnumeric():
            print(random_num(sel))

        # edit the path of the database
        elif sel[0:4] == 'path': # from 0 to the 4th place that is the space to pick 0 to 3
            str = sel[5:] # the 5th place is where the word starts
            set_path(str)

        # run games
        elif sel in games:
            sel.play()

        elif sel == 'mname':
            print(mname())

        elif sel == 'fname':
            print(fname())

        # prints memory
        elif sel == 'pm':
            print(mem)

        # checking for no inputs before sel[0]
        elif sel == '':
            print('')

        # CRUD - str being the name of the database file
        # create json
        elif sel[0] == 'c':
            str = sel[2:]
            create(str)
        
        # retrieve json to memory
        elif sel[0] == 'r':
            str = sel[2:]
            mem=retrieve(str)

        # update json with a new dictionary
        elif sel[0] == 'u':
            str = sel[2:]
            update(mem,str)

        # patch json with new dict key and value entries
        elif sel[0] == 'p':
            str = sel[2:]
            patch(mem,str)

        # delete json
        elif sel[0] == 'd':
            str = sel[2:]
            delete(str)

        # gm commands - str being the atr name
        # insert dictionary key value pair to memory
        elif sel[0] == 'i':
            str = sel[2:]
            mem=input_atr(mem,str)

        # erase dictionary key value pair from memory
        elif sel[0] == 'e':
            str = sel[2:]
            mem=erase_atr(mem,str)

        # output dictionary value from key
        elif sel[0] == 'o':
            str = sel[2:]
            output_atr(mem,str)
    
    print('exit')
