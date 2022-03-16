from antlr4 import *
from antlr.marzo.marzoParser import marzoParser
from antlr.marzo.marzoLexer import marzoLexer
from listeners.gencode import GenCode
from listeners.gendata import GenData

import sys


def main():
    parser = marzoParser(CommonTokenStream(
        marzoLexer(FileStream("input.txt"))))
    tree = parser.program()

    walker = ParseTreeWalker()
    gencode = GenCode()
    gendata = GenData()
    
    walker.walk(gencode, tree)
    walker.walk(gendata, tree)

    with open('test.asm', 'w') as writer:
        writer.write(gencode.r)
        writer.write(gendata.r)


if __name__ == '__main__':
    main()
