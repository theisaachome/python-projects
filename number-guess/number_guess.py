import random;


top_of_range = input("Enter a range number : ");

if top_of_range.isdigit:
    top_of_range = int(top_of_range);
    if top_of_range <=0 :
        print("Please enter a number greater than 0 next time.")
        quit();

random_number= random.randrange(0,top_of_range);
guesses = 0;

while True:
    guesses += 1;
    user_guess= input("Make a guess : ")
    if user_guess.isdigit:
        user_guess = int(user_guess)
    else:
        print("Please enter a number  next time.")
        continue

    if user_guess == random_number:
        print("You got it.",random_number);
        break
    elif user_guess > random_number:
            print("You are above the number.")
    else:
            print("You got it wrong.")
            
print("You got it in ", guesses ," guesses.")