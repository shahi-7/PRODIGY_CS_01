# Caesar Cipher Implementation (Simple)

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Check if it's a letter
            shift_base = 65 if char.isupper() else 97  # Handle uppercase and lowercase
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shifted_char
        else:
            result += char  # Leave non-alphabet characters unchanged
    return result

def main():
    # Input from the user
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (1-25): "))

    if choice == 'e':
        encrypted_message = caesar_cipher(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = caesar_cipher(message, -shift)  # Use negative shift for decryption
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice! Please enter 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
