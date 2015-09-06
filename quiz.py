import lookup, leave_calc, calendar, time, os

class Quiz(object):
    def __init__(self, questions):
        self.count = 1
        self.questions = questions
        self.correct = 0
        self.incorrect = 0
        self.questions_correct = []
        self.questions_incorrect = []
        self.total = 0

    def quiz_main(self):
        for item in self.questions:
            os.system('clear')
            self.quiz_status()
            self.ask_question(item)
            choice = raw_input("Press Enter to continue or enter a command... ")
            if choice == '':
                continue

    def ask_question(self, question):
        cnt = 1
        answers = []
        print question
        data = raw_input("%d." % cnt).upper()
        if data == '':
            print "\n"
            print answers
            print self.check(question, answers)
            self.update(self.check(question,answers),question)
            lookup.search_initiate(**{"search_type" : "annagram", "srch_trm": question})
        while data != '':
            answers.append(data)
            cnt = cnt +1
            data = raw_input("%d." % cnt).upper()
            if data == '':
                print "\n"
                print self.check(question, answers)
                self.update(self.check(question,answers),question)
                lookup.search_initiate(**{"search_type" : "annagram", "srch_trm": question})

    def check(self, question, answers):
        kwargs = {"alphagram":question, "search_type":"check"}
        correct_answers = lookup.build_list(**kwargs)
        if sorted(answers) == sorted(correct_answers):
            return "Correct"
        else:
            return "Incorrect"

    def quiz_status(self):
        print "Question %d of %d" % (self.count, len(self.questions))
        if self.correct + self.incorrect != 0:
            print "%d of %d Correct %.2f%% " % (self.correct, self.total, 100*float(self.correct)/float(self.total))

    def update(self, result, question):
        kwargs = {'result':result,'question':question}
        self.update_db(**kwargs)
        if result == 'Correct':
            self.correct = self.correct + 1
            self.count = self.count + 1
            self.total = self.total + 1
            self.questions_correct.append(question)
        if result == 'Incorrect':
            self.incorrect = self.incorrect + 1
            self.count = self.count + 1
            self.total = self.total + 1
            self.questions_incorrect.append(question)

    def update_db(self, **kwargs):
        current_time = calendar.timegm(time.gmtime())    
        question = kwargs['question']
        if kwargs['result'] == 'Correct':
            command1 = "INSERT OR IGNORE INTO study_list (question,correct_answers,incorrect_answers,last_asked,streak,last_correct,last_incorrect,length) VALUES('%s',0,0,0,0,0,0,%d)" % ( question,len(question)) 
            command2 = "UPDATE study_list SET correct_answers = correct_answers +1, last_correct = %d, last_asked = %d,streak = streak +1 WHERE question = '%s'" % (current_time, current_time, question)
            leave_calc.update_db(command1)
            leave_calc.update_db(command2)
        if kwargs['result'] == 'Incorrect':
            command1 = "INSERT OR IGNORE INTO study_list (question,correct_answers,incorrect_answers,last_asked,streak,last_correct,last_incorrect,length) VALUES('%s',0,0,0,0,0,0,%d)" % ( question,len(question)) 
            command2 = "UPDATE study_list SET incorrect_answers = incorrect_answers +1, last_incorrect = %d, last_asked = %d,streak = 0 WHERE question = '%s'" % (current_time, current_time, question)
            leave_calc.update_db(command1)
            leave_calc.update_db(command2)


