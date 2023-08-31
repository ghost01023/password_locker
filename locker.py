import json
import sys
import pyperclip
import os

# for i in range(32, 127):
#     print(chr(i))
LOW_RANGE = 32
HIGH_RANGE = 126
# ROOT = "C:\\Users\\Rosja Dostoyevsjky\\Desktop\\electrical homework\\"
# password_file = open(ROOT + "passwords.json")
# password_database = json.load(password_file)
#
#
# def username_exists(root_dir, user):
#     return os.path.isfile(root_dir + user)
#
#
# if len(sys.argv) == 2 and sys.argv[1] == "-add":
#     adding = True
#     while adding:
#         account_name = input("Enter the name of the new account: ")
#         password = input("Enter the password for this account: ")
#         if account_name in password_database:
#             overwrite = input("Do you really want to overwrite the previous password\nassociated with this account?")
#             if overwrite.lower() != "y":
#                 print("Exiting the Locker...")
#                 sys.exit()
#         password_database[account_name] = password
#         with open("C:\\Users\\Rosja Dostoyevsjky\\Desktop\\passwords.json", "w") as pw:
#             pw.write(str(password_database).replace("'", '"'))
#             print("Password added Successfully to the Locker")
#             add_more = input("Do you want to add more passwords to the locker (Y/N): ")
#             if add_more.lower() != "y":
#                 print("Exiting the Locker...")
#                 sys.exit()
#
# elif len(sys.argv) == 2:
#     username = sys.argv[1]
#     print("Checking existence of " + username)
#     # pyperclip.copy(password_database[username])
#     # print("Password copied Successfully to Clipboard.")
#
# elif len(sys.argv[0]) > 20:
#     print("Please run the program from the Command Line.")
#
# else:
#     print("""Invalid number of arguments. Enter in this format:
#     python [file name] [-add flag] || [account name]
#     """)


# PASSWORD LOCKER USERNAME ENCRYPTION ALGORITHM

# VIGNERE CIPHER

def convert_to_vignere_cipher(text, key):
    encrypted_string = ""
    # offset = len(key)
    for i in range(len(text)):
        char = text[i]
        # print(f"""
        # {char} is at {ord(char)}. It will be added to {key[i % len(key)]},
        # which is at {ord(key[i % len(key)])} and will give us ASCII number: {(ord(char) + ord(key[i % len(key)]))}
        # and value of {chr(ord(char) + ord(key[i % len(key)]))}
        # """)
        encrypted_char = chr((ord(char) + ord(key[i % len(key)])) % HIGH_RANGE)
        if ord(encrypted_char) < LOW_RANGE:
            encrypted_char = chr(HIGH_RANGE - ord(encrypted_char))
        # print(encrypted_char)
        encrypted_string += encrypted_char
    return encrypted_string

# print(key[i % len(key)] + " to " + str(ord(key[i % len(key)])))
# print(f"{char} is at ASCII value of {ord(char)} and added by {len(key) + LOW_RANGE}, "
#       f"its modulo by {HIGH_RANGE} is {((ord(char) + len(key) + LOW_RANGE) % HIGH_RANGE)} "
#       f"and the character at that position is {encrypted_char}")
# print(f"{char} changed to {encrypted_char}")
# print(encrypted_char)


def convert_vignere_cipher_to_plain_text(text, key):
    decrypted_string = ""
    for i in range(len(text)):
        char = text[i]
        decrypted_char = chr((ord(char) - ord(key[i % len(key)])) % HIGH_RANGE)
        if ord(decrypted_char) < LOW_RANGE:
            decrypted_char = chr((ord(decrypted_char) + HIGH_RANGE))
        print(char + " has been decrypted to ASCII code number " + str(ord(decrypted_char)) + " of value " + decrypted_char)
        decrypted_string += decrypted_char
    return decrypted_string


code = convert_to_vignere_cipher("01234,#ENCRYPT-SPACES         !", "aaaaa")
print(code)

print(convert_vignere_cipher_to_plain_text(code, "generalkey"))

# f"and added by {LOW_RANGE} which gives the value as {((ord(char) + len(key)) % HIGH_RANGE) + LOW_RANGE} "
