import os
import json

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
