import unittest


class CaesarCipherTest(unittest.TestCase):

    def test_cases(self):
        test_cases = read_test_cases()
        for text, N, expected in test_cases:
            with self.subTest():
                self.assertEqual(caesar_cipher(text, N), expected)


def caesar_cipher(text, N):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypt_text = [(letters[(letters.find(letter) - N) % 26]) for letter in text]
    return "".join(encrypt_text)


def read_test_cases():
    num_cases = int(input("Digite o número de casos de teste: "))
    test_cases = []
    for _ in range(num_cases):
        text = input("Digite o texto codificado: ")
        N = int(input("Digite o número de deslocamentos: "))
        expected = input("Digite o texto esperado: ")
        test_cases.append((text, N, expected))
    return test_cases


if __name__ == '__main__':
    unittest.main()
