''' Test Module '''
import unittest
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
#from machinetranslation import translator
from machinetranslation.translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    ''' Test Class for English to French '''
    def test1(self):
        ''' Test function for English to French '''
        self.assertEqual(english_to_french("Hi, it's Gautam, what's your name?"),
        "Salut, c'est Gautam, quel est votre nom?")
        self.assertNotEqual(english_to_french("How is your day so far?"),
        "Salut, c'est Gautam, quel est votre nom?")

class TestFrenchToEnglish(unittest.TestCase):
    ''' Test Class for French to English '''
    def test1(self):
        ''' Test Function for French to English '''
        self.assertEqual(french_to_english("Salut, c'est Gautam, quel est votre nom?"),
        "Hi, it's Gautam, what's your name?")
        self.assertNotEqual(french_to_english("Comment votre journée est-elle si loin?"),
        "Hi, it's Gautam, what's your name?")

unittest.main()
