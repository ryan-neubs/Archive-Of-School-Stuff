# parser.py
#  parser for Jelle

"""Produce AST for Jelle program.

Examples
========

prog1.jle
---------
[PROGRAM,
 [DISPLAY, [STR, 'Enter the value of a:']],
 [INPUT, 'a'],
 [DISPLAY, [STR, 'Enter the value of b:']],
 [INPUT, 'b'],
 [DISPLAY, [STR, 'Enter the value of c:']],
 [INPUT, 'c'],
 [ASSIGN,
  'discrim',
  [SUB,
   [EXP, [ID, 'b'], [NUM, '2']],
   [MUL, [MUL, [NUM, '4'], [ID, 'a']], [ID, 'c']]]],
 [ASSIGN, 'discroot', [EXP, [ID, 'discrim'], [NUM, '.5']]],
 [DISPLAY,
  [STR, 'root1 is'],
  [DIV,
   [ADD, [NEG, [ID, 'b']], [ID, 'discroot']],
   [MUL, [NUM, '2'], [ID, 'a']]]],
 [DISPLAY,
  [STR, 'root2 is'],
  [DIV,
   [SUB, [NEG, [ID, 'b']], [ID, 'discroot']],
   [MUL, [NUM, '2'], [ID, 'a']]]]]


prog2.jle
---------
[PROGRAM,
 [DISPLAY, [STR, 'Enter values of a, b and c: ']],
 [INPUT, 'a', 'b', 'c'],
 [ASSIGN,
  'discroot',
  [CALL,
   'sqrt',
   [SUB,
    [EXP, [ID, 'b'], [NUM, '2']],
    [MUL, [MUL, [NUM, '4'], [ID, 'a']], [ID, 'c']]]]],
 [DISPLAY,
  [STR, 'root1 is'],
  [DIV,
   [ADD, [NEG, [ID, 'b']], [ID, 'discroot']],
   [MUL, [NUM, '2'], [ID, 'a']]],
  [STR, '\n']],
 [DISPLAY,
  [STR, 'root2 is'],
  [DIV,
   [SUB, [NEG, [ID, 'b']], [ID, 'discroot']],
   [MUL, [NUM, '2'], [ID, 'a']]],
  [STR, '\n']]]

"""

import enum
from lexer import Lexer, TokCat


class AST(enum.Enum):
    PROGRAM = 0
    INPUT = 1
    ASSIGN = 2
    DISPLAY = 3
    ADD = 4
    SUB = 5
    MUL = 6
    DIV = 7
    MOD = 8
    NEG = 9
    EXP = 10
    ID = 11
    NUM = 12
    STR = 13
    CALL = 14

    def __repr__(self):
        return self.name

