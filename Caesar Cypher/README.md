# Purpose
In this function, the shift value (called key) is used to shift each letter in the text by a certain amount. Non-letter characters are replaced with random letters, which makes the encrypted text more difficult to decrypt without knowing the original key.

To decrypt the text, the function is called again with the encrypted text and the negative of the key value. This will shift the characters in the opposite direction, effectively undoing the original encryption. 
