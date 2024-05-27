import unittest
from caesar_cipher import caesar_cipher_decrypt


class CaesarCipherTest(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(caesar_cipher_decrypt("VQREQFGT", 2), "TOPCODER")

    def test_case_2(self):
        self.assertEqual(
            caesar_cipher_decrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 10),
            "QRSTUVWXYZABCDEFGHIJKLMNOP",
        )

    def test_case_3(self):
        self.assertEqual(caesar_cipher_decrypt("TOPCODER", 0), "TOPCODER")

    def test_case_4(self):
        self.assertEqual(caesar_cipher_decrypt("ZWBGLZ", 25), "AXCHMA")

    def test_case_5(self):
        self.assertEqual(caesar_cipher_decrypt("DBNPCBQ", 1), "CAMOBAP")

    def test_case_6(self):
        self.assertEqual(caesar_cipher_decrypt("LIPPSASVPH", 4), "HELLOWORLD")

    def test_no_displacement(self):
        self.assertEqual(caesar_cipher_decrypt("ABCDE", 0), "ABCDE")

    def test_maximum_displacement(self):
        self.assertEqual(caesar_cipher_decrypt("ABCDE", 25), "ZABCD")

    def test_inverse_displacement(self):
        self.assertEqual(caesar_cipher_decrypt("CDEFG", 2), "ABCDE")

    def test_empty_string(self):
        self.assertEqual(caesar_cipher_decrypt("", 5), "")

    def test_single_character(self):
        self.assertEqual(caesar_cipher_decrypt("A", 1), "Z")

    def test_all_alphabet_characters(self):
        self.assertEqual(
            caesar_cipher_decrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 26),
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        )

    def test_large_shift(self):
        self.assertEqual(caesar_cipher_decrypt("HELLO", 52), "HELLO")


if __name__ == "__main__":
    unittest.main()
