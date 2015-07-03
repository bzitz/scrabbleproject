import sqlite3 as lite
import sys, csv
from tabulate import tabulate
from sys import argv

def connect(query):
    con = lite.connect('twl14.db')

    with con: 
        con.row_factory = lite.Row
        cur = con.cursor()

        cur.execute(query)
        rows = cur.fetchall()
    return rows

def xstr(s):
    if s is None:
        return ''
    else:
        return str(s)

def print_table(table):
    print("\n")
    if table:
        print tabulate(
            sorted(table, key=lambda x: x[1]),    
            headers=['Fhook','Word','Bhook','Definition'],
            tablefmt="simple"
            )
        print len(table)
    else:
        print "No data matching that search"


def search_results(**kwargs):
    if kwargs["search_type"] == "annagram":
        alpha = ''.join(sorted(kwargs["srch_trm"])).upper()
        rows = connect("SELECT front_hooks,word,back_hooks,definition FROM words WHERE length = 7 AND alphagram LIKE '%s'" % '%A%E%I%R%S%T%')
        words = make_table(rows)  
    elif kwargs["search_type"] == "pattern":
        data = format_data(**kwargs)
        rows = connect("SELECT front_hooks,word,back_hooks,definition FROM words WHERE word LIKE '%s'" % data )
        words = make_table(rows)  
    return words                   
   
def format_data(**kwargs):
    if kwargs["search_type"] == "pattern":
        srch_trm = kwargs["srch_trm"]
        if '?' in srch_trm:
            return srch_trm.replace('?','_')
        else:
            return srch_trm
            
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

def find(wrd, param):
    print_table(search_results(wrd.upper(), param))

def main(_, word):
    alpha = ''.join(sorted(word))
    print_table(alphagram_info(alpha.upper()))

if __name__=='__main__':
    main(*argv)

