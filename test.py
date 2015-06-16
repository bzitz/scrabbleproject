import sqlite3 as lite
import sys, csv

def update_anagramct():
    con = lite.connect('twl14.db')

    with con:
        con.row_factory = lite.Row  
        cur = con.cursor()

        cur.execute("SELECT alphagram FROM words")
        rows = cur.fetchall()
        li = []
        for row in rows:
            li.append(row[0])
        for word in li:
            x = li.count(word)
            print word
            cur.execute("UPDATE words SET num_anagrams=? WHERE alphagram=?",(x,word))


update_anagramct()
    
