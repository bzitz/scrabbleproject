import os, lookup, sys, question, quiz

def choice_handler(choice):
    if choice == ":s":
        search()
    elif choice == ":sa":
        query("annagram")
    elif choice == ":sp":
        query("pattern")
    elif choice == ":sn":
        query("new")
    elif choice ==":judge":
        query("judge")
    elif choice ==":r7":
        start_quiz(lookup.random_7())
    elif choice ==":l50":
        start_quiz(lookup.last_50_missed())
    elif choice == ":quit":
        print "Goodbye"
        sys.exit
    else:
        data = raw_input("No command found choose again...  ")
        choice_handler(data)

def main():
    os.system('clear')
    data = raw_input("Enter Choice... ")
    choice_handler(data)

def search():
    os.system('clear')
    print "Enter :sa for Annagram lookup"
    print "Enter :sp for Pattern match"
    data = raw_input()
    choice_handler(data)

def query(param):
    os.system('clear')
    if param == "annagram" or param == "pattern":
        print "Enter %s you would like to search" % param
        word = raw_input()
        kwargs = {"srch_trm" : word,"search_type" : param }
        lookup.search_initiate(**kwargs) 
        wrd_lst = lookup.build_list(**kwargs)
        print "\n"
    if param == "new":
        print "Enter Length or 0 for all new words"
        srch = raw_input()
        kwargs = {"length" : srch, "search_type" : param}
        lookup.search_initiate(**kwargs)
        wrd_lst = lookup.build_list(**kwargs)
        print "\n"
    data = raw_input("Press Enter to continue or :help to see other commands...  ")
    if data == "":
        query(param)
    elif data == ":quiz":
        new_quiz = quiz.Quiz(wrd_lst)
        new_quiz.quiz_main()
        choice = raw_input("Would you like to quiz on the missed questions... ")
        if choice == 'y':
            missed_quiz = quiz.Quiz(new_quiz.questions_incorrect)
            missed_quiz.quiz_main()
    else:
        choice_handler(data)

def start_quiz(word_list):
    new_quiz = quiz.Quiz(word_list)
    new_quiz.quiz_main()
    choice = raw_input("Would you like to quiz on the missed questions... ")
    if choice == 'y':
        missed_quiz = quiz.Quiz(ran_quiz.questions_incorrect)
        missed_quiz.quiz_main()
    else:
        main()

main()
