"""
=========================================================
QUANT ULTRA
Database Manager
=========================================================
"""

import sqlite3


class Database:

    def __init__(self, db_path="quant_ultra.db"):

        self.conn = sqlite3.connect(db_path)

        self.cursor = self.conn.cursor()

        self.initialize()

    # -------------------------------------------------

    def initialize(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS trades(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            symbol TEXT,

            side TEXT,

            entry REAL,

            exit REAL,

            quantity INTEGER,

            pnl REAL,

            status TEXT,

            created_at TEXT

        )

        """)

        self.conn.commit()

    # -------------------------------------------------

    def save_trade(self, trade):

        self.cursor.execute("""

        INSERT INTO trades(

            symbol,

            side,

            entry,

            exit,

            quantity,

            pnl,

            status,

            created_at

        )

        VALUES(?,?,?,?,?,?,?,?)

        """,

        (

            trade["symbol"],

            trade["side"],

            trade["entry"],

            trade.get("exit"),

            trade["quantity"],

            trade.get("pnl",0),

            trade["status"],

            trade["created_at"],

        )

        )

        self.conn.commit()

    # -------------------------------------------------

    def get_trades(self):

        return self.cursor.execute(

            "SELECT * FROM trades"

        ).fetchall()

    # -------------------------------------------------

    def close(self):

        self.conn.close()


if __name__ == "__main__":

    db = Database()

    print(db.get_trades())