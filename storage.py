import sqlite3


class Storage:
    def __init__(self, db_name="journal.db"):
        self.conn = sqlite3.connect(db_name,check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                emotion TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def save_entry(self, text, emotion, created_at):
        command = "INSERT INTO entries (text, emotion, created_at) VALUES (?, ?, ?)"
        self.cursor.execute(command, (text, emotion, created_at))
        self.conn.commit()

    def fetch_all(self):
        self.cursor.execute("SELECT text, emotion, created_at FROM entries ORDER BY created_at ASC")
        return self.cursor.fetchall()

    def fetch_latest(self, limit=10):
        self.cursor.execute(
            "SELECT text, emotion, created_at FROM entries ORDER BY created_at DESC LIMIT ?",
            (limit,)
        )
        return self.cursor.fetchall()

    def fetch_by_emotion(self, emotion):
        self.cursor.execute(
            "SELECT text, emotion, created_at FROM entries WHERE emotion = ? ORDER BY created_at DESC",
            (emotion,)
        )
        return self.cursor.fetchall()

    def search_text(self, keyword):
        self.cursor.execute(
            "SELECT text, emotion, created_at FROM entries WHERE text LIKE ? ORDER BY created_at DESC",
            (f"%{keyword}%",)
        )
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
