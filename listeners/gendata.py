from antlr.marzo.marzoListener import marzoListener
from antlr.marzo.marzoParser import marzoParser

import asm


class GenData(marzoListener):
    def __init__(self):
        self.r = ''

    # PROGRAM
    def enterProgram(self, ctx: marzoParser.ProgramContext):
        self.r = asm.tpl_start_data

    # DATATYPES
    def enterDeclare_int(self, ctx: marzoParser.Declare_intContext):
        self.r += asm.tpl_var.substitute(name=ctx.getChild(1).getText())
