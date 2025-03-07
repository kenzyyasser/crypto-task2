import string
from collections import Counter

def decrypt(ciphertext, key_map):
    """Decrypts a monoalphabetic substitution cipher text using a given key map."""
    return ''.join(key_map.get(char, char) for char in ciphertext)

def frequency_analysis(ciphertext):
    """Performs frequency analysis on the encrypted text."""
    letter_counts = Counter(ciphertext)
    sorted_letters = [char for char, _ in letter_counts.most_common() if char in string.ascii_lowercase]
    return sorted_letters

def cryptanalysis_monoalphabetic(ciphertext):
    """Attempts to break a monoalphabetic cipher using frequency analysis."""
    english_frequency = "etaoinshrdlcumwfgypbvkjxqz"  # Standard letter frequency order
    cipher_frequency = frequency_analysis(ciphertext)
    
    key_map = {cipher: plain for cipher, plain in zip(cipher_frequency, english_frequency)}
    decrypted_text = decrypt(ciphertext, key_map)
    
    print("Most likely decryption:")
    print(decrypted_text)

if __name__ == "__main__":
    encrypted_message = input("Enter the encrypted message: ").lower()
    cryptanalysis_monoalphabetic(encrypted_message)
