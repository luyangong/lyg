import random

pets = {'cat': 'littleblack', 'dog': 'bigyellow', 'pig': 'littlegrey'}

for quizNum in range(3):
    quizFile = open('quiz%s.txt'%(quizNum + 1), 'w')
    answerFile = open('quiz%s_answers.txt'%(quizNum + 1), 'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(' ' * 20 + 'the right name of pets quiz(Form %s)'%(quizNum + 1))
    quizFile.write('\n\n')

    animal = list(pets.keys())
    random.shuffle(animal)

    for questionNum in range(3):

        correctAnswer = pets[animal[questionNum]]
        wrongAnswers = list(pets.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 1)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write('%s. Which is the name of %s?\n\n'%(questionNum + 1, animal[questionNum]))
        for i in range(2):
            quizFile.write('%s. %s  '%('AB'[i], answerOptions[i]))
        quizFile.write('\n\n')

        answerFile.write('%s. %s\n'%(questionNum + 1, 'AB'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerFile.close()
        
    
