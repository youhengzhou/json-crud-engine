import os
import json
import random
import names

# player      the player name
# atr         the default attributes
# play        displays the generic information
# inputAtr    logic to set the attributes, taking a string and a number and put it to the dictionary
# outputAtr   returns the atr by getting a string and reading from the atr dict

player = 'default'
def play():
    print(
    '''
CYOA ENGINE
Welcome: {name}
    '''.format(name=player))

path = os.getcwd() + '\\database\\'

# CRUD
def create(dictionary,string):
    with open(path + string + '.json', 'w') as outfile:
        json.dump(dictionary, outfile, indent=4)
    
def retrieve(string):
    with open(path + string + '.json', 'r') as f:
        return(json.load(f))

def update(dictionary,string):
    with open(path + string + '.json', 'r') as f:
        data=(json.load(f))
        data.update(dictionary)
    with open(path + string + '.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

def delete(string):
    if os.path.exists(path + string + '.json'):
        os.remove(path + string + '.json')
    else:
        print('The selected file does not exist')

# IEO
def input_atr(dictionary,string):
    for i in range(len(string)):
            if string[i] == " ":
                word1=string[:i]
                word2=string[i+1:]
                print('i ' + word1)
                print('i ' + word2)
                dictionary[word1] = word2
                return(dictionary)

def erase_atr(dictionary,string):
    print('e ' + string)
    print('e ' + dictionary.pop(string,'atr_not_found'))
    return(dictionary)

def output_atr(dictionary,string):
    print('o '+ string)
    print('o ' + dictionary[string])
    return(dictionary[string])

# CYOA
# on an engine level, create a copy of the dictionary as the dict_template
def generate(dict_input):
    dict_output=dict(dict_input)
    keylist=[]
    for key in dict_input:
        keylist.append(key)
    for i in range(0, len(dict_input), 1):
        r = random.randint(0, len(dict_input[keylist[i]])-1)
        dict_output[keylist[i]] = dict_input[keylist[i]][r]
    return(dict_output)

# generate names
def mname():
    return(names.get_full_name(gender='male'))

def fname():
    return(names.get_full_name(gender='female'))
    