import string

def decrypt(ciphertext, key_map):
    """Decrypts a monoalphabetic substitution cipher text using a given key map."""
    return ''.join(key_map.get(char, char) for char in ciphertext)

def generate_permutations(sequence, limit=10):
    """Generates a limited number of permutations of a given sequence manually."""
    count = [0]  # Using a list to allow modification inside the nested function

    def permute(seq, step=0):
        if count[0] >= limit:
            return  # Stop generating permutations after the limit

        if step == len(seq):
            yield "".join(seq)
            count[0] += 1
            return

        for i in range(step, len(seq)):
            seq[step], seq[i] = seq[i], seq[step]
            yield from permute(seq, step + 1)
            seq[step], seq[i] = seq[i], seq[step]

    yield from permute(list(sequence))

def brute_force_monoalphabetic(ciphertext, max_attempts=10):
    """Attempts to break a monoalphabetic substitution cipher using brute force."""
    alphabet = list(string.ascii_lowercase)

    for index, key in enumerate(generate_permutations(alphabet, limit=max_attempts)):
        key_map = {cipher: plain for cipher, plain in zip(alphabet, key)}
        decrypted_text = decrypt(ciphertext, key_map)
        print(f"Attempt {index + 1}: {decrypted_text}")  # Output decrypted texts

if __name__ == "__main__":
    encrypted_message = input("Enter the encrypted message: ").lower()
    brute_force_monoalphabetic(encrypted_message)
