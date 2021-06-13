import os
import json

# player      the player name
# atr         the default attributes
# logo        displays the logo
# setAtr      logic to set the attributes, taking a string and a number and put it to the dictionary
# readAtr     returns the atr by getting a string and reading from the atr dict

player = 'default'

atr = {
    'hpt': 0,
    'atk': 0,
    'def': 0,
    'str': 0,
    'wgt': 0,
    'mov': 0,
}

def print_logo():
    print(
    '''
CYOA ENGINE
Welcome: {name}
    '''.format(name=player))

path = os.getcwd() + '\\database\\'

# CRUD
def create(dict,str):
    with open(path + str + '.json', 'w') as outfile:
        json.dump(dict, outfile)

def create_blank(str):
    with open(path + str + '.json', 'w') as outfile:
        json.dump(outfile)
    
def retrieve(str):
    with open(path + str + '.json', 'r') as f:
        return(json.load(f))

def update(dict,str):
    with open(path + str + '.json', 'r') as f:
        data=(json.load(f))
        data.update(dict)
        with open(path + str + '.json', 'w') as outfile:
            json.dump(dict, outfile)

def delete(str):
    if os.path.exists(path + str + '.json'):
        os.remove(path + str + '.json')
    else:
        print('The selected file does not exist')

# IEO
def input_atr(dict,str):
    for i in range(len(str)):
            if str[i] == " ":
                word1=str[:i]
                word2=str[i+1:]
                print('i ' + word1)
                print('i ' + word2)
                dict[word1] = word2
                return(dict)

def erase_atr(dict,str):
    print('e ' + str)
    print('e ' + dict.pop(str,'atr_not_found'))
    return(dict)

def output_atr(dict,str):
    print('o '+ str)
    print('o ' + dict[str])
    return(dict[str])
