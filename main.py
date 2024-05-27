import unittest


class CaesarCipherTest(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(caesar_cipher('VQREQFGT', 2), 'TOPCODER')

    def test_case_2(self):
        self.assertEqual(caesar_cipher('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 10), 'QRSTUVWXYZABCDEFGHIJKLMNOP')

    def test_case_3(self):
        self.assertEqual(caesar_cipher('TOPCODER', 0), 'TOPCODER')

    def test_case_4(self):
        self.assertEqual(caesar_cipher('ZWBGLZ', 25), 'AXCHMA')

    def test_case_5(self):
        self.assertEqual(caesar_cipher('DBNPCBQ', 1), 'CAMOBAP')

    def test_case_6(self):
        self.assertEqual(caesar_cipher('LIPPSASVPH', 4), 'HELLOWORLD')

    def no_displacement_test(self):
        self.assertEqual(caesar_cipher('ABCDE', 0), 'ABCDE')

    def maximum_displacement_test(self):
        self.assertEqual(caesar_cipher('ABCDE', 25), 'ZABCD')

    def inverse_displacement_test(self):
        self.assertEqual(caesar_cipher('CDEFG', 2), 'ABCDE')

    def test_empty_string(self):
        self.assertEqual(caesar_cipher('', 5), '')

    def test_single_character(self):
        self.assertEqual(caesar_cipher('A', 1), 'Z')

    def test_all_alphabet_characters(self):
        self.assertEqual(caesar_cipher('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 26), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def test_large_shift(self):
        self.assertEqual(caesar_cipher('HELLO', 52), 'HELLO')

    def test_negative_shift(self):
        with self.assertRaises(ValueError):
            caesar_cipher('HELLO', -1)

    def test_non_alphabet_character(self):
        with self.assertRaises(ValueError):
            caesar_cipher('HELLO1', 1)

    def test_lower_case_character(self):
        with self.assertRaises(ValueError):
            caesar_cipher('Hello', 1)


def caesar_cipher(N, text):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypt_text = [(letters[(letters.find(letter) - N) % 26]) for letter in text]

    return "".join(encrypt_text)
