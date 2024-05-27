def caesar_cipher_decrypt(ciphertext, shift):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_text = []
    for letter in ciphertext:
        pos = letters.find(letter)
        new_pos = (pos - shift) % 26
        decrypted_text.append(letters[new_pos])
    return "".join(decrypted_text)


def process_cases(cases):
    results = []
    for case in cases:
        ciphertext, shift = case
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        results.append(decrypted_text)
    return results


N = int(input())
cases = []

for _ in range(N):
    ciphertext = input().strip()
    shift = int(input().strip())
    cases.append((ciphertext, shift))

results = process_cases(cases)

for result in results:
    print(result)
