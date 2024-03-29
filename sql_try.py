from mysql import connector
from credentials import *

conn = connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="people_data"
)

cursor = conn.cursor()
query = f"USE people_data;"
cursor.execute(query)
add_user = f"INSERT INTO profile (`email`, `username`, `password`) VALUES "

for i in range(1, 500):
    username = usernames[i]
    password = passwords[i]
    user_email = emails[i]
    user_details = {
        "email": user_email,
        "username": username,
        "password": password
    }
    formatted_keys = []
    formatted_values = []
    for key, value in user_details.items():
        formatted_keys.append('`' + key + "`")
        formatted_values.append('"' + value + '"')
    sql_keys = ', '.join(formatted_keys)
    sql_values = ', '.join(formatted_values)
    new_user = "(" + sql_values + ")" + (", " if i < 499 else ";")
    print(new_user)
    add_user += new_user
print(len(add_user))
cursor.execute(add_user)
cursor.execute("SELECT * FROM profile;")
results = cursor.fetchall()
# for count, row in enumerate(results):
#     print(row)
#     print(count)

cursor.close()
print("Closed cursor")
conn.close()
print("Closed connection")
