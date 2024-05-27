import unittest

class CaesarCipherTest(unittest.TestCase):

    def test_case_1(self):
        pass


def caesar_cipher(N, text):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypt_text = [(letters[(letters.find(letter) - N) % 26] ) for letter in text]

    return "".join(encrypt_text)



print(caesar_cipher(25, "ZWBGLZ"))