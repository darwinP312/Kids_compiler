import sys
from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor

class Interpreter(SimpleLangVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx: SimpleLangParser.ProgramContext):
        #Recorre el arbol de sintaxis y ejecuta las sentencias
        return self.visitChildren(ctx)

    def visitPrintStatement(self, ctx: SimpleLangParser.PrintStatementContext):
        #Obtiene el contenido de la expresion
        python_code = f'print({ctx.expr().getText()})'  # Genera código Python equivalente
        
        #Ejecuta el código interpretado
        exec(python_code)

        return None

    def visitVarDeclaration(self, ctx: SimpleLangParser.VarDeclarationContext):
        var_name = ctx.ID().getText()
        value = ctx.expr().getText()
        
        #Genera código Python 
        python_code = f"{var_name} = {value}"
        
        # Ejecuta el código interpretado
        exec(python_code, globals())

        return None

    def visitExpr(self, ctx: SimpleLangParser.ExprContext):
        return ctx.getText() 


def main():
    #Lee el archivo .magia
    input_stream = FileStream("prueba.magia")
    
    #Crea el lexer y el parser
    lexer = SimpleLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleLangParser(stream)
    
    #Analiza el codigo y crea el arbol de sintaxis
    tree = parser.program()
    
    #print("Árbol de sintaxis:")
    #print(tree.toStringTree(recog=parser)) 
    
    #Ejecuta el código con el intérprete
    interpreter = Interpreter()
    interpreter.visit(tree)


if __name__ == '__main__':
    main()
