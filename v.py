import random
import sys

from engine import engine

import gladiator as gladiator

# engine.py stores the create, read, update and delete logic of the game

# CRUD offers create, retrieve, update, delete

# IEO offers input, erase, output

mem={}

sel = ''
while (sel != 'q' and 'quit'):
    print(mem)
    sel = input('\ninput selection: ')

    # generates a random number from 1 up to that number
    if sel.isnumeric():
        print(random.randint(1, int(sel)))

    # run games
    elif sel == 'gladiator':
        gladiator.play()

    elif sel == 'mname':
        print(engine.mname())

    elif sel == 'fname':
        print(engine.fname())

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
        engine.create(mem,str)
    
    # retrieve json to memory
    elif sel[0] == 'r':
        str = sel[2:]
        mem=engine.retrieve(str)

    # update json with new dict entries
    elif sel[0] == 'u':
        str = sel[2:]
        engine.update(mem,str)

    # delete json
    elif sel[0] == 'd':
        str = sel[2:]
        engine.delete(str)

    # gm commands - str being the atr name
    # insert dictionary key value pair to memory
    elif sel[0] == 'i':
        str = sel[2:]
        mem=engine.input_atr(mem,str)

    # erase dictionary key value pair from memory
    elif sel[0] == 'e':
        str = sel[2:]
        mem=engine.erase_atr(mem,str)

    # output dictionary value from key
    elif sel[0] == 'o':
        str = sel[2:]
        engine.output_atr(mem,str)
