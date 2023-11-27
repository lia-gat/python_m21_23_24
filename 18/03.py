def encrypt_caesar(msg, shift):
    encrypted_msg = ''
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    shift = shift % len(alphabet)
    for letter in msg:
        if letter.lower() in alphabet:
            index = (alphabet.index(letter.lower()) + shift) % len(alphabet)
            if letter.islower():
                encrypted_msg += alphabet[index]
            else:
                encrypted_msg += alphabet[index].upper()
        else:
            encrypted_msg += letter
    return encrypted_msg

def decrypt_caesar(msg, shift):
    decrypt_msg = ''
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    shift = shift % len(alphabet)
    for letter in msg:
        if letter.lower() in alphabet:
            index = (alphabet.index(letter.lower()) - shift) % len(alphabet)
            if letter.islower():
                decrypt_msg += alphabet[index]
            else:
                decrypt_msg += alphabet[index].upper()
        else:
            decrypt_msg += letter
    return decrypt_msg

msg = "Да здравствует салат Цезарь!"
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted,
shift)
print(encrypted)
print(decrypted)

print('\n*******\n')

msg = "Да здравствует салат Цезарь!"
shift = 5
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted,
shift)
print(encrypted)
print(decrypted)