def caesar_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
        else:
            result += char
    return result


print(caesar_cipher("Hello, World!", 3))  # prints: Khoor, Zruog!
