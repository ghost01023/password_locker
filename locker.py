import json
import sys
import os
from cipher import encrypt, decrypt

ROOT = "C:\\Users\\Rosja Dostoyevsjky\\Desktop\\"
password_file = open(ROOT + "passwords.json", "r+")
pw = "JohnnyBeGood!"
password_database = json.loads(decrypt(str(password_file.read()), pw))
encrypted = ""
# print(encrypted)
for key, value in password_database.items():
    newString = '{"' + key + '":"' + value + '"}'
    # print(newString)
    encrypted += encrypt(newString, pw)

print("FINAL ENCRYPTED IS \n" + encrypted)
# password_file.seek(0)
# password_file.write(encrypted)
password_file.close()


def username_exists(root_dir, user):
    return os.path.isfile(root_dir + user)


if len(sys.argv) == 2 and sys.argv[1] == "-add":
    adding = True
    while adding:
        account_name = input("Enter the name of the new account: ")
        password = input("Enter the password for this account: ")
        if account_name in password_database:
            overwrite = input("Do you really want to overwrite the previous password\nassociated with this account?")
            if overwrite.lower() != "y":
                print("Exiting the Locker...")
                sys.exit()
        password_database[account_name] = password
        with open("C:\\Users\\Rosja Dostoyevsjky\\Desktop\\passwords.json", "w") as pw:
            pw.write(str(password_database).replace("'", '"'))
            print("Password added Successfully to the Locker")
            add_more = input("Do you want to add more passwords to the locker (Y/N): ")
            if add_more.lower() != "y":
                print("Exiting the Locker...")
                sys.exit()

elif len(sys.argv) == 2:
    username = sys.argv[1]
    print("Checking existence of " + username)
    # pyperclip.copy(password_database[username])
    # print("Password copied Successfully to Clipboard.")

elif len(sys.argv[0]) > 20:
    print("Please run the program from the Command Line.")

else:
    print("""Invalid number of arguments. Enter in this format:
    python [file name] [-add flag] || [account name]
    """)


# PASSWORD LOCKER USERNAME ENCRYPTION ALGORITHM


# print(code)
#

# f"and added by {LOW_RANGE} which gives the value as {((ord(char) + len(key)) % HIGH_RANGE) + LOW_RANGE} "
