import sqlite3 as lite

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

def alphabet():
    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    return alpha

def get_words(rows):
    words = []
    for row in rows:
        words.append(row[0].encode('ascii', 'ignore'))
    new = sorted(list(set(words)))
    new.sort(key=len)
    return new

def add_backhook():
    words = get_words(connect("SELECT word from words"))
    for word in words:
        hooks = []
        for ltr in alphabet():
            new_word = word + ltr
            if new_word in words:
                hooks.append(ltr)
        bhooks = ''.join(hooks)
        command = "UPDATE words SET back_hooks = '%s' WHERE word = '%s'" % (bhooks.lower(), word)
        update_db(command)
        print command

def add_fronthook():
    words = get_words(connect("SELECT word from words WHERE length <= 9"))
    for word in words:
        hooks = []
        for ltr in alphabet():
            new_word = ltr + word
            if new_word in words:
                hooks.append(ltr)
        fhooks = ''.join(hooks)
        command = "UPDATE words SET front_hooks = '%s' WHERE word = '%s'" % (fhooks.lower(), word)
        update_db(command)
        print command

add_fronthook()
