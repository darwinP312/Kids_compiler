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
        4,1,31,155,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,5,0,25,8,0,10,0,12,0,
        28,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,40,8,1,1,2,1,
        2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,54,8,3,10,3,12,3,57,
        9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,67,8,4,10,4,12,4,70,9,4,
        1,4,1,4,1,4,1,4,5,4,76,8,4,10,4,12,4,79,9,4,1,4,3,4,82,8,4,1,5,1,
        5,1,5,1,5,1,5,1,5,5,5,90,8,5,10,5,12,5,93,9,5,1,5,1,5,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,3,9,118,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,144,8,
        9,10,9,12,9,147,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,0,1,18,11,
        0,2,4,6,8,10,12,14,16,18,20,0,1,1,0,13,15,166,0,22,1,0,0,0,2,39,
        1,0,0,0,4,41,1,0,0,0,6,47,1,0,0,0,8,60,1,0,0,0,10,83,1,0,0,0,12,
        96,1,0,0,0,14,98,1,0,0,0,16,103,1,0,0,0,18,117,1,0,0,0,20,148,1,
        0,0,0,22,26,5,1,0,0,23,25,3,2,1,0,24,23,1,0,0,0,25,28,1,0,0,0,26,
        24,1,0,0,0,26,27,1,0,0,0,27,29,1,0,0,0,28,26,1,0,0,0,29,30,5,2,0,
        0,30,1,1,0,0,0,31,40,3,4,2,0,32,40,3,6,3,0,33,40,3,8,4,0,34,40,3,
        10,5,0,35,40,3,20,10,0,36,37,3,18,9,0,37,38,5,3,0,0,38,40,1,0,0,
        0,39,31,1,0,0,0,39,32,1,0,0,0,39,33,1,0,0,0,39,34,1,0,0,0,39,35,
        1,0,0,0,39,36,1,0,0,0,40,3,1,0,0,0,41,42,3,12,6,0,42,43,5,27,0,0,
        43,44,5,4,0,0,44,45,3,18,9,0,45,46,5,3,0,0,46,5,1,0,0,0,47,48,5,
        5,0,0,48,49,5,27,0,0,49,50,5,6,0,0,50,51,5,7,0,0,51,55,5,8,0,0,52,
        54,3,2,1,0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,
        0,56,58,1,0,0,0,57,55,1,0,0,0,58,59,5,9,0,0,59,7,1,0,0,0,60,61,5,
        10,0,0,61,62,5,6,0,0,62,63,3,18,9,0,63,64,5,7,0,0,64,68,5,8,0,0,
        65,67,3,2,1,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,
        0,0,0,69,71,1,0,0,0,70,68,1,0,0,0,71,81,5,9,0,0,72,73,5,11,0,0,73,
        77,5,8,0,0,74,76,3,2,1,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,
        0,77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,82,5,9,0,0,81,72,
        1,0,0,0,81,82,1,0,0,0,82,9,1,0,0,0,83,84,5,12,0,0,84,85,5,6,0,0,
        85,86,3,18,9,0,86,87,5,7,0,0,87,91,5,8,0,0,88,90,3,2,1,0,89,88,1,
        0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,
        91,1,0,0,0,94,95,5,9,0,0,95,11,1,0,0,0,96,97,7,0,0,0,97,13,1,0,0,
        0,98,99,5,16,0,0,99,100,5,6,0,0,100,101,5,27,0,0,101,102,5,7,0,0,
        102,15,1,0,0,0,103,104,5,17,0,0,104,105,5,6,0,0,105,106,5,27,0,0,
        106,107,5,7,0,0,107,17,1,0,0,0,108,109,6,9,-1,0,109,110,5,6,0,0,
        110,111,3,18,9,0,111,112,5,7,0,0,112,118,1,0,0,0,113,118,5,27,0,
        0,114,118,5,28,0,0,115,118,5,29,0,0,116,118,5,30,0,0,117,108,1,0,
        0,0,117,113,1,0,0,0,117,114,1,0,0,0,117,115,1,0,0,0,117,116,1,0,
        0,0,118,145,1,0,0,0,119,120,10,13,0,0,120,121,5,18,0,0,121,144,3,
        18,9,14,122,123,10,12,0,0,123,124,5,19,0,0,124,144,3,18,9,13,125,
        126,10,11,0,0,126,127,5,20,0,0,127,144,3,18,9,12,128,129,10,10,0,
        0,129,130,5,21,0,0,130,144,3,18,9,11,131,132,10,9,0,0,132,133,5,
        22,0,0,133,144,3,18,9,10,134,135,10,8,0,0,135,136,5,23,0,0,136,144,
        3,18,9,9,137,138,10,7,0,0,138,139,5,24,0,0,139,144,3,18,9,8,140,
        141,10,6,0,0,141,142,5,25,0,0,142,144,3,18,9,7,143,119,1,0,0,0,143,
        122,1,0,0,0,143,125,1,0,0,0,143,128,1,0,0,0,143,131,1,0,0,0,143,
        134,1,0,0,0,143,137,1,0,0,0,143,140,1,0,0,0,144,147,1,0,0,0,145,
        143,1,0,0,0,145,146,1,0,0,0,146,19,1,0,0,0,147,145,1,0,0,0,148,149,
        5,26,0,0,149,150,5,6,0,0,150,151,3,18,9,0,151,152,5,7,0,0,152,153,
        5,3,0,0,153,21,1,0,0,0,10,26,39,55,68,77,81,91,117,143,145
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Empecemos!'", "'Hasta luego!'", "';'", 
                     "'='", "'hacer esto'", "'('", "')'", "'{'", "'}'", 
                     "'Si pasa esto'", "'Sino'", "'Repetir hasta que'", 
                     "'numero'", "'texto'", "'logico'", "'aumentar'", "'disminuir'", 
                     "'y'", "'o'", "'menor que'", "'mayor que'", "'igual que'", 
                     "'menor o igual que'", "'mayor o igual que'", "'diferente de'", 
                     "'escribir'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "STRING", "BOOL", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_varDeclaration = 2
    RULE_functionDeclaration = 3
    RULE_ifStatement = 4
    RULE_loopStatement = 5
    RULE_tipo = 6
    RULE_aumentar = 7
    RULE_disminuir = 8
    RULE_expr = 9
    RULE_printStatement = 10

    ruleNames =  [ "program", "statement", "varDeclaration", "functionDeclaration", 
                   "ifStatement", "loopStatement", "tipo", "aumentar", "disminuir", 
                   "expr", "printStatement" ]

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
    ID=27
    INT=28
    STRING=29
    BOOL=30
    WS=31

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
            self.state = 22
            self.match(SimpleLangParser.T__0)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2080437344) != 0):
                self.state = 23
                self.statement()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
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
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15]:
                localctx = SimpleLangParser.DeclaracionVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.varDeclaration()
                pass
            elif token in [5]:
                localctx = SimpleLangParser.DeclaracionFuncionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.functionDeclaration()
                pass
            elif token in [10]:
                localctx = SimpleLangParser.CondicionalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.ifStatement()
                pass
            elif token in [12]:
                localctx = SimpleLangParser.CicloContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.loopStatement()
                pass
            elif token in [26]:
                localctx = SimpleLangParser.EscribirContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 35
                self.printStatement()
                pass
            elif token in [6, 27, 28, 29, 30]:
                localctx = SimpleLangParser.ExpresionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 36
                self.expr(0)
                self.state = 37
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
            self.state = 41
            self.tipo()
            self.state = 42
            self.match(SimpleLangParser.ID)
            self.state = 43
            self.match(SimpleLangParser.T__3)
            self.state = 44
            self.expr(0)
            self.state = 45
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
            self.state = 47
            self.match(SimpleLangParser.T__4)
            self.state = 48
            self.match(SimpleLangParser.ID)
            self.state = 49
            self.match(SimpleLangParser.T__5)
            self.state = 50
            self.match(SimpleLangParser.T__6)
            self.state = 51
            self.match(SimpleLangParser.T__7)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2080437344) != 0):
                self.state = 52
                self.statement()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
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
            self.state = 60
            self.match(SimpleLangParser.T__9)
            self.state = 61
            self.match(SimpleLangParser.T__5)
            self.state = 62
            self.expr(0)
            self.state = 63
            self.match(SimpleLangParser.T__6)
            self.state = 64
            self.match(SimpleLangParser.T__7)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2080437344) != 0):
                self.state = 65
                self.statement()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(SimpleLangParser.T__8)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 72
                self.match(SimpleLangParser.T__10)
                self.state = 73
                self.match(SimpleLangParser.T__7)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2080437344) != 0):
                    self.state = 74
                    self.statement()
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 80
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
            self.state = 83
            self.match(SimpleLangParser.T__11)
            self.state = 84
            self.match(SimpleLangParser.T__5)
            self.state = 85
            self.expr(0)
            self.state = 86
            self.match(SimpleLangParser.T__6)
            self.state = 87
            self.match(SimpleLangParser.T__7)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2080437344) != 0):
                self.state = 88
                self.statement()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
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
            self.state = 96
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
            self.state = 98
            self.match(SimpleLangParser.T__15)
            self.state = 99
            self.match(SimpleLangParser.T__5)
            self.state = 100
            self.match(SimpleLangParser.ID)
            self.state = 101
            self.match(SimpleLangParser.T__6)
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
            self.state = 103
            self.match(SimpleLangParser.T__16)
            self.state = 104
            self.match(SimpleLangParser.T__5)
            self.state = 105
            self.match(SimpleLangParser.ID)
            self.state = 106
            self.match(SimpleLangParser.T__6)
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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = SimpleLangParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 109
                self.match(SimpleLangParser.T__5)
                self.state = 110
                self.expr(0)
                self.state = 111
                self.match(SimpleLangParser.T__6)
                pass
            elif token in [27]:
                localctx = SimpleLangParser.IDContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 113
                self.match(SimpleLangParser.ID)
                pass
            elif token in [28]:
                localctx = SimpleLangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 114
                self.match(SimpleLangParser.INT)
                pass
            elif token in [29]:
                localctx = SimpleLangParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.match(SimpleLangParser.STRING)
                pass
            elif token in [30]:
                localctx = SimpleLangParser.BooleanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 116
                self.match(SimpleLangParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 143
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.AndContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 119
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 120
                        self.match(SimpleLangParser.T__17)
                        self.state = 121
                        self.expr(14)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.OrContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 122
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 123
                        self.match(SimpleLangParser.T__18)
                        self.state = 124
                        self.expr(13)
                        pass

                    elif la_ == 3:
                        localctx = SimpleLangParser.MenorQueContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 125
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 126
                        self.match(SimpleLangParser.T__19)
                        self.state = 127
                        self.expr(12)
                        pass

                    elif la_ == 4:
                        localctx = SimpleLangParser.MayorQueContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 128
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 129
                        self.match(SimpleLangParser.T__20)
                        self.state = 130
                        self.expr(11)
                        pass

                    elif la_ == 5:
                        localctx = SimpleLangParser.IgualQueContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 131
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 132
                        self.match(SimpleLangParser.T__21)
                        self.state = 133
                        self.expr(10)
                        pass

                    elif la_ == 6:
                        localctx = SimpleLangParser.MenorIgualQueContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 134
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 135
                        self.match(SimpleLangParser.T__22)
                        self.state = 136
                        self.expr(9)
                        pass

                    elif la_ == 7:
                        localctx = SimpleLangParser.MayorIgualQueContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 137
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 138
                        self.match(SimpleLangParser.T__23)
                        self.state = 139
                        self.expr(8)
                        pass

                    elif la_ == 8:
                        localctx = SimpleLangParser.DiferenteDeContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 140
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 141
                        self.match(SimpleLangParser.T__24)
                        self.state = 142
                        self.expr(7)
                        pass

             
                self.state = 147
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
        self.enterRule(localctx, 20, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(SimpleLangParser.T__25)
            self.state = 149
            self.match(SimpleLangParser.T__5)
            self.state = 150
            self.expr(0)
            self.state = 151
            self.match(SimpleLangParser.T__6)
            self.state = 152
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
        self._predicates[9] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 6)
         




