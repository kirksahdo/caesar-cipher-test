from caesar_cipher import process_cases

if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().strip().split("\n")

    N = int(data[0])
    cases = []

    for i in range(1, len(data), 2):
        ciphertext = data[i].strip()
        shift = int(data[i + 1].strip())
        cases.append((ciphertext, shift))

    results = process_cases(N, cases)

    for result in results:
        print(result)
