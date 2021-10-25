# JSON engine 21 9 16
#   database
#       eng.json
#   engine
#       eng.py
import os
import json

path = os.getcwd() + '\\database\\'

def set_path(string):
    global path
    path = os.getcwd() + string

def didsplay_kv(dictionary, key, value):
    dictionary[key] = value
    return dictionary

def create(*args):
    blank_dictionary = {}
    path_string = ''
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string)==False:
        os.makedirs(path + path_string)
    with open(path + path_string + 'eng.json', 'w') as outfile:
        json.dump(blank_dictionary, outfile, indent=4)

def retrieve(*args):
    path_string = ''
    if (args):
        path_string = str(args[0]) + '\\'
    with open(path + path_string + 'eng.json', 'r') as f:
        return(json.load(f))

def retrieve_k(key, *args):
    path_string = ''
    if (args):
        path_string = str(args[0]) + '\\'
    with open(path + path_string + 'eng.json', 'r') as f:
        return(json.load(f)[key])

def update(dictionary, *args):
    path_string = ''
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string)==False:
        os.makedirs(path + path_string)
    with open(path + path_string + 'eng.json', 'w') as outfile:
        json.dump(dictionary, outfile, indent=4)

def update_kv(key, value, *args):
    path_string = ''
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string)==False:
        os.makedirs(path + path_string)
    with open(path + path_string + 'eng.json', 'w') as outfile:
        json.dump({key: value}, outfile, indent=4)

def patch(dictionary, *args):
    path_string = ''
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string)==False:
        os.makedirs(path + path_string)
    with open(path + path_string + 'eng.json', 'r') as f:
        data=(json.load(f))
        data.update(dictionary)
        with open(path + path_string + 'eng.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)

def patch_kv(key, value, *args):
    path_string = ''
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string)==False:
        os.makedirs(path + path_string)
    with open(path + path_string + 'eng.json', 'r') as f:
        data=(json.load(f))
        data.update({key: value})
        with open(path + path_string + 'eng.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)

def delete(*args):
    path_string = ''
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string + 'eng.json'):
        os.remove(path + 'eng.json')
    else:
        print('The selected file does not exist')

def delete_k(key, *args):
    path_string = ''
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string + 'eng.json'):
        with open(path + path_string + 'eng.json', 'r') as f:
            data=(json.load(f))
            data.pop(key)
            with open(path + path_string + 'eng.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
    else:
        print('The selected file does not exist')

def display(path_string, *args):
    path_string = ''
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string + 'eng.json'):
        with open(path + path_string + 'eng.json', 'r') as f:
            print(json.load(f))
    else:
        print('The selected file does not exist')

def display_key(key, *args):
    path_string = ''
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string + 'eng.json'):
        with open(path + path_string + 'eng.json', 'r') as f:
            print(key + ' ' + str(json.load(f)[key]))
    else:
        print('The selected file does not exist')

def display_nkv(key, *args):
    path_string = ''
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string + 'eng.json'):
        with open(path + path_string + 'eng.json', 'r') as f:
            data = json.load(f)
            data.pop(key,'key not found')
            print(data)
    else:
        print('The selected file does not exist')

def displayfull(*args):
    path_string = ''
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string + 'eng.json'):
        with open(path + path_string + 'eng.json', 'r') as f:
            print(json.dumps(json.load(f), indent=4))
    else:
        print('The selected file does not exist')

def displayfull_nkv(key, *args):
    path_string = ''
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string + 'eng.json'):
        with open(path + path_string + 'eng.json', 'r') as f:
            data = json.load(f)
            data.pop(key,'key not found')
            print(json.dumps(data, indent=4))
    else:
        print('The selected file does not exist')
