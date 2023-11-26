#!/usr/bin/python3
import dis
import marshal

def list_names():
    with open('hidden_4.pyc', 'rb') as file:
        code = marshal.load(file)

    instructions = dis.get_instructions(code)

    names = [instruction.argval for instruction in instructions
             if instruction.opname == 'LOAD_GLOBAL' and not instruction.argval.startswith('__')]

    for name in sorted(set(names)):
        print(name)

if __name__ == '__main__':
    list_names()
