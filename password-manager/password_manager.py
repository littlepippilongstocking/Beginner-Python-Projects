"""
Dilyana Koleva, July 2022
Python Projects for Beginners - Password Manager
"""

from cryptography.fernet import Fernet

"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
"""


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


#password = input("What is the master password?")
#key = load_key() + password.encode()
key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split(" | ")
            print("User:", user, "| Password:", fer.decrypt(pwd.encode()).decode())


def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    with open("passwords.txt", 'a') as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    print("Welcome to Password Manager 3.0. Your best friend for managing your passwords.")
    mode = input("Would you like to add a new password or view existing ones (view or add)? \n"
                 "To quit, please, press q.").lower()
    if mode == "q":
        print("Thank you for using Password Manager 3.0. Goodbye!")
        quit()

    if mode == "view":
        print("You have selected option View to see all existing passwords and usernames.")
        view()
    elif mode == "add":
        print("You have selected option Add. Please, proceed to adding a new password and username.")
        add()
    else:
        print("The selected mode is invalid.")
        continue
