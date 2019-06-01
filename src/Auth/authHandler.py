"""
authHandler.py
class Handler(string fileName):
- func wipe(bool) (bool- wipe backups?)
- func getUsers()
- func addUser(User)
- func remUser(User)
- func updateUser(User)
- func findUser(string) (string- name of user)

authHandler handles ALL the data stored in auth.db
and should be the ONLY one to use it.
"""
import sqlite3


class Handler:
    def __init__(self, filename="data/db/auth.db"):
        self.filename = filename
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()