class JelleParser:
    """ Parser class """

    def __init__(self, progstr):
        self.tokens = Lexer(progstr)

    def parse_program(self):
        """ <PROGRAM> ::= {<STMT> SEMI} """
        ast = [AST.PROGRAM]
        while self.tokens.peek != TokCat.END:
            ast.append(self.parse_stmt())
            self.tokens.expect(TokCat.SEMI)
        return ast

    def parse_stmt(self):
        """ <STMT> ::= <INPUT_STMT> | <ASSIGN_STMT> | <DISPLAY_STMT> """
        token = self.tokens.expect(TokCat.INPUT, TokCat.ID, TokCat.DISPLAY,
                                   consume=False)
        if token == TokCat.INPUT:
            return self.parse_input()
        elif token == TokCat.ID:
            return self.parse_assignment()
        else:
            return self.parse_display()

    def parse_input(self):
        """   <INPUT_STMT> ::= INPUT ID {COMMA ID} """
        input = [AST.INPUT]
        tokens = self.tokens
        tokens.expect(TokCat.INPUT)
        input.append(self.tokens.peek.lexeme)
        tokens.expect(TokCat.ID)
        while tokens.peek == TokCat.COMMA:
            input.append(tokens.get().lexeme)
            tokens.expect(TokCat.ID)
        return input

    def parse_assignment(self):
        """  <ASSIGN_STMT> ::= ID ASSIGN <E> """
        assign = [AST.ASSIGN]
        self.tokens.expect(TokCat.ID)
        self.tokens.expect(TokCat.ASSIGN)
        assign.append(self.tokens.peek.lexeme)
        assign.append(self.parse_expr())
        return assign

    def parse_display(self):
        """ <DiSPLAY_STMT> ::= DISPLAY <DISPLAY_ARG> {COMMA <DSIPLAY_ARG} """
        display = [AST.DISPLAY]
        self.tokens.expect(TokCat.DISPLAY)
        display.append(self.parse_display_arg())
        while self.tokens.peek == TokCat.COMMA:
            self.tokens.get()
            display.append(self.parse_display_arg())
        return display

    def parse_display_arg(self):
        """ <DISPLAY_ARG> ::= STRING | NL | <E> """
        if self.tokens.peek == TokCat.STRING:
            return [AST.STR, self.tokens.get().lexeme.strip('"')]
        elif self.tokens.peek == TokCat.NL:
            self.tokens.get()
            return [AST.STR, "\n"]
        else:
            return self.parse_expr()

    def parse_expr(self):
        """ <E> ::= <E1> {ADDOP <E1>} """
        expr = self.parse_expr1()
        while self.tokens.peek == TokCat.ADDOP:
            if self.tokens.peek.lexeme == "+":
                expr = [AST.ADD, expr]
            else:
                expr = [AST.SUB, expr]
            self.tokens.get()
            expr.append(self.parse_expr1())
        return expr

    def parse_expr1(self):
        """ <E1> ::= <E2> {MULOP <E2>} """
        expr1 = self.parse_expr2()
        while self.tokens.peek == TokCat.MULOP:
            token = self.tokens.get()
            if token.lexeme == "*":
                expr1 = [AST.MUL, expr1, self.parse_expr2()]
            elif token.lexeme == "/":
                expr1 = [AST.DIV, expr1, self.parse_expr2()]
            else:
                expr1 = [AST.MOD, expr1, self.parse_expr2()]
        return expr1

    def parse_expr2(self):
        """ <E2> ::= {ADDOP} <E3> """
        count = 0
        while self.tokens.peek == TokCat.ADDOP:
            if self.tokens.peek.lexeme == "-":
                count += 1
            self.tokens.get()
        if count % 2 != 0:
            return [AST.NEG, self.parse_expr3()]
        return self.parse_expr3()

    def parse_expr3(self):
        """ <E3> ::= <E4> EXPOP <E2> | <E4> """
        expr3 = self.parse_expr4()
        if self.tokens.peek == TokCat.EXPOP:
            expr3 = [AST.EXP, expr3]
            self.tokens.get()
            expr3.append(self.parse_expr2())
        return expr3
        

    def parse_expr4(self):
        """ <E4> ::= NUMBER | LPAREN <E> RPAREN | ID 
                   | ID LPAREN [<E> {COMMA <E>}] RPAREN
        """
        node = []
        tokens = self.tokens
        peek = tokens.expect(TokCat.NUMBER,
                             TokCat.LPAREN,
                             TokCat.ID)
        if peek == TokCat.NUMBER:
            node.append(AST.NUM)
            node.append(peek.lexeme)
        elif peek == TokCat.LPAREN:
            node.append(self.parse_expr())
            tokens.expect(TokCat.RPAREN)
        elif peek == TokCat.ID:
            if tokens.peek == TokCat.LPAREN:
                self.tokens.get()
                node.append(AST.CALL)
                node.append(peek.lexeme)
                if tokens.peek != TokCat.RPAREN:
                    node.append(self.parse_expr())
                    while tokens.peek == TokCat.COMMA:
                        tokens.get()
                        node.append(self.parse_expr())
                tokens.expect(TokCat.RPAREN)
                return node
            node.append(AST.ID)
            node.append(peek.lexeme)
        return node
    
def parse(fname):  
    with open(fname) as infile:
        program = infile.read()
    parser = JelleParser(program)
    return parser.parse_program()


if __name__ == "__main__":
    import pprint
    import sys
    #ast = parse(sys.argv[1])     # command line filename
    ast = parse(input("file: "))  # prompt for filename
    pprint.pprint(ast)
