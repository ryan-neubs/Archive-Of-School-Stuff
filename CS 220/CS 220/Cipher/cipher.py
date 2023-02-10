# cipher.py

import string
from random import shuffle
import random

class Cipher:
    
    LETTERS = [ch for ch in string.ascii_uppercase]

    def __init__(self, LETTERS):
            
        ''' Creates a new random cipher
        note: a cipher is a mapping of uppercase characters into upercase
        characters where each character maps to a unique character
        and no character maps to itself
        '''
        self.LETTERS = LETTERS
        self.RandLetters = LETTERS[:]
        self.CiphDict = {}
        self.TextCipher = ''
        self.DecodedText = ''
        self.DecodedDict = {}
        for i in range(len(self.LETTERS)):
            while self.LETTERS[i] == self.RandLetters[i]:
                shuffle(self.RandLetters)
    
    

    def _no_matches(seq1, seq2):
    
        '''returns True if no position in sequences match
        pre: seq1 and seq2 are sequences of some length
        post: returns True if there is no i such that seq1[i] == seq2[i]
        '''
        for i in range(len(seq1)):
            if seq1[i] === seq2[i]:
                return False
        return True

    def encode(self, plaintext):

        '''returns an encoded version of plaintext
        note: uppercase letters are encoded, all others remain the same
        '''
                       

    def decode(self, ciphertext):

        '''returns a decoded version of ciphertext
        note: uppercase letters are decoded, all others remain the same
        '''
