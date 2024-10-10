'''
Sapendo che la chiave di cifra è: XXXXIsASecretKey

(non conoscete i primi 4 caratteri della chiave)

e che il messaggio cifrato è: OgJuOYJZT0FDb47DBOkNgA==

NB: la parte ignota delle chiave contiene esclusivamente maiuscole e minuscole

Trovare la decodifica del messaggio.
'''
import base64
import itertools
import string

def encrypt(plain_text):
    encrypted_bytes = plain_text.encode("utf-8")
    encrypted_text = base64.b64encode(encrypted_bytes)
    return encrypted_text.decode("utf-8")

def decrypt(encrypted_text):
    encrypted_bytes = encrypted_text.encode("utf-8")
    decrypted_bytes = base64.b64decode(encrypted_bytes)
    return decrypted_bytes.decode("utf-8")

# Known part of the secret key
known_key = "IsASecretKey"

# Ciphertext
ciphertext = "OgJuOYJZT0FDb47DBOkNgA=="

# Brute-force the first 4 characters of the secret key
for attempt in itertools.product(string.ascii_letters, repeat=4):
    key = "".join(attempt) + known_key
    try:
        # Attempt to decode the ciphertext with the current key
        plaintext = base64.b64decode(ciphertext).decode("utf-8")
        print("Key used:", key)
        print(f"Decoded message: {plaintext}")
        break
    except ValueError:
        # If decoding fails, try the next key
        continue

# Example usage:

plain_text = "Hello, World!"
encrypted_text = encrypt(plain_text)
decrypted_text = decrypt(encrypted_text)

print("Plain Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)