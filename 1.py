def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char_code = ord(char)
            char_code = (char_code - ord('A' if is_upper else 'a') + shift) % 26
            char_code += ord('A' if is_upper else 'a')
            result += chr(char_code)
        else:
            result += char
    return result
plaintext = "Hello, World!"
shift_value = 3
encrypted_text = caesar_cipher(plaintext, shift_value)
print(f"Original Text: {plaintext}")
print(f"Encrypted Text: {encrypted_text}")
output
Original Text: Hello, World!
Encrypted Text: Khoor, Zruog!
