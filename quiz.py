class Quiz(object):
    def __init__(self, questions):
        self.count = 1
        self.questions = questions
        self.correct = 20
        self.incorrect = 0
        self.questions_correct = []
        self.questions_incorrect = []
        self.total = self.correct + self.incorrect

    def quiz_main(self):
        print self.questions
        for item in self.questions:
            self.ask_question(item)
            self.update

    def ask_question(self, question):
        self.quiz_status()

    def quiz_status(self):
        print "Question %d of %d" % (self.count, len(self.questions))
        if self.correct + self.incorrect != 0:
            print "%d of %d Correct %.2f%% " % (self.correct, self.total, 100*float(self.correct)/float(self.total))

test = Quiz(['help','me','crazy'])

test.quiz_main()

