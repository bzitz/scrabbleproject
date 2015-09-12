import sqlite3 as lite
import sys, csv, calendar, time
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

def search_initiate(**kwargs):
    if kwargs["search_type"] == "annagram":
        srch_trm = kwargs["srch_trm"]
        print_table(annagram_search(srch_trm))
    if kwargs["search_type"] == "pattern":
        srch_trm = kwargs["srch_trm"]
        print_table(pattern_search(srch_trm))
    if kwargs["search_type"] == "new":
        length = kwargs["length"]
        print_table(newword_search(length))

def annagram_search(srch_trm):
    if '?' in srch_trm: 
        new = srch_trm.translate(None, '?')
        frmt = '%' + '%'.join(sorted(new)).upper() + '%'
    else: 
        frmt = ''.join(sorted(srch_trm)).upper()
    rows = connect("SELECT front_hooks,word,back_hooks,definition,lexicon_symbol,alphagram FROM words WHERE length = %d AND alphagram LIKE '%s'" % (len(srch_trm), frmt))
    words = make_table(rows)  
    return words

def random_7():
    words = []
    rows = connect("SELECT question FROM study_list WHERE length = 7 AND last_asked = 0 ORDER BY RANDOM() LIMIT 50")
    for item in rows:
        question = xstr(item[0])
        words.append(question)
    return words

def last_50_missed():
    words = []
    current_time = calendar.timegm(time.gmtime())
    rows = connect("SELECT question FROM study_list WHERE streak = 0 AND last_asked > 1 ORDER BY last_asked LIMIT 50")
    for item in rows:
        question = xstr(item[0])
        words.append(question)
    return words

def pattern_search(srch_trm):
    if '?' in srch_trm:
        data = srch_trm.replace('?','_').upper()
    else:  
        data = srch_trm.upper()
    rows = connect("SELECT front_hooks,word,back_hooks,definition,lexicon_symbol FROM words WHERE word LIKE '%s'" % data )
    words = make_table(rows)  
    return words

def newword_search(length):
    if int(length) == 0:
        rows = connect("SELECT front_hooks,word,back_hooks,definition,lexicon_symbol FROM words WHERE lexicon_symbol = '$'")
    else:
        rows = connect("SELECT front_hooks,word,back_hooks,definition,lexicon_symbol FROM words WHERE lexicon_symbol = '$' AND length = %d" % int(length))
        
        words = make_table(rows)  
    return words                   
   
def format_data(**kwargs):
    if kwargs["search_type"] == "pattern":
        srch_trm = kwargs["srch_trm"].upper()
        if '?' in srch_trm:
            return srch_trm.replace('?','_'), len(srch_trm)
        else:
            return srch_trm, len(srch_trm)
    elif kwargs["search_type"] == "annagram":
        srch_trm = ''.join(sorted(kwargs["srch_trm"])).upper()
        if '?' in srch_trm:
            new = srch_trm.translate(None,'?')
            frmt = "%" + '%'.join(new) + "%"
            return frmt, len(srch_trm)
        else:
            return srch_trm, len(srch_trm)

def make_table(data):
    words = []
    for row in data:
        fh = xstr(row[0])
        wrd = xstr(row[1]) + ' ' + xstr(row[4])
        bh = xstr(row[2])
        defin = xstr(row[3])
        lst = [fh,wrd,bh,defin]
        words.append(lst)
    return words   

def build_list(**kwargs):
    if kwargs["search_type"] == "check":
        alphagram = kwargs["alphagram"]
        rows = connect("SELECT word FROM words WHERE alphagram = '%s'" % alphagram)
        word_list = []
        for row in rows:
            wrd = xstr(row[0])
            word_list.append(wrd)
        return word_list
    if kwargs["search_type"] == "annagram" or kwargs["search_type"] == "pattern":
        alpha_list = []
        data = format_data(**kwargs)
        if kwargs["search_type"] == "annagram":
            rows = connect("SELECT alphagram FROM words WHERE length = %d AND alphagram LIKE '%s'" % (data[1], data[0]))
        elif kwargs["search_type"] == "pattern":
            rows = connect("SELECT alphagram FROM words WHERE length = %d AND word LIKE '%s'" % (data[1], data[0]))
        for row in rows:
            alphagram = xstr(row[0])
            if alphagram not in alpha_list:
                alpha_list.append(alphagram)
        return alpha_list
    if kwargs["search_type"] == "new":
        wrd_list = []
        number = kwargs["length"] 
        rows = connect("SELECT alphagram FROM words WHERE lexicon_symbol = '$' AND length = %d" % int(number))
        for row in rows:
            alphagram = xstr(row[0])
            if alphagram not in wrd_list:
                wrd_list.append(alphagram)
        return wrd_list

def main(_, word):
    alpha = ''.join(sorted(word))
    print_table(alphagram_info(alpha.upper()))

if __name__=='__main__':
    main(*argv)

