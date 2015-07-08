import os, sys, lookup

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
    kwargs = {"alphagram":question, "search_type":"check"}
    correct_answers = lookup.build_list(**kwargs)
    if sorted(answers) == sorted(correct_answers):
        return "correct"
    elif sorted(answers) != sorted(correct_answers):
        return "incorrect"

def results(result, question):
    if result == 'correct':
        print "CORRECT"
        lookup.search_initiate(**{"search_type" : "annagram", "srch_trm": question})
    elif result == 'incorrect':
        print "INCORRECT"
        lookup.search_initiate(**{"search_type" : "annagram", "srch_trm": question})

def test(question):
    for x in question:
        quiz_main(x)
        print "\n"
        choice = raw_input("Press Enter to continue or enter a command... ")

