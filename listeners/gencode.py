from antlr.marzo.marzoListener import marzoListener
from antlr.marzo.marzoParser import marzoParser

import asm


class GenCode(marzoListener):
    def __init__(self):
        self.r = ''
        self.stack = list()

    # PROGRAM
    def enterProgram(self, ctx: marzoParser.ProgramContext):
        self.r = asm.tpl_start_text

    # DATATYPES
    def exitInteger(self, ctx: marzoParser.IntegerContext):
        self.stack.append(asm.tpl_immediate.substitute(
            immediate=ctx.getText()))

    def exitVariable(self, ctx: marzoParser.VariableContext):
        asm.tpl_var.substitute(prev=self.stack.pop(),
                               name=ctx.getChild(0).getText())

    # ASSIGNMENTS
    def exitAssign(self, ctx: marzoParser.AssignContext):
        asm.tpl_assign.substitute(prev=self.stack.pop(), name=ctx.getText())

    # OPERATIONS
    def exitAddition(self, ctx: marzoParser.AdditionContext):
        self.stack.append(asm.tpl_addition.substitute(
            right=self.stack.pop(),
            left=self.stack.pop()
        ))
