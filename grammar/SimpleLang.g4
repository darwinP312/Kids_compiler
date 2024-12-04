grammar SimpleLang;

//Regla para el programa
program: 'Empecemos!' statement* 'Hasta luego!';

//Sentencias
statement
    : varDeclaration      # DeclaracionVariable
    | functionDeclaration # DeclaracionFuncion
    | ifStatement         # Condicional
    | loopStatement       # Ciclo
    | printStatement      # Escribir
    | expr ';'            # Expresion
    ;

//Declaraciones
varDeclaration: tipo ID '=' expr ';';
functionDeclaration: 'hacer esto' ID '(' ')' '{' statement* '}';

//Condicionales y bucles
ifStatement: 'Si pasa esto' '(' expr ')' '{' statement* '}' ('Sino' '{' statement* '}')?;
loopStatement: 'Repetir hasta que' '(' expr ')' '{' statement* '}';

//Tipos de variables y expresiones
tipo: 'numero' | 'texto' | 'logico';

expr
    : expr ('*' | '/') expr                     # MulDiv
    | expr ('+' | '-') expr                     # SumaResta
    | expr ('>' | '<' | '>=' | '<=' | '==' | '!=') expr # Comparacion
    | '(' expr ')'                              # Parentesis
    | ID                                         # ID
    | INT                                        # Int
    | STRING                                     # String
    | BOOL                                       # Boolean
    ;

//Para imprimir
printStatement: 'escribir' '(' expr ')' ';';

//Tokens
ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
STRING: '"' .*? '"';
BOOL: 'verdadero' | 'falso';
WS: [ \t\r\n]+ -> skip;
