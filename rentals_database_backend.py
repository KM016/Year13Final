import sqlite3

def connect():
    conn = sqlite3.connect("rentals.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS rents(id INTEGER PRIMARY KEY, customerID integer, carID integer , rentdate text, rentlength integer)")
    conn.commit()
    conn.close()

def insert(customerID, carID , rentdate, rentlength):
    conn = sqlite3.connect("rentals.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO rents VALUES(NULL,?,?,?,?)",(customerID, carID , rentdate, rentlength))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("rentals.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM rents")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(customerID = "" , carID = "" , rentdate = "" , rentlength = ""):
    conn = sqlite3.connect("rentals.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM rents WHERE customerID = ? or  carID = ? or rentdate = ? or rentlength = ? ",(customerID, carID , rentdate, rentlength))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("rentals.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM rents WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update(id, customerID, carID , rentdate, rentlength):
    conn = sqlite3.connect("rentals.db")
    cur = conn.cursor()
    cur.execute("UPDATE rents SET customerID = ? , carID = ? , rentdate = ? , rentlength = ?  WHERE id = ?",(customerID, carID , rentdate, rentlength, id))
    conn.commit()
    conn.close()

connect()

