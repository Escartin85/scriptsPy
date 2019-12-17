# Reverse Cipher

message = 'Three can keep a secret , if two of them are dead.'
encrypt_msg = ''

count = len(message) - 1
while count >= 0:
    encrypt_msg = encrypt_msg + message[count]
    count = count - 1

print(encrypt_msg)