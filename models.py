import sqlite3 as sql

def insertLog(username,
        movement,
        weight,
        repetitions,
        rpe):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO logs (username,movement,weight,repetitions,rpe) VALUES (?,?,?,?,?)",
            (username,movement,weight,repetitions,rpe))
    con.commit()
    con.close()
