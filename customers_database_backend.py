import sqlite3

def connect():
    conn = sqlite3.connect("customers.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS customer(id INTEGER PRIMARY KEY, fn text, sn text, passw text, date text, email text, phone text)")
    conn.commit()
    conn.close()

def insert(fn, sn, passw, date, email, phone):
    conn = sqlite3.connect("customers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO customer VALUES(NULL,?,?,?,?,?,?)",(fn, sn, passw, date, email, phone))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("customers.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM customer")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(fn = "", sn ="", passw ="", date= "", email ="", phone = ""):
    conn = sqlite3.connect("customers.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM customer WHERE fn =? or sn =? or passw =? or date =? or email =? or phone =?",(fn, sn, passw, date, email, phone))
    rows = cur.fetchall()
    conn.close()
    return rows

  
def delete(id):
    conn = sqlite3.connect("customers.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM customer WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update(id, fn, sn, passw, date, email, phone):
    conn = sqlite3.connect("customers.db")
    cur = conn.cursor()
    cur.execute("UPDATE customer SET fn =?, sn =?, passw =?, date =?, email =?, phone =? WHERE id = ?",(fn, sn, passw, date, email, phone, id))
    conn.commit()
    conn.close()

connect()



