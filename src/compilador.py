import sys
from antlr4 import *

#Clases generadas por ANTLR4
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor

class SimpleLangVisitor(ParseTreeVisitor):

    def __init__(self):
        #Diccionario para almacenar variables
        self.variables = {}

    #Funcion para procesar el programa completo
    def visitProgram(self, ctx: SimpleLangParser.ProgramContext):
        #Recorre todas las declaraciones del programa
        for statement in ctx.statement():
            self.visit(statement)

    #Metodo para procesar las declaraciones de variables
    def visitVarDeclaration(self, ctx: SimpleLangParser.VarDeclarationContext):
        #Obtencion del nombre y valor de las variables
        var_name = ctx.ID().getText() 
        value = ctx.expr().getText()  

        #Traduccion y evaluacion de las variables
        value = self.translate_statement(value) 
        value = self.replace_logical_operators(value)        
        python_code = f"{var_name} = {value}"  

        #Ejecucion del codigo en lenguaje python
        exec(python_code, globals()) 


    #Metodo para manejar declaraciones condicionales
    def visitIfStatement(self, ctx: SimpleLangParser.IfStatementContext):
        #Obtencion de la condicion y su cuerpo
        condition = ctx.expr().getText()
        condition = self.replace_logical_operators(condition)
        if_body = self.translate_statement(ctx.statement(0).getText())

        #Traduccion y validacion
        python_code = f"if {condition}:\n    {if_body.replace('\\n', '\\n    ')}"
        if ctx.statement(1) is not None:
            else_body = self.translate_statement(ctx.statement(1).getText())
            python_code += f"\nelse:\n    {else_body.replace('\\n', '\\n    ')}"

        #Ejecucion del codigo en lenguaje python
        exec(python_code, globals())

    #Metodo para manejar los bucles
    def visitLoopStatement(self, ctx: SimpleLangParser.LoopStatementContext):
        #Obtencion de la condicion y el cuerpo del bucle
        condition = ctx.expr().getText()
        condition = self.replace_logical_operators(condition)
        loop_body = "\n    ".join([self.translate_statement(statement.getText()) for statement in ctx.statement()])
        
        #Traduccion
        python_code = f"while {condition}:\n    {loop_body}"
        
        #Ejecucion del codigo en lenguaje python
        exec(python_code, globals())


    #Manejo de los imprimir
    def visitPrintStatement(self, ctx: SimpleLangParser.PrintStatementContext):
        #Obtencion de la sentencia y valor
        value = ctx.expr().getText()

        #Validacion y traduccion
        value = self.replace_logical_operators(value)
        value = self.translate_statement(value) 
        python_code = f"print({value})"

        #Ejecucion del codigo en lenguaje python
        exec(python_code, globals())

    #Traductor de las sentencias
    def translate_statement(self, statement_text):
        if "escribir" in statement_text:
            return statement_text.replace("escribir", "print")
        
        if "aumentar" in statement_text:
            statement_text = statement_text.replace("aumentar", "").strip("()")
            statement_text = statement_text.replace(");", "").strip("()")
            return f"{statement_text} += 1;"
        
        if "disminuir" in statement_text:
            statement_text = statement_text.replace("disminuir", "").strip("()")
            statement_text = statement_text.replace(");", "").strip("()")
            return f"{statement_text} -= 1"
        
        if "potencia" in statement_text:
            statement_text = statement_text.replace("potencia", "")
            statement_text = statement_text.replace(");", "").strip("()")
            return f"{statement_text} ** 2" 
        
        if "raizCuadrada" in statement_text:
            statement_text = statement_text.replace("raizCuadrada", "")
            statement_text = statement_text.replace(");", "").strip("()")
            return f"{statement_text} ** 0.5" 
        return statement_text
    
    #Traductor de los operadores logicos
    def replace_logical_operators(self, expression):
        expression = expression.replace('igual que', '==')
        expression = expression.replace('menor que', '<')
        expression = expression.replace('mayor que', '>')
        expression = expression.replace('menor igual a', '<=')
        expression = expression.replace('mayor igual a', '>=')
        expression = expression.replace('diferente de', '!=')
        expression = expression.replace('y que', 'and')
        expression = expression.replace('o que', 'or')
        
        return expression

#Metodo main
def main():
    if len(sys.argv) != 2:
        print("Error: debes ejecutar el programa de la siguiente forma: python main.py <archivo.magia>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        #Verifica que el archivo tenga la extension .magia
        if not input_file.endswith(".magia"):
            print(f"Error: El archivo '{input_file}' no tiene la extensión '.magia'.")
            sys.exit(1)

        #Obtien el programa .magia
        input_stream = FileStream(input_file, encoding="utf-8")

        #Hace uso del lexer y parser proporcionados por ANTLR4
        lexer = SimpleLangLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SimpleLangParser(token_stream)

        #Crea el arbol de sintaxis del programa
        tree = parser.program()

        print("----------------------------")
        print("Salida del programa:")

        #El visitor evalua el arbol y compilador
        visitor = SimpleLangVisitor()
        visitor.visit(tree)

        print("----------------------------")
        print("Ejecución completada.")
        
    except FileNotFoundError:
        print(f"Error: El archivo '{input_file}' no existe.")
        sys.exit(1)

if __name__ == "__main__":
    main()
