
score = 0 ;

class Quizz:
    def __init__(self,question,choice,answer):
        self.question=question
        self.answer=answer
        self.choice = choice
    
    def showQuest(self):
        global score
        print(self.question)
        for option in self.choice:
            print(" " + option)
        answer = input("You Anser : ");
        if answer.isdigit :
            answer = int(answer);
            if answer == self.answer:
               score += 1;
        else:
            print("Please enter a number next time")

    def showScore(self,totalQuestion):
        print("You got " + str(score) + " question correct!");
        print("You got " + str((score /totalQuestion) * 100) + " %.")


questions = [
    Quizz("What is the last book of the Old Testament? ",
    [
        "1. Gensis",
        "2 Mathew",
        "3 Malachi"
    ],3),
    Quizz("How many days and nights did Jesus fast?",[
        "1. 20 Days",
        "2. 40 Days",
        "3. 45 Days"
    ],2),

    Quizz("How many days was Jonah in the belly of the big fish? ",
    [
        "1. 2 days and 1 nights",
        "2. 3 days and 3 nights",
        "3. 4 days and 4 nights"
    ],2),

     Quizz("What were the names of the twins who wrestled in their mother's womb?",
    [
        "1. Jacob and Esau",
        "2. Peter and John",
        "3. James and Andrew"
    ],1),

    Quizz( "What does this name of God mean: Jehovah Rapha? ",
    [
        "1. Lord  God Almighty",
        "2. The lord will provde",
        "3. The Lord who heals"
    ],3),
]


def answerQuestions():
    for question in questions:
        question.showQuest();
    question.showScore(len(questions));




print("Welcome too Bible General Quiz Game\n")
print("To Start the game")
playing = input("Please enter yes: ")
if playing.lower() != "yes":
    print("Bye See you next time.")
    quit();

print("Ok let's play :) ");
answerQuestions();
