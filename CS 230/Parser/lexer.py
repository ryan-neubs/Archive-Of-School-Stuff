# lexer.py
#  Lexical scanner for Jelle
# Lexical structure: program is sequence of tokens

"""
<tokens> ::= {space} {<token> {space}}
 <token> ::= ^ | '(' | ')' | ; | , | := | display | input | nl | <addop>
             | <mulop> | <id> | <number> | <string>
 <addop> ::= + | - 
 <mulop> ::= * | / | %
    <id> ::= <letter> {<letter> | <digit>}
   <number> ::= . <digit> {<digit>} | <digit> {<digit>} [. {<digit>}]
<string> ::= "{<char>}"

"""

import enum

from charscanner import CharScanner

class TokCat(enum.Enum):
    """ Token Categories
    The associated values are useful for error messages
    """
    ADDOP = "+ or -"
    MULOP = "*, /, or %"
    EXPOP = "^"
    LPAREN = "("
    RPAREN = ")"
    ASSIGN = ":="
    DISPLAY = "display"
    INPUT = "input"
    NL = "nl"
    ID = "identifier"
    NUMBER = "number"
    COMMA = ","
    SEMI = ";"
    STRING = "a string"
    END = "end of program" # sentinel token for end of file


class Token:

    def __init__(self, category, lexeme):
        self.cat = category
        self.lexeme = lexeme

    def __eq__(self, token_cat):
        # allows tests such as: if token == TokCat.ADDOP
        return self.cat == token_cat

    def __repr__(self):
        return(f"Token({self.cat.name}, '{self.lexeme}')")


class Lexer:
    """Produces a stream of tokens from a string and provides a single
    token buffer for lookahead (peek).
    """

    SINGLE_CHAR_TOKENS = {
        "+": TokCat.ADDOP, "-": TokCat.ADDOP, "*": TokCat.MULOP,
        "/": TokCat.MULOP, "%": TokCat.MULOP, "^": TokCat.EXPOP,
        ",": TokCat.COMMA, ";": TokCat.SEMI, "(": TokCat.LPAREN,
        ")": TokCat.RPAREN
        }

    def __init__(self, programString):
        self._chars = CharScanner(programString)
        self._skip_spaces()
        self.peek = None
        self.get()  # read first token

    def get(self):
        """ returns current token and advance to the next """
        token = self.peek
        self._parse_next_token()
        return token

    def position(self):
        """returns the start of the current token (line, position_in_line)"""
        return self._position

    def expect(self, *tokencats, consume=True):
        """return current token if it is in tokencats o/w raises an exception/
        Note: consume controls whether the stream is advanced or not.

        """
        if self.peek not in tokencats:
            expects = [cat.value for cat in tokencats]
            found = self.peek.lexeme
            if not found:
                found = "end of file"
            msg = f"Expected {expects}, but found {found} at {self.position()}"
            raise SyntaxError(msg)
        if consume:
            return self.get()
        else:
            return self.peek

    def _skip_spaces(self):
        while self._chars.peek and self._chars.peek.isspace():
            self._chars.get()

    def _parse_next_token(self):
        """ <tokens> ::= {space} {<token> {space}} 
        """
        # initial spaces skipped in __init__
        chars = self._chars
        # cache the starting position
        self._position = chars.position()
        if chars.peek is None:  # reached end of string
            self.peek = Token(TokCat.END, "")
        else:
            self.peek = self._parse_token()
            self._skip_spaces()

    def _parse_token(self):
        """<token> ::= ^ | '(' | ')' | ; | , | := | display | input | nl |
                       <addop> | <mulop> | <id> | <number> | <string>

        """

        ch = self._chars.peek
        if ch in self.SINGLE_CHAR_TOKENS:
            return Token(self.SINGLE_CHAR_TOKENS[ch], self._chars.get())
        if ch == ":":
            return self._parse_assignop()
        if ch.isalpha():
            return self._parse_keyword_or_id()
        if ch == "." or ch.isdigit():
            return self._parse_number()
        if ch == '"':
            return self._parse_string()
        self._raise_token_error()

    def _parse_assignop(self):
        self._chars.get()  # consume the ':'
        if self._chars.peek != "=":
            self._raise_token_error()
        self._chars.get()
        return Token(TokCat.ASSIGN, ":=")

    def _parse_keyword_or_id(self):
        """<id> ::= <letter> {<letter> | <digit>}"""

        lexeme = self._chars.get()
        while self._chars.peek and self._chars.peek.isalnum():
            lexeme += self._chars.get()

        if lexeme == "display":
            return Token(TokCat.DISPLAY, lexeme)
        if lexeme == "input":
            return Token(TokCat.INPUT, lexeme)
        if lexeme == "nl":
            return Token(TokCat.NL, lexeme)
        return Token(TokCat.ID, lexeme)

    def _parse_number(self):
        """ <number> ::= . <digit> {<digit>}
                         | <digit> {<digit>} [. {<digit>}] """

        chars = self._chars
        lexeme = chars.get()
        if lexeme == ".":
            if not chars.peek.isdigit():
                self._raise_token_error()
            lexeme += chars.get()
            while chars.peek.isdigit():
                lexeme += chars.get()
        else:
            while chars.peek.isdigit():
                lexeme += chars.get()
            if chars.peek == ".":
                lexeme += chars.get()
            while chars.peek.isdigit():
                lexeme += chars.get()
        return Token(TokCat.NUMBER, lexeme)

    def _parse_string(self):
        """ <string> ::= "{<char>}" """

        chars = self._chars
        lexeme = chars.get()
        while chars.peek != '"':
            lexeme += chars.get()
        lexeme += chars.get()
        return Token(TokCat.STRING, lexeme)

    def _raise_token_error(self):
        raise SyntaxError(f"Unrecognized token at {self._position}")


def main():
    fname = input("file: ")
    with open(fname) as infile:
        chars = infile.read()
    tokens = Lexer(chars)
    while tokens.peek != TokCat.END:
        print(f"{tokens.position()}: {tokens.get()}")

        
if __name__ == "__main__":
    main()
