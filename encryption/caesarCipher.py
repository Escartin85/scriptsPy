# Caesar Cipher

# the string to be encrypted/decrypted
message = 'This is my secret message.'

# the encryption/descryption key:
key = 13

# whether the program encrypts or decrypts:
# set to either 'encrypt' or 'decrypt'
mode = 'encrypt'

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# store the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
    # Only symbols in the SYMBOLS string can be encrypted/decrypted.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # perform encryption/decryption:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key
        
        # handle wraparound, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        
        translated = translated + SYMBOLS[translatedIndex]
    else:
        # append the symbol without encrypting/decrypting:
        translated = translated + symbol

# output the translated string:
print(translated)