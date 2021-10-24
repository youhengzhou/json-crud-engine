import random
from engine import main

def random_num(number):
    return(random.randint(1, int(number)))

def local_create(dictionary, string=''):
    dictionary = {}
    if string=='':
        print('lc ')
        return(dictionary)
    for i in range(len(string)):
            if string[i] == " ":
                word1=string[:i]
                word2=string[i+1:]
                print('lc ' + word1)
                print('lc ' + word2)
                dictionary[word1] = word2
                return(dictionary)

def local_retrieve(dictionary, string=''):
    if string=='':
        print('lr ' + str(dictionary))
        return(dictionary)
    else:
        print('lr '+ string)
        print('lr ' + dictionary[string])
        return(dictionary[string])

def local_update(dictionary, string=''):
    for i in range(len(string)):
            if string[i] == " ":
                word1=string[:i]
                word2=string[i+1:]
                print('lu ' + word1)
                print('lu ' + word2)
                dictionary[word1] = word2
                return(dictionary)

def local_delete(dictionary, string):
    print('ld ' + string)
    print('ld ' + dictionary.pop(string,'atr_not_found'))
    return(dictionary)

def tally_atr(dictionary):
    print('t')
    count = 0
    for value in dictionary.values():
        if isinstance(value, (int, float)):
            count = count + float(value)
    return(count)

def input_eng(sel,mem):
    if sel == 'e':
        return

    elif sel[:2] == 'ec':
        eng.c(sel[3:])
    
    elif sel[:2] == 'er':
        mem=eng.r(sel[3:])

    elif sel[:2] == 'eu':
        eng.u(mem,sel[3:])

    elif sel[:2] == 'ep':
        eng.p(mem,sel[3:])

    elif sel[:2] == 'ed':
        eng.d(mem,sel[3:])

def input_leng(sel,mem):
    if sel == 'l':
        return mem

    elif sel[:2] == 'lc':
        mem=local_create(mem,sel[3:])

    elif sel[:2] == 'lr':
        str = sel[3:]
        if str == None:
            str = None
        local_retrieve(mem,str)

    elif sel[:2] == 'lu':
        mem=local_update(mem,sel[3:])

    elif sel[:2] == 'ld':
        mem=local_delete(mem,sel[3:])

    return mem

def input_sel(sel,mem):
    if sel == None:
        print('')

    elif sel.isnumeric():
        print(random_num(sel))

    elif sel[0:4] == 'path':
        str = sel[5:]
        eng.set_path(str)

    elif sel == 'pm':
        print(mem)

    elif sel[0] == 'e':
        input_eng(sel,mem)

    elif sel[0] == 'l':
        mem=input_leng(sel,mem)

    elif sel[0] == 't':
        print(tally_atr(mem))

    elif sel[0] == 'h':
        print('c r u p d lc lr lu ld path t')

    return mem

def run():
    sel = ''
    mem={}
    while (sel != 'q' and 'quit' and 'exit'):
        sel = input('\n> ')
        mem=input_sel(sel,mem)
        print(mem)

    print('exit')
    