import sqlite3
class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.c = self.con.cursor()
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS products (
                pid INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL,
                alert_quantity INTEGER NOT NULL,
                last_entry_date TEXT NOT NULL,
                last_exit_date TEXT NOT NULL,
                image VARCHAR
            )
        """)
        self.con.commit()

    def insert(self, name, description, price, quantity, alert_quantity, last_entry_date, last_exit_date, image=None):
        sql = """
            INSERT INTO products VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.c.execute(sql, (name, description, price, quantity, alert_quantity, last_entry_date, last_exit_date, image))
        self.con.commit()

    def fetch_records(self):
        self.c.execute("SELECT * FROM products")
        data = self.c.fetchall()
        return data

    def update_recordS(self, name, description, price, quantity, alert_quantity, last_entry_date, last_exit_date,image, pid):
        sql = """
            UPDATE products SET name=?, description=?, price=?, quantity=?, alert_quantity=?, last_entry_date=?, last_exit_date=?, image=? WHERE pid=?
        """
        self.c.execute(sql, (name, description, price, quantity, alert_quantity, last_entry_date, last_exit_date, image, pid))
        self.con.commit()

    def remove_record(self, pid):
        sql = "DELETE FROM products WHERE pid=?"
        self.c.execute(sql, (pid,))
        self.con.commit()
