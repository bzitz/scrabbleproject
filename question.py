import os, sys, lookup, leave_calc, calendar, time

def quiz_main(question):
    os.system("clear")
    print question
    print "\n"
    cnt = 1
    answers = []
    data = raw_input("%d." % cnt).upper()
    if data == '':
        print "\n"
        results(check(question,answers),question)
        
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
        kwargs = {'result':result, 'question':question} 
        update_db(**kwargs)
        print "CORRECT"
        lookup.search_initiate(**{"search_type" : "annagram", "srch_trm": question})
    elif result == 'incorrect':
        print "INCORRECT"
        lookup.search_initiate(**{"search_type" : "annagram", "srch_trm": question})

def update_db(**kwargs):
    current_time = calendar.timegm(time.gmtime())    
    question = kwargs['question']
    if kwargs['result'] == 'correct':
       command1 = "INSERT OR IGNORE INTO study_list (question,correct_answers,incorrect_answers,last_asked,streak,last_correct,last_incorrect,length) VALUES('%s',0,0,0,0,0,0,%d)" % ( question,len(question)) 
       command2 = "UPDATE study_list SET correct_answers = correct_answers +1, last_correct = %d, last_asked = %d,streak = streak +1 WHERE question = '%s'" % (current_time, current_time, question)
    leave_calc.update_db(command1)
    leave_calc.update_db(command2)


  
