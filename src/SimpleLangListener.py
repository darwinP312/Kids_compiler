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


    # Enter a parse tree produced by SimpleLangParser#aumentar.
    def enterAumentar(self, ctx:SimpleLangParser.AumentarContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#aumentar.
    def exitAumentar(self, ctx:SimpleLangParser.AumentarContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#disminuir.
    def enterDisminuir(self, ctx:SimpleLangParser.DisminuirContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#disminuir.
    def exitDisminuir(self, ctx:SimpleLangParser.DisminuirContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Or.
    def enterOr(self, ctx:SimpleLangParser.OrContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Or.
    def exitOr(self, ctx:SimpleLangParser.OrContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#MenorIgualQue.
    def enterMenorIgualQue(self, ctx:SimpleLangParser.MenorIgualQueContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#MenorIgualQue.
    def exitMenorIgualQue(self, ctx:SimpleLangParser.MenorIgualQueContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Parentesis.
    def enterParentesis(self, ctx:SimpleLangParser.ParentesisContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Parentesis.
    def exitParentesis(self, ctx:SimpleLangParser.ParentesisContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#String.
    def enterString(self, ctx:SimpleLangParser.StringContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#String.
    def exitString(self, ctx:SimpleLangParser.StringContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#MayorIgualQue.
    def enterMayorIgualQue(self, ctx:SimpleLangParser.MayorIgualQueContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#MayorIgualQue.
    def exitMayorIgualQue(self, ctx:SimpleLangParser.MayorIgualQueContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Int.
    def enterInt(self, ctx:SimpleLangParser.IntContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Int.
    def exitInt(self, ctx:SimpleLangParser.IntContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#And.
    def enterAnd(self, ctx:SimpleLangParser.AndContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#And.
    def exitAnd(self, ctx:SimpleLangParser.AndContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#DiferenteDe.
    def enterDiferenteDe(self, ctx:SimpleLangParser.DiferenteDeContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#DiferenteDe.
    def exitDiferenteDe(self, ctx:SimpleLangParser.DiferenteDeContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#IgualQue.
    def enterIgualQue(self, ctx:SimpleLangParser.IgualQueContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#IgualQue.
    def exitIgualQue(self, ctx:SimpleLangParser.IgualQueContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#ID.
    def enterID(self, ctx:SimpleLangParser.IDContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#ID.
    def exitID(self, ctx:SimpleLangParser.IDContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#MayorQue.
    def enterMayorQue(self, ctx:SimpleLangParser.MayorQueContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#MayorQue.
    def exitMayorQue(self, ctx:SimpleLangParser.MayorQueContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Boolean.
    def enterBoolean(self, ctx:SimpleLangParser.BooleanContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Boolean.
    def exitBoolean(self, ctx:SimpleLangParser.BooleanContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#MenorQue.
    def enterMenorQue(self, ctx:SimpleLangParser.MenorQueContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#MenorQue.
    def exitMenorQue(self, ctx:SimpleLangParser.MenorQueContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#printStatement.
    def enterPrintStatement(self, ctx:SimpleLangParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#printStatement.
    def exitPrintStatement(self, ctx:SimpleLangParser.PrintStatementContext):
        pass



del SimpleLangParser