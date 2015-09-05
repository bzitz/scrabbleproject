class Quiz(object):
    def __init__(self, questions):
        self.questions = questions
        self.correct = 0
        self.incorrect = 0
        self.questions_correct = []
