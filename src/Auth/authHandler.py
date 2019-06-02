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
import os


class Handler:
    def __init__(self, system, filename="data/db/auth.db"):
        self.system = system
        self.filename = filename
        self.connection = None
        self.cursor = None  # To stop spewing errors at me.

    def open(self):
        if not os.path.exists('data/db'):
            os.makedirs('data/db')  # todo make custom for filename could change.
        self.connection = sqlite3.connect(self.filename)
        self.cursor = self.connection.cursor()
        create = "CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, " \
                 "username text NOT NULL, password text NOT NULL, perm integer NOT NULL)"  # todo multiple permissions.
        self.cursor.execute(create)
        self.system.logger.debug("Table users created in db, Creating default values.", caller="AuthHandler")

        sql = 'INSERT OR IGNORE INTO users(id,username,password,perm) values(?,?,?,?)'
        self.cursor.execute(sql, (1, "Username123", "Password123", 2))
        self.connection.commit()

    def verify(self, username, password):
        if self.cursor is None:
            self.system.logger.error("AuthHandler used before opened.", caller="AuthHandler")
            return False
        self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))

        rows = self.cursor.fetchall()
        for row in rows:
            if row[1] == username and row[2] == password:
                self.system.login(username)
                return True
        return False
