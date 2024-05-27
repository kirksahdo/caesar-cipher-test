def caesar_cipher_decrypt(ciphertext, shift):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_text = []
    for letter in ciphertext:
        pos = letters.find(letter)
        new_pos = (pos - shift) % 26
        decrypted_text.append(letters[new_pos])
    return "".join(decrypted_text)


def process_cases(num_cases, cases):
    results = []
    for i in range(num_cases):
        ciphertext, shift = cases[i]
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        results.append(decrypted_text)
    return results
