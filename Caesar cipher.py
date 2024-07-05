def caesar_cipher(text, shift, mode):
    result = ""

    # traverse the text
    for i in range(len(text)):
        char = text[i]

        # Encrypting/Decrypting uppercase characters
        if char.isupper():
            if mode == 'encrypt':
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift - 65) % 26 + 65)

        # Encrypting/Decrypting lowercase characters
        elif char.islower():
            if mode == 'encrypt':
                result += chr((ord(char) + shift - 97) % 26 + 97)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # Non-alphabetic characters remain unchanged
            result += char

    return result

# Get user input
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Choose mode ('encrypt' or 'decrypt'): ").lower()

# Validate mode
if mode not in ['encrypt', 'decrypt']:
    print("Invalid mode! Please choose 'encrypt' or 'decrypt'.")
else:
    # Perform encryption/decryption
    result = caesar_cipher(message, shift, mode)
    print(f"Result: {result}")
