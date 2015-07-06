import os, sys, lookup

questions = ["EHLLO","AEINSTR"]

def quiz_main(question):
    os.system("clear")
    print question
    print "\n"
    cnt = 1
    answers = []
    data = raw_input("%d." % cnt).upper()
    while data != '':
        answers.append(data)
        cnt = cnt + 1
        data = raw_input("%d." % cnt).upper()
        if data == '':
            print "\n"
            results(check(question,answers),question)
                
def check(question,answers):
    rows = lookup.connect("SELECT word FROM words WHERE alphagram = '%s'" % question)
    correct_answers = []
    for row in rows:
        wrd = lookup.xstr(row[0])
        correct_answers.append(wrd)
    if sorted(answers) == sorted(correct_answers):
        return "correct"
    elif sorted(answers) != sorted(correct_answers):
        return "incorrect"

def results(result, question):
    if result == 'correct':
        print "CORRECT"
        lookup.print_table(lookup.search_results(**{"search_type" : "annagram", "srch_trm": question}))
    elif result == 'incorrect':
        print "INCORRECT"
        lookup.print_table(lookup.search_results(**{"search_type" : "annagram", "srch_trm": question}))

def test(question):
    for x in question:
        quiz_main(x)
        print "\n"
        choice = raw_input("Press Enter to continue or enter a command... ")

test(questions)
