import sqlite3 as lite
import sys, csv


con = lite.connect('twl14.db')

with con:
    con.row_factory = lite.Row
    cur = con.cursor()

    cur.execute("SELECT word FROM words WHERE length is NULL")
    rows = cur.fetchall()
    for row in rows:
        cur.execute("UPDATE words SET length = ? WHERE word=?",(len(row['word']), row['word']))

