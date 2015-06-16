import sqlite3 as lite
import sys, csv
from tabulate import tabulate

def connect(query):
    con = lite.connect('twl14.db')

    with con: 
        con.row_factory = lite.Row
        cur = con.cursor()

        cur.execute(query)
        rows = cur.fetchall()
    return rows
    
def get_words():
    rows = connect("SELECT alphagram FROM words WHERE length = 3")
    words = []
    for row in rows:
        words.append(row[0].encode('ascii', 'ignore'))
    new = sorted(list(set(words)))
    new.sort(key=len)
    return new, words

def xstr(s):
    if s is None:
        return ''
    else:
        return str(s)

def print_table(table):
    print("\n")
    print tabulate(
                    sorted(table, key=lambda x: x[1]),    
                    headers=['Fhook','Word','Bhook','Definition'],
                    tablefmt="simple"
                   )


def alphagram_info(alpha):
    rows = connect("SELECT front_hooks,word,back_hooks,definition FROM words WHERE alphagram = '%s'" % alpha)
    words = make_table(rows)  
    return words                   
    

def make_table(data):
    words = []
    for row in data:
        fh = xstr(row[0])
        wrd = xstr(row[1])
        bh = xstr(row[2])
        defin = xstr(row[3])
        lst = [fh,wrd,bh,defin]
        words.append(lst)
    return words   

def new_threes():
    rows = connect("SELECT front_hooks,word,back_hooks,definition FROM words WHERE length = 4 and lexicon_symbol = '$'")
    print_table(make_table(rows))

print_table(alphagram_info('INTY'))
