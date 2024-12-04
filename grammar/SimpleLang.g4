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
    | aumentar            # AumentarEnUno
    | disminuir           # DisminuirEnUno
    | potencia            # Potencias
    | raizCuadrada        # RaizCua
    | expr ';'            # Expresion
    ;

//Declaraciones
varDeclaration: tipo ID '=' expr ';';
functionDeclaration: 'hacer esto' ID '(' ')' '{' statement* '}';

//Condicionales y bucles
ifStatement: 'Si pasa esto' '(' expr ')' '{' statement* '}' ('Sino' '{' statement* '}')?;
loopStatement: 'Repetir mientras que' '(' expr ')' '{' statement* '}';

//Tipos de variables y expresiones
tipo: 'numero' | 'texto' | 'logico';

//++ y --
aumentar: 'aumentar' '(' ID ')' ';';
disminuir: 'disminuir' '(' ID ')' ';';

//Potencia y raiz
potencia: 'potencia' '(' ID ')' ';';
raizCuadrada: 'raizCuadrada' '(' ID ')' ';';

expr
    : expr 'y' expr                       # And
    | expr 'o' expr                       # Or
    | expr 'menor que' expr               # MenorQue
    | expr 'mayor que' expr               # MayorQue
    | expr 'igual que' expr               # IgualQue
    | expr 'menor igual a' expr           # MenorIgualQue
    | expr 'menor igual a' expr           # MayorIgualQue
    | expr 'diferente de' expr            # DiferenteDe
    | '(' expr ')'                        # Parentesis
    | expr '*' expr                       # Suma
    | expr '/' expr                       # Resta
    | expr '+' expr                       # Multiplicacion
    | expr '-' expr                       # Division
    | ID                                  # ID
    | INT                                 # Int
    | STRING                              # String
    | BOOL                                # Boolean
    ;

//Para imprimir
printStatement: 'escribir' '(' expr ')' ';';

//Tokens
ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
STRING: '"' .*? '"';
BOOL: 'verdadero' | 'falso';
WS: [ \t\r\n]+ -> skip;
