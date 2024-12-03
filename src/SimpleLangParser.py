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
        4,1,31,126,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,5,0,21,8,0,10,0,12,0,24,9,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,3,1,3,5,3,50,8,3,10,3,12,3,53,9,3,1,3,1,3,1,4,
        1,4,1,4,1,4,1,4,1,4,5,4,63,8,4,10,4,12,4,66,9,4,1,4,1,4,1,4,1,4,
        5,4,72,8,4,10,4,12,4,75,9,4,1,4,3,4,78,8,4,1,5,1,5,1,5,1,5,1,5,1,
        5,5,5,86,8,5,10,5,12,5,89,9,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,3,7,104,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,5,7,115,8,7,10,7,12,7,118,9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,0,1,
        14,9,0,2,4,6,8,10,12,14,16,0,4,1,0,13,15,1,0,16,17,1,0,18,19,1,0,
        20,25,134,0,18,1,0,0,0,2,35,1,0,0,0,4,37,1,0,0,0,6,43,1,0,0,0,8,
        56,1,0,0,0,10,79,1,0,0,0,12,92,1,0,0,0,14,103,1,0,0,0,16,119,1,0,
        0,0,18,22,5,1,0,0,19,21,3,2,1,0,20,19,1,0,0,0,21,24,1,0,0,0,22,20,
        1,0,0,0,22,23,1,0,0,0,23,25,1,0,0,0,24,22,1,0,0,0,25,26,5,2,0,0,
        26,1,1,0,0,0,27,36,3,4,2,0,28,36,3,6,3,0,29,36,3,8,4,0,30,36,3,10,
        5,0,31,36,3,16,8,0,32,33,3,14,7,0,33,34,5,3,0,0,34,36,1,0,0,0,35,
        27,1,0,0,0,35,28,1,0,0,0,35,29,1,0,0,0,35,30,1,0,0,0,35,31,1,0,0,
        0,35,32,1,0,0,0,36,3,1,0,0,0,37,38,3,12,6,0,38,39,5,27,0,0,39,40,
        5,4,0,0,40,41,3,14,7,0,41,42,5,3,0,0,42,5,1,0,0,0,43,44,5,5,0,0,
        44,45,5,27,0,0,45,46,5,6,0,0,46,47,5,7,0,0,47,51,5,8,0,0,48,50,3,
        2,1,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,
        54,1,0,0,0,53,51,1,0,0,0,54,55,5,9,0,0,55,7,1,0,0,0,56,57,5,10,0,
        0,57,58,5,6,0,0,58,59,3,14,7,0,59,60,5,7,0,0,60,64,5,8,0,0,61,63,
        3,2,1,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,
        65,67,1,0,0,0,66,64,1,0,0,0,67,77,5,9,0,0,68,69,5,11,0,0,69,73,5,
        8,0,0,70,72,3,2,1,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,
        74,1,0,0,0,74,76,1,0,0,0,75,73,1,0,0,0,76,78,5,9,0,0,77,68,1,0,0,
        0,77,78,1,0,0,0,78,9,1,0,0,0,79,80,5,12,0,0,80,81,5,6,0,0,81,82,
        3,14,7,0,82,83,5,7,0,0,83,87,5,8,0,0,84,86,3,2,1,0,85,84,1,0,0,0,
        86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,90,1,0,0,0,89,87,1,
        0,0,0,90,91,5,9,0,0,91,11,1,0,0,0,92,93,7,0,0,0,93,13,1,0,0,0,94,
        95,6,7,-1,0,95,96,5,6,0,0,96,97,3,14,7,0,97,98,5,7,0,0,98,104,1,
        0,0,0,99,104,5,27,0,0,100,104,5,28,0,0,101,104,5,29,0,0,102,104,
        5,30,0,0,103,94,1,0,0,0,103,99,1,0,0,0,103,100,1,0,0,0,103,101,1,
        0,0,0,103,102,1,0,0,0,104,116,1,0,0,0,105,106,10,8,0,0,106,107,7,
        1,0,0,107,115,3,14,7,9,108,109,10,7,0,0,109,110,7,2,0,0,110,115,
        3,14,7,8,111,112,10,6,0,0,112,113,7,3,0,0,113,115,3,14,7,7,114,105,
        1,0,0,0,114,108,1,0,0,0,114,111,1,0,0,0,115,118,1,0,0,0,116,114,
        1,0,0,0,116,117,1,0,0,0,117,15,1,0,0,0,118,116,1,0,0,0,119,120,5,
        26,0,0,120,121,5,6,0,0,121,122,3,14,7,0,122,123,5,7,0,0,123,124,
        5,3,0,0,124,17,1,0,0,0,10,22,35,51,64,73,77,87,103,114,116
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Empecemos!'", "'Hasta luego!'", "';'", 
                     "'='", "'hacer esto'", "'('", "')'", "'{'", "'}'", 
                     "'Si pasa esto'", "'Sino'", "'Repetir hasta que'", 
                     "'numero'", "'texto'", "'logico'", "'*'", "'/'", "'+'", 
                     "'-'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
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
    RULE_expr = 7
    RULE_printStatement = 8

    ruleNames =  [ "program", "statement", "varDeclaration", "functionDeclaration", 
                   "ifStatement", "loopStatement", "tipo", "expr", "printStatement" ]

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
            self.state = 18
            self.match(SimpleLangParser.T__0)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2080437344) != 0):
                self.state = 19
                self.statement()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 25
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
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15]:
                localctx = SimpleLangParser.DeclaracionVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.varDeclaration()
                pass
            elif token in [5]:
                localctx = SimpleLangParser.DeclaracionFuncionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.functionDeclaration()
                pass
            elif token in [10]:
                localctx = SimpleLangParser.CondicionalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.ifStatement()
                pass
            elif token in [12]:
                localctx = SimpleLangParser.CicloContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.loopStatement()
                pass
            elif token in [26]:
                localctx = SimpleLangParser.EscribirContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.printStatement()
                pass
            elif token in [6, 27, 28, 29, 30]:
                localctx = SimpleLangParser.ExpresionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 32
                self.expr(0)
                self.state = 33
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
            self.state = 37
            self.tipo()
            self.state = 38
            self.match(SimpleLangParser.ID)
            self.state = 39
            self.match(SimpleLangParser.T__3)
            self.state = 40
            self.expr(0)
            self.state = 41
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
            self.state = 43
            self.match(SimpleLangParser.T__4)
            self.state = 44
            self.match(SimpleLangParser.ID)
            self.state = 45
            self.match(SimpleLangParser.T__5)
            self.state = 46
            self.match(SimpleLangParser.T__6)
            self.state = 47
            self.match(SimpleLangParser.T__7)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2080437344) != 0):
                self.state = 48
                self.statement()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
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
            self.state = 56
            self.match(SimpleLangParser.T__9)
            self.state = 57
            self.match(SimpleLangParser.T__5)
            self.state = 58
            self.expr(0)
            self.state = 59
            self.match(SimpleLangParser.T__6)
            self.state = 60
            self.match(SimpleLangParser.T__7)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2080437344) != 0):
                self.state = 61
                self.statement()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(SimpleLangParser.T__8)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 68
                self.match(SimpleLangParser.T__10)
                self.state = 69
                self.match(SimpleLangParser.T__7)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2080437344) != 0):
                    self.state = 70
                    self.statement()
                    self.state = 75
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 76
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
            self.state = 79
            self.match(SimpleLangParser.T__11)
            self.state = 80
            self.match(SimpleLangParser.T__5)
            self.state = 81
            self.expr(0)
            self.state = 82
            self.match(SimpleLangParser.T__6)
            self.state = 83
            self.match(SimpleLangParser.T__7)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2080437344) != 0):
                self.state = 84
                self.statement()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
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
            self.state = 92
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ComparacionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion" ):
                listener.enterComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion" ):
                listener.exitComparacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacion" ):
                return visitor.visitComparacion(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
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


    class SumaRestaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumaResta" ):
                listener.enterSumaResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumaResta" ):
                listener.exitSumaResta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaResta" ):
                return visitor.visitSumaResta(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = SimpleLangParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 95
                self.match(SimpleLangParser.T__5)
                self.state = 96
                self.expr(0)
                self.state = 97
                self.match(SimpleLangParser.T__6)
                pass
            elif token in [27]:
                localctx = SimpleLangParser.IDContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 99
                self.match(SimpleLangParser.ID)
                pass
            elif token in [28]:
                localctx = SimpleLangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 100
                self.match(SimpleLangParser.INT)
                pass
            elif token in [29]:
                localctx = SimpleLangParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 101
                self.match(SimpleLangParser.STRING)
                pass
            elif token in [30]:
                localctx = SimpleLangParser.BooleanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 102
                self.match(SimpleLangParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 114
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.MulDivContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 105
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 106
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 107
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.SumaRestaContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 108
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 109
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 110
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = SimpleLangParser.ComparacionContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 111
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 112
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 113
                        self.expr(7)
                        pass

             
                self.state = 118
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
        self.enterRule(localctx, 16, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(SimpleLangParser.T__25)
            self.state = 120
            self.match(SimpleLangParser.T__5)
            self.state = 121
            self.expr(0)
            self.state = 122
            self.match(SimpleLangParser.T__6)
            self.state = 123
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
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         




