import string
from collections import Counter

def generate_playfair_matrix(keyword):
    """Generates a 5x5 Playfair matrix from the keyword."""
    keyword = keyword.lower().replace("j", "i")
    seen = set()
    matrix = []
    for char in keyword + string.ascii_lowercase:
        if char not in seen and char in string.ascii_lowercase and char != 'j':
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    """Finds the row and column of a character in the Playfair matrix."""
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)
    return None, None

def encrypt_playfair(plaintext, matrix):
    """Encrypts text using the Playfair cipher rules."""
    plaintext = plaintext.lower().replace("j", "i").replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += 'x'  # Padding if odd length
    ciphertext = ""
    
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        if row1 == row2:  # Same row
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle swap
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    
    return ciphertext

def decrypt_playfair(ciphertext, matrix):
    """Decrypts text using the Playfair cipher rules."""
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        if row1 == row2:  # Same row
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle swap
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    
    return plaintext

if __name__ == "__main__":
    keyword = input("Enter the keyword for Playfair cipher: ")
    matrix = generate_playfair_matrix(keyword)
    
    print("Playfair 5x5 Matrix:")
    for row in matrix:
        print(" ".join(row))
    
    choice = input("Encrypt or Decrypt (e/d)? ").lower()
    text = input("Enter the text: ")
    
    if choice == "e":
        print("Encrypted Text:", encrypt_playfair(text, matrix))
    elif choice == "d":
        print("Decrypted Text:", decrypt_playfair(text, matrix))
