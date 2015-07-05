import os, lookup, sys

def choice_handler(choice):
    if choice == ":s":
        search()
    elif choice == ":sa":
        query("annagram")
    elif choice == ":sp":
        query("pattern")
    elif choice == ":sn":
        query("new")

    elif choice == ":quit":
        print "Goodbye"
        sys.exit

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
        kwargs = {"srch_trm" : word,"search_type" : param}
        lookup.print_table(lookup.search_results(**kwargs)) 
        print "\n"
    if param == "new":
        print "Enter Length or 0 for all new words"
        srch = raw_input()
        kwargs = {"length" : srch, "search_type" : param}
        lookup.print_table(lookup.search_results(**kwargs))
        print "\n"
    data = raw_input("Press Enter to continue or :help to see other commands...  ")
    if data == "":
        query(param)
    else:
        choice_handler(data)

main()
