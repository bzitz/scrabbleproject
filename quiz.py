import os, sys

kwargs = {"questions" : ['EHLLO', 'ABS']}
def quiz_main(**kwargs):
    for x in range(len(kwargs["questions"])):
        # os.system("clear")
        print kwargs["questions"][x]
        print "\n"
        cnt = 1
        answers = []
        data = raw_input("%d." % cnt)
        while data != '':
            answers.append(data)
            cnt = cnt + 1
            data = raw_input("%d." % cnt)
            if data == '':
                if kwargs['questions'][x] == "EHLLO":
                    answer_key = ['HELLO']
                elif kwargs['questions'][x] == "ABS":
                    answer_key = ['ABS','SAB','BAS']
                if sorted(answers) == sorted(answer_key):
                    print "CORRECT"
                elif answers != answer_key:
                    print "INCORRECT"
                
                print sorted(answers)

quiz_main(**kwargs)

