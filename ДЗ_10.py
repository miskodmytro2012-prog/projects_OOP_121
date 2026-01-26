import sqlite3

conn = sqlite3.connect("FruitBasket.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Fruits (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Назва_фрукта TEXT,
    Колір TEXT
)
""")

cursor.execute("DELETE FROM Fruits")

cursor.execute("INSERT INTO Fruits (Назва_фрукта, Колір) VALUES ('Яблуко', 'Червоне')")
cursor.execute("INSERT INTO Fruits (Назва_фрукта, Колір) VALUES ('Банан', 'Жовтий')")
cursor.execute("INSERT INTO Fruits (Назва_фрукта, Колір) VALUES ('Апельсин', 'Помаранчевий')")

cursor.execute("UPDATE Fruits SET Колір = 'Зелене' WHERE Назва_фрукта = 'Яблуко'")

cursor.execute("SELECT * FROM Fruits WHERE Колір = 'Жовтий'")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Fruits")
print(cursor.fetchall())

conn.commit()
conn.close()