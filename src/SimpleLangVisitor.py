# Generated from grammar/SimpleLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete generic visitor for a parse tree produced by SimpleLangParser.

class SimpleLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleLangParser#program.
    def visitProgram(self, ctx:SimpleLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#DeclaracionVariable.
    def visitDeclaracionVariable(self, ctx:SimpleLangParser.DeclaracionVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#DeclaracionFuncion.
    def visitDeclaracionFuncion(self, ctx:SimpleLangParser.DeclaracionFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Condicional.
    def visitCondicional(self, ctx:SimpleLangParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Ciclo.
    def visitCiclo(self, ctx:SimpleLangParser.CicloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Escribir.
    def visitEscribir(self, ctx:SimpleLangParser.EscribirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Expresion.
    def visitExpresion(self, ctx:SimpleLangParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#varDeclaration.
    def visitVarDeclaration(self, ctx:SimpleLangParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:SimpleLangParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ifStatement.
    def visitIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#loopStatement.
    def visitLoopStatement(self, ctx:SimpleLangParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#tipo.
    def visitTipo(self, ctx:SimpleLangParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Comparacion.
    def visitComparacion(self, ctx:SimpleLangParser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#MulDiv.
    def visitMulDiv(self, ctx:SimpleLangParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Parentesis.
    def visitParentesis(self, ctx:SimpleLangParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ID.
    def visitID(self, ctx:SimpleLangParser.IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#String.
    def visitString(self, ctx:SimpleLangParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Boolean.
    def visitBoolean(self, ctx:SimpleLangParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Int.
    def visitInt(self, ctx:SimpleLangParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#SumaResta.
    def visitSumaResta(self, ctx:SimpleLangParser.SumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#printStatement.
    def visitPrintStatement(self, ctx:SimpleLangParser.PrintStatementContext):
        return self.visitChildren(ctx)



del SimpleLangParser