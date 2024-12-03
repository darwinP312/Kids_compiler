# Generated from grammar/SimpleLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete listener for a parse tree produced by SimpleLangParser.
class SimpleLangListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleLangParser#program.
    def enterProgram(self, ctx:SimpleLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#program.
    def exitProgram(self, ctx:SimpleLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#DeclaracionVariable.
    def enterDeclaracionVariable(self, ctx:SimpleLangParser.DeclaracionVariableContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#DeclaracionVariable.
    def exitDeclaracionVariable(self, ctx:SimpleLangParser.DeclaracionVariableContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#DeclaracionFuncion.
    def enterDeclaracionFuncion(self, ctx:SimpleLangParser.DeclaracionFuncionContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#DeclaracionFuncion.
    def exitDeclaracionFuncion(self, ctx:SimpleLangParser.DeclaracionFuncionContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Condicional.
    def enterCondicional(self, ctx:SimpleLangParser.CondicionalContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Condicional.
    def exitCondicional(self, ctx:SimpleLangParser.CondicionalContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Ciclo.
    def enterCiclo(self, ctx:SimpleLangParser.CicloContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Ciclo.
    def exitCiclo(self, ctx:SimpleLangParser.CicloContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Escribir.
    def enterEscribir(self, ctx:SimpleLangParser.EscribirContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Escribir.
    def exitEscribir(self, ctx:SimpleLangParser.EscribirContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Expresion.
    def enterExpresion(self, ctx:SimpleLangParser.ExpresionContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Expresion.
    def exitExpresion(self, ctx:SimpleLangParser.ExpresionContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#varDeclaration.
    def enterVarDeclaration(self, ctx:SimpleLangParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#varDeclaration.
    def exitVarDeclaration(self, ctx:SimpleLangParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:SimpleLangParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:SimpleLangParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#ifStatement.
    def enterIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#ifStatement.
    def exitIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#loopStatement.
    def enterLoopStatement(self, ctx:SimpleLangParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#loopStatement.
    def exitLoopStatement(self, ctx:SimpleLangParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#tipo.
    def enterTipo(self, ctx:SimpleLangParser.TipoContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#tipo.
    def exitTipo(self, ctx:SimpleLangParser.TipoContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Comparacion.
    def enterComparacion(self, ctx:SimpleLangParser.ComparacionContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Comparacion.
    def exitComparacion(self, ctx:SimpleLangParser.ComparacionContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#MulDiv.
    def enterMulDiv(self, ctx:SimpleLangParser.MulDivContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#MulDiv.
    def exitMulDiv(self, ctx:SimpleLangParser.MulDivContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Parentesis.
    def enterParentesis(self, ctx:SimpleLangParser.ParentesisContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Parentesis.
    def exitParentesis(self, ctx:SimpleLangParser.ParentesisContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#ID.
    def enterID(self, ctx:SimpleLangParser.IDContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#ID.
    def exitID(self, ctx:SimpleLangParser.IDContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#String.
    def enterString(self, ctx:SimpleLangParser.StringContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#String.
    def exitString(self, ctx:SimpleLangParser.StringContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Boolean.
    def enterBoolean(self, ctx:SimpleLangParser.BooleanContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Boolean.
    def exitBoolean(self, ctx:SimpleLangParser.BooleanContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Int.
    def enterInt(self, ctx:SimpleLangParser.IntContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Int.
    def exitInt(self, ctx:SimpleLangParser.IntContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#SumaResta.
    def enterSumaResta(self, ctx:SimpleLangParser.SumaRestaContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#SumaResta.
    def exitSumaResta(self, ctx:SimpleLangParser.SumaRestaContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#printStatement.
    def enterPrintStatement(self, ctx:SimpleLangParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#printStatement.
    def exitPrintStatement(self, ctx:SimpleLangParser.PrintStatementContext):
        pass



del SimpleLangParser