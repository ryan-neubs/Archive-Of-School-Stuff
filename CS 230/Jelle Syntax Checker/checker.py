# checker.py
# Syntax Checker for Jelle
# by Ryan Neubauer

from lexer import Lexer, TokCat


class JelleChecker:

    def __init__(self, progstr):
        self.tokens = Lexer(progstr)

    def check_program(self):
        """ <PROGRAM> ::= {<STMT> SEMI} """
        while self.tokens.peek != TokCat.END:
            self.check_stmt()
            self.tokens.expect(TokCat.SEMI)

    def check_stmt(self):
        """ <STMT> ::= <INPUT_STMT> | <ASSIGN_STMT> | <DISPLAY_STMT> """
        start = self.tokens.expect(TokCat.INPUT, TokCat.ID, TokCat.DISPLAY,
                                  consume=False)
        if start == TokCat.INPUT:
            self.check_input()
        elif start == TokCat.ID:
            self.check_assignment()
        else:
            self.check_display()

    def check_input(self):
        """   <INPUT_STMT> ::= INPUT ID {COMMA ID} """
        self.tokens.expect(TokCat.INPUT)
        self.tokens.expect(TokCat.ID)
        while self.tokens.peek == TokCat.COMMA:
            self.tokens.get()
            self.tokens.expect(TokCat.ID)

    def check_display(self):
        """ <DiSPLAY_STMT> ::= DISPLAY <DISPLAY_ARG> {COMMA <DISPLAY_ARG>} """
        self.tokens.expect(TokCat.DISPLAY)
        self.check_display_arg()
        while self.tokens.peek == TokCat.COMMA:
            self.tokens.get()
            self.check_display_arg()

    def check_display_arg(self):
        """ <DISPLAY_ARG> ::= STRING | NL | <E> """
        if self.tokens.peek == TokCat.STRING or self.tokens.peek == TokCat.NL:
            self.tokens.get()
        else:
            self.check_expr()
    

    def check_assignment(self):
        """  <ASSIGN_STMT> ::= ID ASSIGN <E> """
        self.tokens.expect(TokCat.ID)
        self.tokens.expect(TokCat.ASSIGN)
        self.check_expr()

    def check_expr(self):
        """ <E> ::= <E1> {ADDOP <E1>} """
        self.check_expr1()
        while self.tokens.peek == TokCat.ADDOP:
            self.tokens.get()
            self.check_expr1()

    def check_expr1(self):
        """ <E1> ::= <E2> {MULOP <E2>} """
        self.check_expr2()
        while self.tokens.peek == TokCat.MULOP:
            self.tokens.get()
            self.check_expr2()

    def check_expr2(self):
        """ <E2> ::= {ADDOP} <E3> """
        while self.tokens.peek == TokCat.ADDOP:
            self.tokens.get()
        self.check_expr3()

    def check_expr3(self):
        """ <E3> ::= <E4> EXPOP <E3> | <E4> """
        self.check_expr4()
        if self.tokens.peek == TokCat.EXPOP:
            self.tokens.get()
            self.check_expr3()

    def check_expr4(self):
        """ <E4> ::= NUMBER | LPAREN <E> RPAREN | ID 
                   | ID LPAREN [<E> {COMMA <E>}] RPAREN
        """
        start = self.tokens.expect(TokCat.NUMBER, TokCat.LPAREN, TokCat.ID)
        if start == TokCat.LPAREN:
            self.check_expr()
            self.tokens.expect(TokCat.RPAREN)
        elif start == TokCat.ID:
            if self.tokens.peek == TokCat.LPAREN:
                self.tokens.get()
                self.check_expr()
                while self.tokens.peek == TokCat.COMMA:
                    self.tokens.get()
                    self.check_expr()
                self.tokens.expect(TokCat.RPAREN)

def main():
    fname = input("file: ")
    with open(fname) as infile:
        program = infile.read()
    checker = JelleChecker(program)
    checker.check_program()
    print("Looks Good!")


if __name__ == "__main__":
    main()
