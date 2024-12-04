# Generated from grammar/SimpleLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,189,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        5,0,29,8,0,10,0,12,0,32,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,48,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,1,3,5,3,62,8,3,10,3,12,3,65,9,3,1,3,1,3,1,4,1,4,1,4,1,
        4,1,4,1,4,5,4,75,8,4,10,4,12,4,78,9,4,1,4,1,4,1,4,1,4,5,4,84,8,4,
        10,4,12,4,87,9,4,1,4,3,4,90,8,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,98,8,
        5,10,5,12,5,101,9,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,
        1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,140,
        8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,178,
        8,11,10,11,12,11,181,9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,0,1,
        22,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,1,1,0,13,15,206,0,26,1,
        0,0,0,2,47,1,0,0,0,4,49,1,0,0,0,6,55,1,0,0,0,8,68,1,0,0,0,10,91,
        1,0,0,0,12,104,1,0,0,0,14,106,1,0,0,0,16,112,1,0,0,0,18,118,1,0,
        0,0,20,124,1,0,0,0,22,139,1,0,0,0,24,182,1,0,0,0,26,30,5,1,0,0,27,
        29,3,2,1,0,28,27,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,
        0,31,33,1,0,0,0,32,30,1,0,0,0,33,34,5,2,0,0,34,1,1,0,0,0,35,48,3,
        4,2,0,36,48,3,6,3,0,37,48,3,8,4,0,38,48,3,10,5,0,39,48,3,24,12,0,
        40,48,3,14,7,0,41,48,3,16,8,0,42,48,3,18,9,0,43,48,3,20,10,0,44,
        45,3,22,11,0,45,46,5,3,0,0,46,48,1,0,0,0,47,35,1,0,0,0,47,36,1,0,
        0,0,47,37,1,0,0,0,47,38,1,0,0,0,47,39,1,0,0,0,47,40,1,0,0,0,47,41,
        1,0,0,0,47,42,1,0,0,0,47,43,1,0,0,0,47,44,1,0,0,0,48,3,1,0,0,0,49,
        50,3,12,6,0,50,51,5,32,0,0,51,52,5,4,0,0,52,53,3,22,11,0,53,54,5,
        3,0,0,54,5,1,0,0,0,55,56,5,5,0,0,56,57,5,32,0,0,57,58,5,6,0,0,58,
        59,5,7,0,0,59,63,5,8,0,0,60,62,3,2,1,0,61,60,1,0,0,0,62,65,1,0,0,
        0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,
        5,9,0,0,67,7,1,0,0,0,68,69,5,10,0,0,69,70,5,6,0,0,70,71,3,22,11,
        0,71,72,5,7,0,0,72,76,5,8,0,0,73,75,3,2,1,0,74,73,1,0,0,0,75,78,
        1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,
        79,89,5,9,0,0,80,81,5,11,0,0,81,85,5,8,0,0,82,84,3,2,1,0,83,82,1,
        0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,
        85,1,0,0,0,88,90,5,9,0,0,89,80,1,0,0,0,89,90,1,0,0,0,90,9,1,0,0,
        0,91,92,5,12,0,0,92,93,5,6,0,0,93,94,3,22,11,0,94,95,5,7,0,0,95,
        99,5,8,0,0,96,98,3,2,1,0,97,96,1,0,0,0,98,101,1,0,0,0,99,97,1,0,
        0,0,99,100,1,0,0,0,100,102,1,0,0,0,101,99,1,0,0,0,102,103,5,9,0,
        0,103,11,1,0,0,0,104,105,7,0,0,0,105,13,1,0,0,0,106,107,5,16,0,0,
        107,108,5,6,0,0,108,109,5,32,0,0,109,110,5,7,0,0,110,111,5,3,0,0,
        111,15,1,0,0,0,112,113,5,17,0,0,113,114,5,6,0,0,114,115,5,32,0,0,
        115,116,5,7,0,0,116,117,5,3,0,0,117,17,1,0,0,0,118,119,5,18,0,0,
        119,120,5,6,0,0,120,121,5,32,0,0,121,122,5,7,0,0,122,123,5,3,0,0,
        123,19,1,0,0,0,124,125,5,19,0,0,125,126,5,6,0,0,126,127,5,32,0,0,
        127,128,5,7,0,0,128,129,5,3,0,0,129,21,1,0,0,0,130,131,6,11,-1,0,
        131,132,5,6,0,0,132,133,3,22,11,0,133,134,5,7,0,0,134,140,1,0,0,
        0,135,140,5,32,0,0,136,140,5,33,0,0,137,140,5,34,0,0,138,140,5,35,
        0,0,139,130,1,0,0,0,139,135,1,0,0,0,139,136,1,0,0,0,139,137,1,0,
        0,0,139,138,1,0,0,0,140,179,1,0,0,0,141,142,10,17,0,0,142,143,5,
        20,0,0,143,178,3,22,11,18,144,145,10,16,0,0,145,146,5,21,0,0,146,
        178,3,22,11,17,147,148,10,15,0,0,148,149,5,22,0,0,149,178,3,22,11,
        16,150,151,10,14,0,0,151,152,5,23,0,0,152,178,3,22,11,15,153,154,
        10,13,0,0,154,155,5,24,0,0,155,178,3,22,11,14,156,157,10,12,0,0,
        157,158,5,25,0,0,158,178,3,22,11,13,159,160,10,11,0,0,160,161,5,
        25,0,0,161,178,3,22,11,12,162,163,10,10,0,0,163,164,5,26,0,0,164,
        178,3,22,11,11,165,166,10,8,0,0,166,167,5,27,0,0,167,178,3,22,11,
        9,168,169,10,7,0,0,169,170,5,28,0,0,170,178,3,22,11,8,171,172,10,
        6,0,0,172,173,5,29,0,0,173,178,3,22,11,7,174,175,10,5,0,0,175,176,
        5,30,0,0,176,178,3,22,11,6,177,141,1,0,0,0,177,144,1,0,0,0,177,147,
        1,0,0,0,177,150,1,0,0,0,177,153,1,0,0,0,177,156,1,0,0,0,177,159,
        1,0,0,0,177,162,1,0,0,0,177,165,1,0,0,0,177,168,1,0,0,0,177,171,
        1,0,0,0,177,174,1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,179,180,
        1,0,0,0,180,23,1,0,0,0,181,179,1,0,0,0,182,183,5,31,0,0,183,184,
        5,6,0,0,184,185,3,22,11,0,185,186,5,7,0,0,186,187,5,3,0,0,187,25,
        1,0,0,0,10,30,47,63,76,85,89,99,139,177,179
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Empecemos!'", "'Hasta luego!'", "';'", 
                     "'='", "'hacer esto'", "'('", "')'", "'{'", "'}'", 
                     "'Si pasa esto'", "'Sino'", "'Repetir mientras que'", 
                     "'numero'", "'texto'", "'logico'", "'aumentar'", "'disminuir'", 
                     "'potencia'", "'raizCuadrada'", "'y'", "'o'", "'menor que'", 
                     "'mayor que'", "'igual que'", "'menor igual a'", "'diferente de'", 
                     "'*'", "'/'", "'+'", "'-'", "'escribir'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "STRING", "BOOL", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_varDeclaration = 2
    RULE_functionDeclaration = 3
    RULE_ifStatement = 4
    RULE_loopStatement = 5
    RULE_tipo = 6
    RULE_aumentar = 7
    RULE_disminuir = 8
    RULE_potencia = 9
    RULE_raizCuadrada = 10
    RULE_expr = 11
    RULE_printStatement = 12

    ruleNames =  [ "program", "statement", "varDeclaration", "functionDeclaration", 
                   "ifStatement", "loopStatement", "tipo", "aumentar", "disminuir", 
                   "potencia", "raizCuadrada", "expr", "printStatement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    ID=32
    INT=33
    STRING=34
    BOOL=35
    WS=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SimpleLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(SimpleLangParser.T__0)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 66573038688) != 0):
                self.state = 27
                self.statement()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self.match(SimpleLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclaracionVariableContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def varDeclaration(self):
            return self.getTypedRuleContext(SimpleLangParser.VarDeclarationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionVariable" ):
                listener.enterDeclaracionVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionVariable" ):
                listener.exitDeclaracionVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionVariable" ):
                return visitor.visitDeclaracionVariable(self)
            else:
                return visitor.visitChildren(self)


    class CicloContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def loopStatement(self):
            return self.getTypedRuleContext(SimpleLangParser.LoopStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCiclo" ):
                listener.enterCiclo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCiclo" ):
                listener.exitCiclo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCiclo" ):
                return visitor.visitCiclo(self)
            else:
                return visitor.visitChildren(self)


    class ExpresionContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)


    class DisminuirEnUnoContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def disminuir(self):
            return self.getTypedRuleContext(SimpleLangParser.DisminuirContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisminuirEnUno" ):
                listener.enterDisminuirEnUno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisminuirEnUno" ):
                listener.exitDisminuirEnUno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisminuirEnUno" ):
                return visitor.visitDisminuirEnUno(self)
            else:
                return visitor.visitChildren(self)


    class PotenciasContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def potencia(self):
            return self.getTypedRuleContext(SimpleLangParser.PotenciaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPotencias" ):
                listener.enterPotencias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPotencias" ):
                listener.exitPotencias(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPotencias" ):
                return visitor.visitPotencias(self)
            else:
                return visitor.visitChildren(self)


    class AumentarEnUnoContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def aumentar(self):
            return self.getTypedRuleContext(SimpleLangParser.AumentarContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAumentarEnUno" ):
                listener.enterAumentarEnUno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAumentarEnUno" ):
                listener.exitAumentarEnUno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAumentarEnUno" ):
                return visitor.visitAumentarEnUno(self)
            else:
                return visitor.visitChildren(self)


    class EscribirContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def printStatement(self):
            return self.getTypedRuleContext(SimpleLangParser.PrintStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscribir" ):
                listener.enterEscribir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscribir" ):
                listener.exitEscribir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscribir" ):
                return visitor.visitEscribir(self)
            else:
                return visitor.visitChildren(self)


    class RaizCuaContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def raizCuadrada(self):
            return self.getTypedRuleContext(SimpleLangParser.RaizCuadradaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaizCua" ):
                listener.enterRaizCua(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaizCua" ):
                listener.exitRaizCua(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaizCua" ):
                return visitor.visitRaizCua(self)
            else:
                return visitor.visitChildren(self)


    class CondicionalContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifStatement(self):
            return self.getTypedRuleContext(SimpleLangParser.IfStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)


    class DeclaracionFuncionContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionDeclaration(self):
            return self.getTypedRuleContext(SimpleLangParser.FunctionDeclarationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionFuncion" ):
                listener.enterDeclaracionFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionFuncion" ):
                listener.exitDeclaracionFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionFuncion" ):
                return visitor.visitDeclaracionFuncion(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = SimpleLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15]:
                localctx = SimpleLangParser.DeclaracionVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.varDeclaration()
                pass
            elif token in [5]:
                localctx = SimpleLangParser.DeclaracionFuncionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.functionDeclaration()
                pass
            elif token in [10]:
                localctx = SimpleLangParser.CondicionalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.ifStatement()
                pass
            elif token in [12]:
                localctx = SimpleLangParser.CicloContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.loopStatement()
                pass
            elif token in [31]:
                localctx = SimpleLangParser.EscribirContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 39
                self.printStatement()
                pass
            elif token in [16]:
                localctx = SimpleLangParser.AumentarEnUnoContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 40
                self.aumentar()
                pass
            elif token in [17]:
                localctx = SimpleLangParser.DisminuirEnUnoContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 41
                self.disminuir()
                pass
            elif token in [18]:
                localctx = SimpleLangParser.PotenciasContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 42
                self.potencia()
                pass
            elif token in [19]:
                localctx = SimpleLangParser.RaizCuaContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 43
                self.raizCuadrada()
                pass
            elif token in [6, 32, 33, 34, 35]:
                localctx = SimpleLangParser.ExpresionContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(SimpleLangParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(SimpleLangParser.TipoContext,0)


        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_varDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclaration" ):
                listener.enterVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclaration" ):
                listener.exitVarDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclaration" ):
                return visitor.visitVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def varDeclaration(self):

        localctx = SimpleLangParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.tipo()
            self.state = 50
            self.match(SimpleLangParser.ID)
            self.state = 51
            self.match(SimpleLangParser.T__3)
            self.state = 52
            self.expr(0)
            self.state = 53
            self.match(SimpleLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = SimpleLangParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(SimpleLangParser.T__4)
            self.state = 56
            self.match(SimpleLangParser.ID)
            self.state = 57
            self.match(SimpleLangParser.T__5)
            self.state = 58
            self.match(SimpleLangParser.T__6)
            self.state = 59
            self.match(SimpleLangParser.T__7)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 66573038688) != 0):
                self.state = 60
                self.statement()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(SimpleLangParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = SimpleLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(SimpleLangParser.T__9)
            self.state = 69
            self.match(SimpleLangParser.T__5)
            self.state = 70
            self.expr(0)
            self.state = 71
            self.match(SimpleLangParser.T__6)
            self.state = 72
            self.match(SimpleLangParser.T__7)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 66573038688) != 0):
                self.state = 73
                self.statement()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self.match(SimpleLangParser.T__8)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 80
                self.match(SimpleLangParser.T__10)
                self.state = 81
                self.match(SimpleLangParser.T__7)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 66573038688) != 0):
                    self.state = 82
                    self.statement()
                    self.state = 87
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 88
                self.match(SimpleLangParser.T__8)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = SimpleLangParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_loopStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(SimpleLangParser.T__11)
            self.state = 92
            self.match(SimpleLangParser.T__5)
            self.state = 93
            self.expr(0)
            self.state = 94
            self.match(SimpleLangParser.T__6)
            self.state = 95
            self.match(SimpleLangParser.T__7)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 66573038688) != 0):
                self.state = 96
                self.statement()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
            self.match(SimpleLangParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = SimpleLangParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AumentarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_aumentar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAumentar" ):
                listener.enterAumentar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAumentar" ):
                listener.exitAumentar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAumentar" ):
                return visitor.visitAumentar(self)
            else:
                return visitor.visitChildren(self)




    def aumentar(self):

        localctx = SimpleLangParser.AumentarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_aumentar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(SimpleLangParser.T__15)
            self.state = 107
            self.match(SimpleLangParser.T__5)
            self.state = 108
            self.match(SimpleLangParser.ID)
            self.state = 109
            self.match(SimpleLangParser.T__6)
            self.state = 110
            self.match(SimpleLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisminuirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_disminuir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisminuir" ):
                listener.enterDisminuir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisminuir" ):
                listener.exitDisminuir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisminuir" ):
                return visitor.visitDisminuir(self)
            else:
                return visitor.visitChildren(self)




    def disminuir(self):

        localctx = SimpleLangParser.DisminuirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_disminuir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(SimpleLangParser.T__16)
            self.state = 113
            self.match(SimpleLangParser.T__5)
            self.state = 114
            self.match(SimpleLangParser.ID)
            self.state = 115
            self.match(SimpleLangParser.T__6)
            self.state = 116
            self.match(SimpleLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PotenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_potencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPotencia" ):
                listener.enterPotencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPotencia" ):
                listener.exitPotencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPotencia" ):
                return visitor.visitPotencia(self)
            else:
                return visitor.visitChildren(self)




    def potencia(self):

        localctx = SimpleLangParser.PotenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_potencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(SimpleLangParser.T__17)
            self.state = 119
            self.match(SimpleLangParser.T__5)
            self.state = 120
            self.match(SimpleLangParser.ID)
            self.state = 121
            self.match(SimpleLangParser.T__6)
            self.state = 122
            self.match(SimpleLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RaizCuadradaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_raizCuadrada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaizCuadrada" ):
                listener.enterRaizCuadrada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaizCuadrada" ):
                listener.exitRaizCuadrada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaizCuadrada" ):
                return visitor.visitRaizCuadrada(self)
            else:
                return visitor.visitChildren(self)




    def raizCuadrada(self):

        localctx = SimpleLangParser.RaizCuadradaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_raizCuadrada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(SimpleLangParser.T__18)
            self.state = 125
            self.match(SimpleLangParser.T__5)
            self.state = 126
            self.match(SimpleLangParser.ID)
            self.state = 127
            self.match(SimpleLangParser.T__6)
            self.state = 128
            self.match(SimpleLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class MenorIgualQueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenorIgualQue" ):
                listener.enterMenorIgualQue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenorIgualQue" ):
                listener.exitMenorIgualQue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMenorIgualQue" ):
                return visitor.visitMenorIgualQue(self)
            else:
                return visitor.visitChildren(self)


    class ParentesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(SimpleLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicacionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicacion" ):
                listener.enterMultiplicacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicacion" ):
                listener.exitMultiplicacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicacion" ):
                return visitor.visitMultiplicacion(self)
            else:
                return visitor.visitChildren(self)


    class MayorIgualQueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMayorIgualQue" ):
                listener.enterMayorIgualQue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMayorIgualQue" ):
                listener.exitMayorIgualQue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMayorIgualQue" ):
                return visitor.visitMayorIgualQue(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SimpleLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class SumaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class DiferenteDeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiferenteDe" ):
                listener.enterDiferenteDe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiferenteDe" ):
                listener.exitDiferenteDe(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiferenteDe" ):
                return visitor.visitDiferenteDe(self)
            else:
                return visitor.visitChildren(self)


    class IgualQueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgualQue" ):
                listener.enterIgualQue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgualQue" ):
                listener.exitIgualQue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgualQue" ):
                return visitor.visitIgualQue(self)
            else:
                return visitor.visitChildren(self)


    class DivisionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivision" ):
                listener.enterDivision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivision" ):
                listener.exitDivision(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivision" ):
                return visitor.visitDivision(self)
            else:
                return visitor.visitChildren(self)


    class IDContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterID" ):
                listener.enterID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitID" ):
                listener.exitID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitID" ):
                return visitor.visitID(self)
            else:
                return visitor.visitChildren(self)


    class MayorQueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMayorQue" ):
                listener.enterMayorQue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMayorQue" ):
                listener.exitMayorQue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMayorQue" ):
                return visitor.visitMayorQue(self)
            else:
                return visitor.visitChildren(self)


    class BooleanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(SimpleLangParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)


    class MenorQueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenorQue" ):
                listener.enterMenorQue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenorQue" ):
                listener.exitMenorQue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMenorQue" ):
                return visitor.visitMenorQue(self)
            else:
                return visitor.visitChildren(self)


    class RestaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResta" ):
                listener.enterResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResta" ):
                listener.exitResta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResta" ):
                return visitor.visitResta(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = SimpleLangParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 131
                self.match(SimpleLangParser.T__5)
                self.state = 132
                self.expr(0)
                self.state = 133
                self.match(SimpleLangParser.T__6)
                pass
            elif token in [32]:
                localctx = SimpleLangParser.IDContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 135
                self.match(SimpleLangParser.ID)
                pass
            elif token in [33]:
                localctx = SimpleLangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 136
                self.match(SimpleLangParser.INT)
                pass
            elif token in [34]:
                localctx = SimpleLangParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 137
                self.match(SimpleLangParser.STRING)
                pass
            elif token in [35]:
                localctx = SimpleLangParser.BooleanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 138
                self.match(SimpleLangParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 177
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.AndContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 141
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 142
                        self.match(SimpleLangParser.T__19)
                        self.state = 143
                        self.expr(18)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.OrContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 144
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 145
                        self.match(SimpleLangParser.T__20)
                        self.state = 146
                        self.expr(17)
                        pass

                    elif la_ == 3:
                        localctx = SimpleLangParser.MenorQueContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 147
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 148
                        self.match(SimpleLangParser.T__21)
                        self.state = 149
                        self.expr(16)
                        pass

                    elif la_ == 4:
                        localctx = SimpleLangParser.MayorQueContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 150
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 151
                        self.match(SimpleLangParser.T__22)
                        self.state = 152
                        self.expr(15)
                        pass

                    elif la_ == 5:
                        localctx = SimpleLangParser.IgualQueContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 153
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 154
                        self.match(SimpleLangParser.T__23)
                        self.state = 155
                        self.expr(14)
                        pass

                    elif la_ == 6:
                        localctx = SimpleLangParser.MenorIgualQueContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 156
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 157
                        self.match(SimpleLangParser.T__24)
                        self.state = 158
                        self.expr(13)
                        pass

                    elif la_ == 7:
                        localctx = SimpleLangParser.MayorIgualQueContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 159
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 160
                        self.match(SimpleLangParser.T__24)
                        self.state = 161
                        self.expr(12)
                        pass

                    elif la_ == 8:
                        localctx = SimpleLangParser.DiferenteDeContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 162
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 163
                        self.match(SimpleLangParser.T__25)
                        self.state = 164
                        self.expr(11)
                        pass

                    elif la_ == 9:
                        localctx = SimpleLangParser.SumaContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 165
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 166
                        self.match(SimpleLangParser.T__26)
                        self.state = 167
                        self.expr(9)
                        pass

                    elif la_ == 10:
                        localctx = SimpleLangParser.RestaContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 168
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 169
                        self.match(SimpleLangParser.T__27)
                        self.state = 170
                        self.expr(8)
                        pass

                    elif la_ == 11:
                        localctx = SimpleLangParser.MultiplicacionContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 171
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 172
                        self.match(SimpleLangParser.T__28)
                        self.state = 173
                        self.expr(7)
                        pass

                    elif la_ == 12:
                        localctx = SimpleLangParser.DivisionContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 174
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 175
                        self.match(SimpleLangParser.T__29)
                        self.state = 176
                        self.expr(6)
                        pass

             
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = SimpleLangParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(SimpleLangParser.T__30)
            self.state = 183
            self.match(SimpleLangParser.T__5)
            self.state = 184
            self.expr(0)
            self.state = 185
            self.match(SimpleLangParser.T__6)
            self.state = 186
            self.match(SimpleLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 5)
         




