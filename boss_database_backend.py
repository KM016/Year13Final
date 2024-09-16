import sqlite3

def connect():
    conn = sqlite3.connect("employer.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS boss(id INTEGER PRIMARY KEY, boss_user text, boss_pass text)")
    conn.commit()
    conn.close()

def insert(boss_user, boss_pass):
    conn = sqlite3.connect("employer.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO boss VALUES(NULL,?,?)",(boss_user, boss_pass))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("employer.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM boss")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(boss_user = "", boss_pass = ""):
    conn = sqlite3.connect("employer.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM boss WHERE boss_user = ? or boss_pass = ?",(boss_user, boss_pass))
    rows = cur.fetchall()
    conn.close()
    return rows

  
def delete(id):
    conn = sqlite3.connect("employer.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM boss WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update(id ,boss_user, boss_pass):
    conn = sqlite3.connect("employer.db")
    cur = conn.cursor()
    cur.execute("UPDATE boss SET (boss_user=?,  boss_pass =? WHERE id = ?",(boss_user, boss_pass, id))
    conn.commit()
    conn.close()

connect()




