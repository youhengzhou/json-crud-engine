import os
import json

path = os.getcwd() + '\\jdb\\'
path_string = ''

def set_path(string):
    global path
    path = os.getcwd() + string

def dictionary_kv(dictionary, key, value):
    dictionary[key] = value
    return dictionary

def set_path_string(args, create_flag):
    global path_string
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string) == False:
        if create_flag == True:
            os.makedirs(path + path_string)
        else:
            return False
    return path_string

def create(dictionary, *args):
    path_string = set_path_string(args, True)
    with open(path + path_string + 'eng.json', 'w') as outfile:
        json.dump(dictionary, outfile, indent=4)

def retrieve(*args):
    path_string = set_path_string(args, False)
    if path_string == False:
        return False
    with open(path + path_string + 'eng.json', 'r') as f:
        return(json.load(f))

def retrieve_k(key, *args):
    path_string = set_path_string(args, False)
    if path_string == False:
        return False
    with open(path + path_string + 'eng.json', 'r') as f:
        if key in json.load(f):
            with open(path + path_string + 'eng.json', 'r') as f:
                return(json.load(f)[key])
        else:
            return False

def update(dictionary, *args):
    path_string = set_path_string(args, False)
    if path_string == False:
        return False
    with open(path + path_string + 'eng.json', 'w') as outfile:
        json.dump(dictionary, outfile, indent=4)
        return True

def update_kv(key, value, *args):
    path_string = set_path_string(args, False)
    if path_string == False:
        return False
    with open(path + path_string + 'eng.json', 'w') as outfile:
        json.dump({key: value}, outfile, indent=4)
        return True

def patch(dictionary, *args):
    path_string = set_path_string(args, False)
    if path_string == False:
        return False
    with open(path + path_string + 'eng.json', 'r') as f:
        data=(json.load(f))
        data.update(dictionary)
        with open(path + path_string + 'eng.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
            return True

def patch_kv(key, value, *args):
    path_string = set_path_string(args, False)
    if path_string == False:
        return False
    with open(path + path_string + 'eng.json', 'r') as f:
        data=(json.load(f))
        data.update({key: value})
        with open(path + path_string + 'eng.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
            return True

def delete(*args):
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string + 'eng.json'):
        os.remove(path + path_string + 'eng.json')
        os.rmdir(path + path_string)
        return True
    else:
        print('The selected file does not exist')
        return False

def delete_k(key, *args):
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string + 'eng.json'):
        with open(path + path_string + 'eng.json', 'r') as f:
            if key in json.load(f):
                data = json.load(f)
                data.pop(key)
                with open(path + path_string + 'eng.json', 'w') as outfile:
                    json.dump(data, outfile, indent=4)
                    return True
            else:
                print('The selected key does not exist')
                return False
    else:
        print('The selected file does not exist')
        return False

def display(*args):
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string + 'eng.json'):
        with open(path + path_string + 'eng.json', 'r') as f:
            print(json.load(f))
            return True
    else:
        print('The selected file does not exist')
        return False

def display_key(key, *args):
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string + 'eng.json'):
        with open(path + path_string + 'eng.json', 'r') as f:
            if key in json.load(f):
                print(key + ': ' + str(json.load(f)[key]))
                return True
            else:
                print('The selected key does not exist')
                return False
    else:
        print('The selected file does not exist')
        return False

def display_nkv(key, *args):
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string + 'eng.json'):
        with open(path + path_string + 'eng.json', 'r') as f:
            if key in json.load(f):
                data = json.load(f)
                data.pop(key,'key not found')
                print(data)
                return True
            else:
                print('The selected key does not exist')
                return False
    else:
        print('The selected file does not exist')
        return False

def display_ind(*args):
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string + 'eng.json'):
        with open(path + path_string + 'eng.json', 'r') as f:
            print(json.dumps(json.load(f), indent=4))
    else:
        print('The selected file does not exist')

def display_ind_nkv(key, *args):
    if (args):
        path_string = str(args[0]) + '\\'
    if os.path.exists(path + path_string + 'eng.json'):
        with open(path + path_string + 'eng.json', 'r') as f:
            data = json.load(f)
            data.pop(key,'key not found')
            print(json.dumps(data, indent=4))
    else:
        print('The selected file does not exist')
