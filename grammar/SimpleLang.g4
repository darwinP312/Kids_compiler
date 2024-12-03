grammar SimpleLang;

//Inicio y fin del programa
program: 'Empecemos!' statement* 'Hasta luego!';

//Sentencias
statement
    : varDeclaration      # DeclaracionDeVariable
    | functionDeclaration # DeclaracionDeFuncion
    | ifStatement         # Condicional
    | loopStatement       # Ciclo
    | printStatement      # Escribir
    | expr ';'            # Expresion
    ;

//Declaraciones
varDeclaration: type ID '=' expr ';';
functionDeclaration: 'hacer esto' ID '(' ')' '{' statement* '}';

//Condicionales y bucles
ifStatement: 'Si pasa esto' '(' expr ')' '{' statement* '}' ('Sino' '{' statement* '}')?;
loopStatement: 'Repetir hasta que' '(' expr ')' '{' statement* '}';

//Tipos de variables y expresiones
type: 'numero' | 'texto' | 'logico';

expr
    : expr ('*' | '/') expr               # MulDiv
    | expr ('+' | '-') expr               # AddSub
    | expr ('>' | '<' | '>=' | '<=' | '==' | '!=') expr # Comparacion
    | '(' expr ')'                        # Parenthesis
    | ID                                  # Identifier
    | INT                                 # IntLiteral
    | STRING                              # StringLiteral
    | BOOL                                # BooleanLiteral
    ;

//Para imprimir
printStatement: 'escribir' '(' expr ')' ';';

//Tokens
ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
STRING: '"' .*? '"';
BOOL: 'verdadero' | 'falso';
WS: [ \t\r\n]+ -> skip;
