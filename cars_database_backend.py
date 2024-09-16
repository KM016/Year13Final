import sqlite3

def connect():
    conn = sqlite3.connect("cars.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS car(id INTEGER PRIMARY KEY, make text, model text, year integer, price integer, milage integer, fuel text, rentprice integer, numberplate integer, owners integer, rented integer)")
    conn.commit()
    conn.close()

def insert(make, model, year, price, milage, fuel, rentprice, numberplate, owners, rented):
    conn = sqlite3.connect("cars.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO car VALUES(NULL,?,?,?,?,?,?,?,?,?,?)",(make, model, year, price, milage, fuel, rentprice, numberplate, owners, rented))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("cars.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM car")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(make="", model = "", year = "", price = "", milage = "", fuel = "", rentprice = "", numberplate = "", owners = "", rented = ""):
    conn = sqlite3.connect("cars.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM car WHERE make=? or model = ? or year = ? or price = ? or milage = ? or fuel = ? or rentprice = ? or numberplate = ? or owners = ? or rented = ?",(make, model, year, price, milage, fuel, rentprice, numberplate, owners, rented))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("cars.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM car WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update(id,make, model, year, price, milage, fuel, rentprice, numberplate, owners, rented):
    conn = sqlite3.connect("cars.db")
    cur = conn.cursor()
    cur.execute("UPDATE car SET make=?, model = ?, year = ?, price = ?, milage = ? , fuel = ? ,  rentprice = ? ,  numberplate = ? , owners = ?, rented = ?  WHERE id = ?",(make, model, year, price, milage, fuel, rentprice, numberplate, owners, rented, id))
    conn.commit()
    conn.close()

connect()

