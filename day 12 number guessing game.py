from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer: 
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        
def set_difficulty():
    level = input("What level do you want to play? Type 'Easy' or 'Hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():        
    print("Number Guessing Game")
    print("I'm thinking of a number between 1 and 100. What do you think it is?")
    answer = randint(1, 100)
    
    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")
    
    guess = 0
    while guess != answer:
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
    
    print("Congratulations! You won!")

game()
