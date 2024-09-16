import sqlite3

def connect():
    conn = sqlite3.connect("employees.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY, fn text, sn text, passw text, date text, email text, phone text)")
    conn.commit()
    conn.close()

def insert(fn, sn, passw, date, email, phone):
    conn = sqlite3.connect("employees.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO employee VALUES(NULL,?,?,?,?,?,?)",(fn, sn, passw, date, email, phone))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("employees.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(fn = "", sn ="", passw ="", date= "", email ="", phone = ""):
    conn = sqlite3.connect("employees.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM employee WHERE fn =? or sn =? or passw =? or date =? or email =? or phone =?",(fn, sn, passw, date, email, phone))
    rows = cur.fetchall()
    conn.close()
    return rows

  
def delete(id):
    conn = sqlite3.connect("employees.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM employee WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update(id, fn, sn, passw, date, email, phone):
    conn = sqlite3.connect("employees.db")
    cur = conn.cursor()
    cur.execute("UPDATE employee SET fn =?, sn =?, passw =?, date =?, email =?, phone =? WHERE id = ?",(fn, sn, passw, date, email, phone, id))
    conn.commit()
    conn.close()

connect()



