// Generated from c:/Users/DARWI/Documents/GitHub/Kids_compiler/grammar/SimpleLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class SimpleLangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, LINE_COMMENT=33, ID=34, INT=35, STRING=36, BOOL=37, WS=38;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_varDeclaration = 2, RULE_functionDeclaration = 3, 
		RULE_ifStatement = 4, RULE_loopStatement = 5, RULE_tipo = 6, RULE_aumentar = 7, 
		RULE_disminuir = 8, RULE_potencia = 9, RULE_raizCuadrada = 10, RULE_expr = 11, 
		RULE_printStatement = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "varDeclaration", "functionDeclaration", "ifStatement", 
			"loopStatement", "tipo", "aumentar", "disminuir", "potencia", "raizCuadrada", 
			"expr", "printStatement"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Empecemos!'", "'Hasta luego!'", "';'", "'='", "'hacer esto'", 
			"'('", "')'", "'{'", "'}'", "'Si pasa esto'", "'Sino'", "'Repetir mientras que'", 
			"'numero'", "'texto'", "'logico'", "'aumentar'", "'disminuir'", "'potencia'", 
			"'raizCuadrada'", "'y que'", "'o que'", "'menor que'", "'mayor que'", 
			"'igual que'", "'menor igual a'", "'diferente de'", "'*'", "'/'", "'+'", 
			"'-'", "','", "'escribir'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, "LINE_COMMENT", 
			"ID", "INT", "STRING", "BOOL", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "SimpleLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SimpleLangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			match(T__0);
			setState(30);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 261994050656L) != 0)) {
				{
				{
				setState(27);
				statement();
				}
				}
				setState(32);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(33);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionVariableContext extends StatementContext {
		public VarDeclarationContext varDeclaration() {
			return getRuleContext(VarDeclarationContext.class,0);
		}
		public DeclaracionVariableContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CicloContext extends StatementContext {
		public LoopStatementContext loopStatement() {
			return getRuleContext(LoopStatementContext.class,0);
		}
		public CicloContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionContext extends StatementContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExpresionContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DisminuirEnUnoContext extends StatementContext {
		public DisminuirContext disminuir() {
			return getRuleContext(DisminuirContext.class,0);
		}
		public DisminuirEnUnoContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PotenciasContext extends StatementContext {
		public PotenciaContext potencia() {
			return getRuleContext(PotenciaContext.class,0);
		}
		public PotenciasContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AumentarEnUnoContext extends StatementContext {
		public AumentarContext aumentar() {
			return getRuleContext(AumentarContext.class,0);
		}
		public AumentarEnUnoContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class EscribirContext extends StatementContext {
		public PrintStatementContext printStatement() {
			return getRuleContext(PrintStatementContext.class,0);
		}
		public EscribirContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RaizCuaContext extends StatementContext {
		public RaizCuadradaContext raizCuadrada() {
			return getRuleContext(RaizCuadradaContext.class,0);
		}
		public RaizCuaContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CondicionalContext extends StatementContext {
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public CondicionalContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionFuncionContext extends StatementContext {
		public FunctionDeclarationContext functionDeclaration() {
			return getRuleContext(FunctionDeclarationContext.class,0);
		}
		public DeclaracionFuncionContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(47);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				_localctx = new DeclaracionVariableContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(35);
				varDeclaration();
				}
				break;
			case 2:
				_localctx = new DeclaracionFuncionContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(36);
				functionDeclaration();
				}
				break;
			case 3:
				_localctx = new CondicionalContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(37);
				ifStatement();
				}
				break;
			case 4:
				_localctx = new CicloContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(38);
				loopStatement();
				}
				break;
			case 5:
				_localctx = new EscribirContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(39);
				printStatement();
				}
				break;
			case 6:
				_localctx = new AumentarEnUnoContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(40);
				aumentar();
				}
				break;
			case 7:
				_localctx = new DisminuirEnUnoContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(41);
				disminuir();
				}
				break;
			case 8:
				_localctx = new PotenciasContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(42);
				potencia();
				}
				break;
			case 9:
				_localctx = new RaizCuaContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(43);
				raizCuadrada();
				}
				break;
			case 10:
				_localctx = new ExpresionContext(_localctx);
				enterOuterAlt(_localctx, 10);
				{
				setState(44);
				expr(0);
				setState(45);
				match(T__2);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDeclarationContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(SimpleLangParser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public VarDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDeclaration; }
	}

	public final VarDeclarationContext varDeclaration() throws RecognitionException {
		VarDeclarationContext _localctx = new VarDeclarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_varDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			tipo();
			setState(50);
			match(ID);
			setState(51);
			match(T__3);
			setState(52);
			expr(0);
			setState(53);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionDeclarationContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SimpleLangParser.ID, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public FunctionDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDeclaration; }
	}

	public final FunctionDeclarationContext functionDeclaration() throws RecognitionException {
		FunctionDeclarationContext _localctx = new FunctionDeclarationContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_functionDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			match(T__4);
			setState(56);
			match(ID);
			setState(57);
			match(T__5);
			setState(58);
			match(T__6);
			setState(59);
			match(T__7);
			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 261994050656L) != 0)) {
				{
				{
				setState(60);
				statement();
				}
				}
				setState(65);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(66);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStatementContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_ifStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(T__9);
			setState(69);
			match(T__5);
			setState(70);
			expr(0);
			setState(71);
			match(T__6);
			setState(72);
			match(T__7);
			setState(76);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 261994050656L) != 0)) {
				{
				{
				setState(73);
				statement();
				}
				}
				setState(78);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(79);
			match(T__8);
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__10) {
				{
				setState(80);
				match(T__10);
				setState(81);
				match(T__7);
				setState(85);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 261994050656L) != 0)) {
					{
					{
					setState(82);
					statement();
					}
					}
					setState(87);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(88);
				match(T__8);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LoopStatementContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public LoopStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loopStatement; }
	}

	public final LoopStatementContext loopStatement() throws RecognitionException {
		LoopStatementContext _localctx = new LoopStatementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_loopStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(T__11);
			setState(92);
			match(T__5);
			setState(93);
			expr(0);
			setState(94);
			match(T__6);
			setState(95);
			match(T__7);
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 261994050656L) != 0)) {
				{
				{
				setState(96);
				statement();
				}
				}
				setState(101);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(102);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoContext extends ParserRuleContext {
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 57344L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AumentarContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SimpleLangParser.ID, 0); }
		public AumentarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_aumentar; }
	}

	public final AumentarContext aumentar() throws RecognitionException {
		AumentarContext _localctx = new AumentarContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_aumentar);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(T__15);
			setState(107);
			match(T__5);
			setState(108);
			match(ID);
			setState(109);
			match(T__6);
			setState(110);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DisminuirContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SimpleLangParser.ID, 0); }
		public DisminuirContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_disminuir; }
	}

	public final DisminuirContext disminuir() throws RecognitionException {
		DisminuirContext _localctx = new DisminuirContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_disminuir);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			match(T__16);
			setState(113);
			match(T__5);
			setState(114);
			match(ID);
			setState(115);
			match(T__6);
			setState(116);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PotenciaContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SimpleLangParser.ID, 0); }
		public PotenciaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_potencia; }
	}

	public final PotenciaContext potencia() throws RecognitionException {
		PotenciaContext _localctx = new PotenciaContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_potencia);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			match(T__17);
			setState(119);
			match(T__5);
			setState(120);
			match(ID);
			setState(121);
			match(T__6);
			setState(122);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RaizCuadradaContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SimpleLangParser.ID, 0); }
		public RaizCuadradaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_raizCuadrada; }
	}

	public final RaizCuadradaContext raizCuadrada() throws RecognitionException {
		RaizCuadradaContext _localctx = new RaizCuadradaContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_raizCuadrada);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			match(T__18);
			setState(125);
			match(T__5);
			setState(126);
			match(ID);
			setState(127);
			match(T__6);
			setState(128);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OrContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public OrContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MenorIgualQueContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public MenorIgualQueContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParentesisContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ParentesisContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StringContext extends ExprContext {
		public TerminalNode STRING() { return getToken(SimpleLangParser.STRING, 0); }
		public StringContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MultiplicacionContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public MultiplicacionContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MayorIgualQueContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public MayorIgualQueContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class EscribirDosContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public EscribirDosContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntContext extends ExprContext {
		public TerminalNode INT() { return getToken(SimpleLangParser.INT, 0); }
		public IntContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SumaContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public SumaContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PotenciasExprContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public PotenciasExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RaizCuaExprContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public RaizCuaExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AndContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public AndContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DiferenteDeContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public DiferenteDeContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IgualQueContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public IgualQueContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DivisionContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public DivisionContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IDContext extends ExprContext {
		public TerminalNode ID() { return getToken(SimpleLangParser.ID, 0); }
		public IDContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MayorQueContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public MayorQueContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BooleanContext extends ExprContext {
		public TerminalNode BOOL() { return getToken(SimpleLangParser.BOOL, 0); }
		public BooleanContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MenorQueContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public MenorQueContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RestaContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public RestaContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 22;
		enterRecursionRule(_localctx, 22, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__5:
				{
				_localctx = new ParentesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(131);
				match(T__5);
				setState(132);
				expr(0);
				setState(133);
				match(T__6);
				}
				break;
			case T__17:
				{
				_localctx = new PotenciasExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(135);
				match(T__17);
				setState(136);
				match(T__5);
				setState(137);
				expr(0);
				setState(138);
				match(T__6);
				}
				break;
			case T__18:
				{
				_localctx = new RaizCuaExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(140);
				match(T__18);
				setState(141);
				match(T__5);
				setState(142);
				expr(0);
				setState(143);
				match(T__6);
				}
				break;
			case ID:
				{
				_localctx = new IDContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(145);
				match(ID);
				}
				break;
			case INT:
				{
				_localctx = new IntContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(146);
				match(INT);
				}
				break;
			case STRING:
				{
				_localctx = new StringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(147);
				match(STRING);
				}
				break;
			case BOOL:
				{
				_localctx = new BooleanContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(148);
				match(BOOL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(192);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(190);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
					case 1:
						{
						_localctx = new AndContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(151);
						if (!(precpred(_ctx, 20))) throw new FailedPredicateException(this, "precpred(_ctx, 20)");
						setState(152);
						match(T__19);
						setState(153);
						expr(21);
						}
						break;
					case 2:
						{
						_localctx = new OrContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(154);
						if (!(precpred(_ctx, 19))) throw new FailedPredicateException(this, "precpred(_ctx, 19)");
						setState(155);
						match(T__20);
						setState(156);
						expr(20);
						}
						break;
					case 3:
						{
						_localctx = new MenorQueContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(157);
						if (!(precpred(_ctx, 18))) throw new FailedPredicateException(this, "precpred(_ctx, 18)");
						setState(158);
						match(T__21);
						setState(159);
						expr(19);
						}
						break;
					case 4:
						{
						_localctx = new MayorQueContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(160);
						if (!(precpred(_ctx, 17))) throw new FailedPredicateException(this, "precpred(_ctx, 17)");
						setState(161);
						match(T__22);
						setState(162);
						expr(18);
						}
						break;
					case 5:
						{
						_localctx = new IgualQueContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(163);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(164);
						match(T__23);
						setState(165);
						expr(17);
						}
						break;
					case 6:
						{
						_localctx = new MenorIgualQueContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(166);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(167);
						match(T__24);
						setState(168);
						expr(16);
						}
						break;
					case 7:
						{
						_localctx = new MayorIgualQueContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(169);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(170);
						match(T__24);
						setState(171);
						expr(15);
						}
						break;
					case 8:
						{
						_localctx = new DiferenteDeContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(172);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(173);
						match(T__25);
						setState(174);
						expr(14);
						}
						break;
					case 9:
						{
						_localctx = new SumaContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(175);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(176);
						match(T__26);
						setState(177);
						expr(10);
						}
						break;
					case 10:
						{
						_localctx = new RestaContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(178);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(179);
						match(T__27);
						setState(180);
						expr(9);
						}
						break;
					case 11:
						{
						_localctx = new MultiplicacionContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(181);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(182);
						match(T__28);
						setState(183);
						expr(8);
						}
						break;
					case 12:
						{
						_localctx = new DivisionContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(184);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(185);
						match(T__29);
						setState(186);
						expr(7);
						}
						break;
					case 13:
						{
						_localctx = new EscribirDosContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(187);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(188);
						match(T__30);
						setState(189);
						expr(2);
						}
						break;
					}
					} 
				}
				setState(194);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintStatementContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public PrintStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printStatement; }
	}

	public final PrintStatementContext printStatement() throws RecognitionException {
		PrintStatementContext _localctx = new PrintStatementContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_printStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(195);
			match(T__31);
			setState(196);
			match(T__5);
			setState(197);
			expr(0);
			setState(198);
			match(T__6);
			setState(199);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 11:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 20);
		case 1:
			return precpred(_ctx, 19);
		case 2:
			return precpred(_ctx, 18);
		case 3:
			return precpred(_ctx, 17);
		case 4:
			return precpred(_ctx, 16);
		case 5:
			return precpred(_ctx, 15);
		case 6:
			return precpred(_ctx, 14);
		case 7:
			return precpred(_ctx, 13);
		case 8:
			return precpred(_ctx, 9);
		case 9:
			return precpred(_ctx, 8);
		case 10:
			return precpred(_ctx, 7);
		case 11:
			return precpred(_ctx, 6);
		case 12:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001&\u00ca\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0001\u0000\u0001\u0000\u0005\u0000\u001d\b\u0000\n\u0000\f"+
		"\u0000 \t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u00010\b\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0005"+
		"\u0003>\b\u0003\n\u0003\f\u0003A\t\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005"+
		"\u0004K\b\u0004\n\u0004\f\u0004N\t\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0005\u0004T\b\u0004\n\u0004\f\u0004W\t\u0004\u0001"+
		"\u0004\u0003\u0004Z\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0005\u0005b\b\u0005\n\u0005\f\u0005e\t"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0003\u000b\u0096\b\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b"+
		"\u00bf\b\u000b\n\u000b\f\u000b\u00c2\t\u000b\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0000\u0001\u0016\r\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u0000\u0001\u0001\u0000\r\u000f"+
		"\u00de\u0000\u001a\u0001\u0000\u0000\u0000\u0002/\u0001\u0000\u0000\u0000"+
		"\u00041\u0001\u0000\u0000\u0000\u00067\u0001\u0000\u0000\u0000\bD\u0001"+
		"\u0000\u0000\u0000\n[\u0001\u0000\u0000\u0000\fh\u0001\u0000\u0000\u0000"+
		"\u000ej\u0001\u0000\u0000\u0000\u0010p\u0001\u0000\u0000\u0000\u0012v"+
		"\u0001\u0000\u0000\u0000\u0014|\u0001\u0000\u0000\u0000\u0016\u0095\u0001"+
		"\u0000\u0000\u0000\u0018\u00c3\u0001\u0000\u0000\u0000\u001a\u001e\u0005"+
		"\u0001\u0000\u0000\u001b\u001d\u0003\u0002\u0001\u0000\u001c\u001b\u0001"+
		"\u0000\u0000\u0000\u001d \u0001\u0000\u0000\u0000\u001e\u001c\u0001\u0000"+
		"\u0000\u0000\u001e\u001f\u0001\u0000\u0000\u0000\u001f!\u0001\u0000\u0000"+
		"\u0000 \u001e\u0001\u0000\u0000\u0000!\"\u0005\u0002\u0000\u0000\"\u0001"+
		"\u0001\u0000\u0000\u0000#0\u0003\u0004\u0002\u0000$0\u0003\u0006\u0003"+
		"\u0000%0\u0003\b\u0004\u0000&0\u0003\n\u0005\u0000\'0\u0003\u0018\f\u0000"+
		"(0\u0003\u000e\u0007\u0000)0\u0003\u0010\b\u0000*0\u0003\u0012\t\u0000"+
		"+0\u0003\u0014\n\u0000,-\u0003\u0016\u000b\u0000-.\u0005\u0003\u0000\u0000"+
		".0\u0001\u0000\u0000\u0000/#\u0001\u0000\u0000\u0000/$\u0001\u0000\u0000"+
		"\u0000/%\u0001\u0000\u0000\u0000/&\u0001\u0000\u0000\u0000/\'\u0001\u0000"+
		"\u0000\u0000/(\u0001\u0000\u0000\u0000/)\u0001\u0000\u0000\u0000/*\u0001"+
		"\u0000\u0000\u0000/+\u0001\u0000\u0000\u0000/,\u0001\u0000\u0000\u0000"+
		"0\u0003\u0001\u0000\u0000\u000012\u0003\f\u0006\u000023\u0005\"\u0000"+
		"\u000034\u0005\u0004\u0000\u000045\u0003\u0016\u000b\u000056\u0005\u0003"+
		"\u0000\u00006\u0005\u0001\u0000\u0000\u000078\u0005\u0005\u0000\u0000"+
		"89\u0005\"\u0000\u00009:\u0005\u0006\u0000\u0000:;\u0005\u0007\u0000\u0000"+
		";?\u0005\b\u0000\u0000<>\u0003\u0002\u0001\u0000=<\u0001\u0000\u0000\u0000"+
		">A\u0001\u0000\u0000\u0000?=\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000"+
		"\u0000@B\u0001\u0000\u0000\u0000A?\u0001\u0000\u0000\u0000BC\u0005\t\u0000"+
		"\u0000C\u0007\u0001\u0000\u0000\u0000DE\u0005\n\u0000\u0000EF\u0005\u0006"+
		"\u0000\u0000FG\u0003\u0016\u000b\u0000GH\u0005\u0007\u0000\u0000HL\u0005"+
		"\b\u0000\u0000IK\u0003\u0002\u0001\u0000JI\u0001\u0000\u0000\u0000KN\u0001"+
		"\u0000\u0000\u0000LJ\u0001\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000"+
		"MO\u0001\u0000\u0000\u0000NL\u0001\u0000\u0000\u0000OY\u0005\t\u0000\u0000"+
		"PQ\u0005\u000b\u0000\u0000QU\u0005\b\u0000\u0000RT\u0003\u0002\u0001\u0000"+
		"SR\u0001\u0000\u0000\u0000TW\u0001\u0000\u0000\u0000US\u0001\u0000\u0000"+
		"\u0000UV\u0001\u0000\u0000\u0000VX\u0001\u0000\u0000\u0000WU\u0001\u0000"+
		"\u0000\u0000XZ\u0005\t\u0000\u0000YP\u0001\u0000\u0000\u0000YZ\u0001\u0000"+
		"\u0000\u0000Z\t\u0001\u0000\u0000\u0000[\\\u0005\f\u0000\u0000\\]\u0005"+
		"\u0006\u0000\u0000]^\u0003\u0016\u000b\u0000^_\u0005\u0007\u0000\u0000"+
		"_c\u0005\b\u0000\u0000`b\u0003\u0002\u0001\u0000a`\u0001\u0000\u0000\u0000"+
		"be\u0001\u0000\u0000\u0000ca\u0001\u0000\u0000\u0000cd\u0001\u0000\u0000"+
		"\u0000df\u0001\u0000\u0000\u0000ec\u0001\u0000\u0000\u0000fg\u0005\t\u0000"+
		"\u0000g\u000b\u0001\u0000\u0000\u0000hi\u0007\u0000\u0000\u0000i\r\u0001"+
		"\u0000\u0000\u0000jk\u0005\u0010\u0000\u0000kl\u0005\u0006\u0000\u0000"+
		"lm\u0005\"\u0000\u0000mn\u0005\u0007\u0000\u0000no\u0005\u0003\u0000\u0000"+
		"o\u000f\u0001\u0000\u0000\u0000pq\u0005\u0011\u0000\u0000qr\u0005\u0006"+
		"\u0000\u0000rs\u0005\"\u0000\u0000st\u0005\u0007\u0000\u0000tu\u0005\u0003"+
		"\u0000\u0000u\u0011\u0001\u0000\u0000\u0000vw\u0005\u0012\u0000\u0000"+
		"wx\u0005\u0006\u0000\u0000xy\u0005\"\u0000\u0000yz\u0005\u0007\u0000\u0000"+
		"z{\u0005\u0003\u0000\u0000{\u0013\u0001\u0000\u0000\u0000|}\u0005\u0013"+
		"\u0000\u0000}~\u0005\u0006\u0000\u0000~\u007f\u0005\"\u0000\u0000\u007f"+
		"\u0080\u0005\u0007\u0000\u0000\u0080\u0081\u0005\u0003\u0000\u0000\u0081"+
		"\u0015\u0001\u0000\u0000\u0000\u0082\u0083\u0006\u000b\uffff\uffff\u0000"+
		"\u0083\u0084\u0005\u0006\u0000\u0000\u0084\u0085\u0003\u0016\u000b\u0000"+
		"\u0085\u0086\u0005\u0007\u0000\u0000\u0086\u0096\u0001\u0000\u0000\u0000"+
		"\u0087\u0088\u0005\u0012\u0000\u0000\u0088\u0089\u0005\u0006\u0000\u0000"+
		"\u0089\u008a\u0003\u0016\u000b\u0000\u008a\u008b\u0005\u0007\u0000\u0000"+
		"\u008b\u0096\u0001\u0000\u0000\u0000\u008c\u008d\u0005\u0013\u0000\u0000"+
		"\u008d\u008e\u0005\u0006\u0000\u0000\u008e\u008f\u0003\u0016\u000b\u0000"+
		"\u008f\u0090\u0005\u0007\u0000\u0000\u0090\u0096\u0001\u0000\u0000\u0000"+
		"\u0091\u0096\u0005\"\u0000\u0000\u0092\u0096\u0005#\u0000\u0000\u0093"+
		"\u0096\u0005$\u0000\u0000\u0094\u0096\u0005%\u0000\u0000\u0095\u0082\u0001"+
		"\u0000\u0000\u0000\u0095\u0087\u0001\u0000\u0000\u0000\u0095\u008c\u0001"+
		"\u0000\u0000\u0000\u0095\u0091\u0001\u0000\u0000\u0000\u0095\u0092\u0001"+
		"\u0000\u0000\u0000\u0095\u0093\u0001\u0000\u0000\u0000\u0095\u0094\u0001"+
		"\u0000\u0000\u0000\u0096\u00c0\u0001\u0000\u0000\u0000\u0097\u0098\n\u0014"+
		"\u0000\u0000\u0098\u0099\u0005\u0014\u0000\u0000\u0099\u00bf\u0003\u0016"+
		"\u000b\u0015\u009a\u009b\n\u0013\u0000\u0000\u009b\u009c\u0005\u0015\u0000"+
		"\u0000\u009c\u00bf\u0003\u0016\u000b\u0014\u009d\u009e\n\u0012\u0000\u0000"+
		"\u009e\u009f\u0005\u0016\u0000\u0000\u009f\u00bf\u0003\u0016\u000b\u0013"+
		"\u00a0\u00a1\n\u0011\u0000\u0000\u00a1\u00a2\u0005\u0017\u0000\u0000\u00a2"+
		"\u00bf\u0003\u0016\u000b\u0012\u00a3\u00a4\n\u0010\u0000\u0000\u00a4\u00a5"+
		"\u0005\u0018\u0000\u0000\u00a5\u00bf\u0003\u0016\u000b\u0011\u00a6\u00a7"+
		"\n\u000f\u0000\u0000\u00a7\u00a8\u0005\u0019\u0000\u0000\u00a8\u00bf\u0003"+
		"\u0016\u000b\u0010\u00a9\u00aa\n\u000e\u0000\u0000\u00aa\u00ab\u0005\u0019"+
		"\u0000\u0000\u00ab\u00bf\u0003\u0016\u000b\u000f\u00ac\u00ad\n\r\u0000"+
		"\u0000\u00ad\u00ae\u0005\u001a\u0000\u0000\u00ae\u00bf\u0003\u0016\u000b"+
		"\u000e\u00af\u00b0\n\t\u0000\u0000\u00b0\u00b1\u0005\u001b\u0000\u0000"+
		"\u00b1\u00bf\u0003\u0016\u000b\n\u00b2\u00b3\n\b\u0000\u0000\u00b3\u00b4"+
		"\u0005\u001c\u0000\u0000\u00b4\u00bf\u0003\u0016\u000b\t\u00b5\u00b6\n"+
		"\u0007\u0000\u0000\u00b6\u00b7\u0005\u001d\u0000\u0000\u00b7\u00bf\u0003"+
		"\u0016\u000b\b\u00b8\u00b9\n\u0006\u0000\u0000\u00b9\u00ba\u0005\u001e"+
		"\u0000\u0000\u00ba\u00bf\u0003\u0016\u000b\u0007\u00bb\u00bc\n\u0001\u0000"+
		"\u0000\u00bc\u00bd\u0005\u001f\u0000\u0000\u00bd\u00bf\u0003\u0016\u000b"+
		"\u0002\u00be\u0097\u0001\u0000\u0000\u0000\u00be\u009a\u0001\u0000\u0000"+
		"\u0000\u00be\u009d\u0001\u0000\u0000\u0000\u00be\u00a0\u0001\u0000\u0000"+
		"\u0000\u00be\u00a3\u0001\u0000\u0000\u0000\u00be\u00a6\u0001\u0000\u0000"+
		"\u0000\u00be\u00a9\u0001\u0000\u0000\u0000\u00be\u00ac\u0001\u0000\u0000"+
		"\u0000\u00be\u00af\u0001\u0000\u0000\u0000\u00be\u00b2\u0001\u0000\u0000"+
		"\u0000\u00be\u00b5\u0001\u0000\u0000\u0000\u00be\u00b8\u0001\u0000\u0000"+
		"\u0000\u00be\u00bb\u0001\u0000\u0000\u0000\u00bf\u00c2\u0001\u0000\u0000"+
		"\u0000\u00c0\u00be\u0001\u0000\u0000\u0000\u00c0\u00c1\u0001\u0000\u0000"+
		"\u0000\u00c1\u0017\u0001\u0000\u0000\u0000\u00c2\u00c0\u0001\u0000\u0000"+
		"\u0000\u00c3\u00c4\u0005 \u0000\u0000\u00c4\u00c5\u0005\u0006\u0000\u0000"+
		"\u00c5\u00c6\u0003\u0016\u000b\u0000\u00c6\u00c7\u0005\u0007\u0000\u0000"+
		"\u00c7\u00c8\u0005\u0003\u0000\u0000\u00c8\u0019\u0001\u0000\u0000\u0000"+
		"\n\u001e/?LUYc\u0095\u00be\u00c0";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}