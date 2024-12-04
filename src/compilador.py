import sys
from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor

class SimpleLangVisitor(ParseTreeVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx: SimpleLangParser.ProgramContext):
        for statement in ctx.statement():
            self.visit(statement)

    def visitVarDeclaration(self, ctx: SimpleLangParser.VarDeclarationContext):
        var_name = ctx.ID().getText()
        value = ctx.expr().getText()
        value = self.replace_logical_operators(value)
        python_code = f"{var_name} = {value}"
        exec(python_code, globals())

    def visitIfStatement(self, ctx: SimpleLangParser.IfStatementContext):
        condition = ctx.expr().getText()
        condition = self.replace_logical_operators(condition)
        if_body = self.translate_statement(ctx.statement(0).getText())
        python_code = f"if {condition}:\n    {if_body.replace('\\n', '\\n    ')}"
        if ctx.statement(1) is not None:
            else_body = self.translate_statement(ctx.statement(1).getText())
            python_code += f"\nelse:\n    {else_body.replace('\\n', '\\n    ')}"
        exec(python_code, globals())

    def visitPrintStatement(self, ctx: SimpleLangParser.PrintStatementContext):
        value = ctx.expr().getText()
        value = self.replace_logical_operators(value)
        python_code = f"print({value})"
        exec(python_code, globals())

    def visitAumentar(self, ctx: SimpleLangParser.AumentarContext):
        var_name = ctx.ID().getText()
        python_code = f"{var_name} += 1"
        exec(python_code, globals())

    def visitDisminuir(self, ctx: SimpleLangParser.DisminuirContext):
        var_name = ctx.ID().getText()
        python_code = f"{var_name} -= 1"
        exec(python_code, globals())

    def translate_statement(self, statement_text):
        if "escribir" in statement_text:
            return statement_text.replace("escribir", "print")
        return statement_text

    def replace_logical_operators(self, expression):
        expression = expression.replace('igual que', '==')
        expression = expression.replace('menor que', '<')
        expression = expression.replace('mayor que', '>')
        expression = expression.replace('menor o igual que', '<=')
        expression = expression.replace('mayor o igual que', '>=')
        expression = expression.replace('diferente de', '!=')
        expression = expression.replace('y', 'and')
        expression = expression.replace('o', 'or')
        return expression


def main():
    if len(sys.argv) != 2:
        print("Error: debes ejecutar el programa de la siguiente forma: python main.py <archivo.magia>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        input_stream = FileStream(input_file, encoding="utf-8")
        lexer = SimpleLangLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SimpleLangParser(token_stream)
        tree = parser.program()
        print("----------------------------")
        print("Salida del programa:")
        visitor = SimpleLangVisitor()
        visitor.visit(tree)
        print("----------------------------")
        print("Ejecución completada.")
    except FileNotFoundError:
        print(f"Error: El archivo '{input_file}' no existe.")
        sys.exit(1)

if __name__ == "__main__":
    main()