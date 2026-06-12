import hashlib
import sqlite3


def check_login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)

    result = cursor.fetchall()
    if len(result) > 0:
        return True
    else:
        return False


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


API_KEY = "MY_SUPER_SECRET_API_KEY_12345"

if check_login("admin", "1234"):
    print("Welcome admin!")
