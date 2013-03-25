#!/usr/local/bin/python3
# guess_my_number.py
"""
Guess My Number rules:
    The computer will choose a number between 1 and 10.  Your goal is to guess what the
    number is.  The computer will give you hints on whether you are too high or too low
    with your guess.  Keep playing until you get it right!!

    I've removed separate functions that picked  a number and get the guess from user in
    order to shorten the lines of code used for competition.  I don't know if it matters
    or if tradeoffs in readability for what amounts to 4 fewer lines of code is worth it.

    Note that this is written in PYTHON 3.2.
"""
from random import randint, choice

def main():
    play = input("Hey!  Buddy!  Psst...over here: wanna play a game? (y/n): ") 
    number = randint(1,10)
    while not game_over(play):
        guess = int(input("Pick a number between 1 and 10: "))
        if guess == number:
            print(choice(YOU_WIN))
            play = play_again(action='play')
            number = randint(1,10) 
        elif guess > number:
            print(choice(TOO_HIGH))
            play = play_again()
        else:
            print(choice(TOO_LOW))
            play = play_again()
    print(choice(GOODBYE))

def play_again(action='guess'):
    questions = ["Feeling lucky? Want to go for another round? (y/n) ",
                 "Don't be a quitter.  Guess again? (y/n) "]
    return input(questions[1] if action == 'guess' else questions[0])
                
def game_over(play):
    if play.lower()[0] == 'y':
        return False
    return True

TOO_HIGH = ["You're higher than Smoky on a Friday...",
            "How's the view from 30,000 feet?  You're kinda high...",
            "Bring it down a notch, Miss Cleo."]

YOU_WIN = ["You win! Now if only the rest of your life was this smooth...",
           "You're the big wiener!  That is to say, you guessed my number...",
           "Way to go, winner.  You're the world champ at number guessing.  Hope it pays well.",
           "You win.  Nice."]

TOO_LOW = ["Whoa, whoa, whoa!  Below the belt!  Bring it up a bit.",
           "That's pretty low, mister.  If I had a rubber hose...",
           "You're killing me here...bring it up."]

GOODBYE = ["Ok, quitter.  You coulda been a contender.",
           "See ya, sucker.",
           "Maybe next time, Einstein."]

if __name__ == '__main__': main()
