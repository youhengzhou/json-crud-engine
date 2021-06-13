import random
from engine import engine
from engine.char import char
from engine.locale import locale

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

    # prints memory
    elif sel == 'pm':
        print(mem)

    # CRUD - str being the name of the database file
    elif sel[0] == 'c':
        str = sel[2:]
        engine.create(mem,str)
    
    elif sel[0] == 'cb':
        str = sel[2:]
        engine.create_blank(str)
    
    elif sel[0] == 'r':
        str = sel[2:]
        mem=engine.retrieve(str)

    elif sel[0] == 'u':
        str = sel[2:]
        engine.update(mem,str)

    elif sel[0] == 'd':
        str = sel[2:]
        engine.delete(str)

    # gm commands - str being the atr name
    elif sel[0] == 'i':
        str = sel[2:]
        mem=engine.input_atr(mem,str)

    elif sel[0] == 'e':
        str = sel[2:]
        mem=engine.erase_atr(mem,str)

    elif sel[0] == 'o':
        str = sel[2:]
        engine.output_atr(mem,str)
