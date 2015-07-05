import sqlite3 as lite
import itertools
import lookup

def connect(query):
    con = lite.connect('twl14.db')

    with con: 
        con.row_factory = lite.Row
        cur = con.cursor()

        cur.execute(query)
        rows = cur.fetchall()
    return rows

def update_db(command):
    con = lite.connect('twl14.db')
    with con:
        cur = con.cursor()
        cur.execute(command)

def get_combo():
    combos = itertools.combinations("AABCDDEEFGHIIJKLMMNOOPQRRSSTTUVWXYZ", 4)
    lstcombos = list(combos)
    final = {}
    for x in range(len(lstcombos)):
        combo = ''.join(lstcombos[x])
        kwargs = {"search_type":"annagram", "srch_trm" : "???"+combo}
        table =  lookup.search_results(**kwargs)
        lst = [combo,len(table)]
        final[combo] = len(table)
    srt_final = sorted(final, key=final.get, reverse=True)[:1000]
    for x in srt_final:
        print x,final[x]
        command = "INSERT INTO four_letter_leaves (leave,sevens) VALUES ('%s',%d)" % (x,final[x]) 
        update_db(command)
get_combo()
