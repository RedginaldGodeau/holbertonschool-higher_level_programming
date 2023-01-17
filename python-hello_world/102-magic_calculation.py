#!/usr/bin/python3
def magic_calculation(a, b):
    return (len(a) + len(b))

bytecode = dis.Bytecode(magic_calculation)
    for instr in bytecode:
        print(instr.opname)