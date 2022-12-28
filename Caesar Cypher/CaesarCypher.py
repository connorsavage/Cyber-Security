def caesar_cipher(text, key):
    # create a blank result string
    result = ""
    # loop through each character in the text
    for char in text:
        # if the character is a letter, shift it by the specified amount
        if char.isalpha():
            char_code = ord(char)
            char_code += key
            # if the character is now outside the range of uppercase or lowercase letters, wrap it around
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            else:
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            result += chr(char_code)
        # if the character is not a letter, add a random letter to the result
        else:
            result += chr(ord('a') + random.randint(0, 25))
    return result

# test the Caesar cipher
text = "hello"
key = 3
encrypted_text = caesar_cipher(text, key)
print(encrypted_text)  # prints "khoor" or some other string
decrypted_text = caesar_cipher(encrypted_text, -key)
print(decrypted_text)  # prints "hello" or some other string