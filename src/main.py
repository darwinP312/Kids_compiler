import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor

class SimpleLangExecutor(SimpleLangVisitor):
    def __init__(self):
        super().__init__()
        self.variables = {}  

    def visitProgram(self, ctx):
        print("Iniciando el recorrido del programa")
        return self.visitChildren(ctx)

    def visitDeclaracionVariable(self, ctx):
        varDeclarationCtx = ctx.varDeclaration()
        var_type = varDeclarationCtx.tipo().getText()
        var_name = varDeclarationCtx.ID().getText()
        var_value = self.visit(varDeclarationCtx.expr())
        self.variables[var_name] = var_value
        print(f"Variable declarada: {var_name} = {var_value} (tipo: {var_type})")
        return None

    def visitDeclaracionFuncion(self, ctx):
        id = ctx.ID().getText()
        print(f"Visitando declaración de función: {id}")
        return self.visitChildren(ctx)

    def visitCondicional(self, ctx):
        print("Visitando condicional")
        if_stmt = ctx.ifStatement()
        condition = self.visit(if_stmt.expr())
        if condition:
            print("Condición verdadera, ejecutando bloque if")
            self.visit(if_stmt.statement(0))
        else:
            print("Condición falsa, ejecutando bloque else")
            # Verificar si existe un bloque else y visitar sus declaraciones
            if len(if_stmt.statement()) > 1:
                self.visit(if_stmt.statement(1))
        return None

    def visitCiclo(self, ctx):
        print("Visitando ciclo")
        while self.visit(ctx.expr()):
            print("Ejecutando cuerpo del ciclo")
            for statement in ctx.statement():
                self.visit(statement)
        return None

    def visitEscribir(self, ctx):
        print("Visitando instrucción escribir")
        value = self.visit(ctx.printStatement().expr())
        print(f"Escribir: {value}")
        return None

    def visitExpr(self, ctx):
        if ctx.INT():
            print(f"Visitando expresión numérica: {ctx.INT().getText()}")
            return int(ctx.INT().getText())
        elif ctx.STRING():
            print(f"Visitando expresión de cadena: {ctx.STRING().getText()}")
            return ctx.STRING().getText().strip('"')
        elif ctx.BOOL():
            print(f"Visitando expresión booleana: {ctx.BOOL().getText()}")
            return ctx.BOOL().getText() == 'verdadero'
        elif ctx.ID():
            print(f"Visitando variable: {ctx.ID().getText()}")
            value = self.variables.get(ctx.ID().getText(), None)
            print(f"Valor de la variable {ctx.ID().getText()}: {value}")
            return value
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() in ['+', '-', '*', '/']:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            operator = ctx.getChild(1).getText()
            print(f"Operador: {operator}, Izquierda: {left}, Derecha: {right}")
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right
            elif operator == '/':
                return left / right
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() in ['>', '<', '>=', '<=', '==', '!=']:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            operator = ctx.getChild(1).getText()
            print(f"Operador: {operator}, Izquierda: {left}, Derecha: {right}")
            if operator == '>':
                return left > right
            elif operator == '<':
                return left < right
            elif operator == '>=':
                return left >= right
            elif operator == '<=':
                return left <= right
            elif operator == '==':
                return left == right
            elif operator == '!=':
                return left != right
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return None

#Main
def main(argv):
    input_file = argv[1] if len(argv) > 1 else "prueba.magia"
    print(f"Cargando archivo: {input_file}")
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = SimpleLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleLangParser(stream)
    tree = parser.program()
    print("Árbol de sintaxis generado:")
    print(Trees.toStringTree(tree, None, parser))
    executor = SimpleLangExecutor()
    executor.visit(tree)

if __name__ == "__main__":
    main(sys.argv)
