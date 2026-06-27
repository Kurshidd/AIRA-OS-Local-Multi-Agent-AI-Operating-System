import sqlite3
import threading


class Memory:
    def __init__(self, db_path="memory/chat_history.db"):

        self.lock = threading.Lock()

        self.conn = sqlite3.connect(
            db_path,
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            message TEXT NOT NULL
        )
        """)

        self.conn.commit()

    def save_message(self, role, message):

        with self.lock:

            self.cursor.execute(
                """
                INSERT INTO conversations(role, message)
                VALUES (?, ?)
                """,
                (role, message)
            )

            self.conn.commit()

    def get_recent_messages(self, limit=10):

        with self.lock:

            self.cursor.execute(
                """
                SELECT role, message
                FROM conversations
                ORDER BY id DESC
                LIMIT ?
                """,
                (limit,)
            )

            rows = self.cursor.fetchall()

        rows.reverse()

        return rows

    def clear(self):

        with self.lock:

            self.cursor.execute(
                "DELETE FROM conversations"
            )

            self.conn.commit()

    def close(self):

        with self.lock:

            self.conn.close()