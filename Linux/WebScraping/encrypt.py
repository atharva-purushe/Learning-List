from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

with open('secret.key', 'rb') as key_file:
    key = key_file.read()
fernet = Fernet(key)

with open('Death_Claims.csv', 'rb') as file:
    original = file.read()
encrypted = fernet.encrypt(original)

with open('Death_Claims_encrypted.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

print("✅ File encrypted successfully as 'Death_Claims_encrypted.csv'")
