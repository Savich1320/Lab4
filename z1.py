import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_unique_passwords(n, length):
    passwords = set()
    while len(passwords) < n:
        password = generate_password(length)
        passwords.add(password)
    return passwords

N = int(input("Введите количество паролей: "))
K = int(input("Введите длину пароля: "))

unique_passwords = generate_unique_passwords(N, K)
for password in unique_passwords:
    print(password)
