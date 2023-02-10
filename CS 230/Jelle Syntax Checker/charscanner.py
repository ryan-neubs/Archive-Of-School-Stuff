# charscanner.py

class CharScanner:
    """Wrapper around a character sequence to skip comments and provide
    single character lookahead buffer (peek).
    """

    def __init__(self, charseq):
        self._chars = iter(charseq)
        self.peek = "\n"  # fake 1st character
        self._linenum = 0 # will be incremented to 1 on get
        self._linepos = 1
        self.get()

    def position(self):
        """ return line number and position in line of current character """
        
        return self._linenum, self._linepos

    def get(self):
        """ return current character and advance to the next 
          When sequence is exahusted, peek is None
        """
        
        char = self.peek
        self._advance()

        # advance through any comment characters
        if self.peek == "#":
            while self.peek not in ["\n", None]:
                self._advance()

        return char

    def _advance(self):
        # advances 1 character in the stream

        # update location information
        if self.peek == "\n":
            self._linenum += 1
            self._linepos = 1
        else:
            self._linepos += 1

        # cache next character as the peek
        try:
            self.peek = next(self._chars)
        except StopIteration:
            self.peek = None



def main():
    fname = input("file: ")
    with open(fname) as infile:
        chars = infile.read()
    cscan = CharScanner(chars)
    while cscan.peek:
        print(f"{cscan.position()}: {cscan.get()}")

if __name__ == "__main__":
    main()
