import sqlite3
import os.path
from pathlib import Path


class DBclass():
    def __init__(self, db_file):
        self.db = self.connect(db_file)
        self.record =[]

    @staticmethod
    def connect(dbfile='vk_users.db'):
        p = Path('.')
        db_path = p.cwd() / dbfile
        create = not os.path.exists(db_path)
        db = sqlite3.connect(db_path)
        if create:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS vk_users (
                        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
                        name TEXT NOT NULL,
                        surname TEXT NOT NULL,
                        age INTEGER,
                        city TEXT,
                        city_id INTEGER,
                        interests INTEGER,
                        status INTEGER,
                        group_id INTEGER);
            """)
            db.commit()
        return db

    def add_contact(self, list_user):
        cur = self.db.cursor()
        for rec in list_user:
            cur.execute("""INSERT INTO vk_users (
                id, name, surname, age, city, city_id, interests, status, group_id)
                VALUES (?,?,?,?,?,?,?,?,?);
                """, rec)

        self.db.commit()

    def get_contact_by_id(self, vk_id):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM vk_users WHERE id = ?;", vk_id)
        self.record = cur.fetchone()

    def get_contact_by_status(self, status):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM vk_users WHERE status = ?;", status)
        self.record = cur.fetchone()

    def get_count_contacts(self):
        cur = self.db.cursor()
        cur.execute("SELECT COUNT(*) FROM vk_users;")
        return cur.fetchone()

    def del_contact(self, vk_id):
        cur = self.db.cursor()
        cur.execute("DELETE FROM vk_users WHERE id = ?", vk_id)
        self.db.commit()








