#!/usr/local/bin/python3
# guess_your_number.py
"""
Guess Your Number rules:
    I, the computer, will attempt to guess your number.  This is the exact
    opposite of the proposition made in guess_my_number.py.  You must pick
    a number between one and ten.  I will make a guess.  If I am incorrect,
    tell me if I am too high or too low.  If I guess, I win.

    Note that you need to run this with python 3.x for it to work.
"""

from random import randint, choice

def main():
    print("""Think of a number between 1 and some arbitrary upper bound and I will guess it. 
    For example, if you are thinking of a number between 1 and 1000, 1000 is your upper bound.
    Don't let my artificial intelligence intimidate you.\n""")
    input("Think of a number, then press <enter>.\n") 
    lBound = 1
    uBound = get_upper_bound() 
    play = input("Alright.  I'm ready.  Are you ready to play? (y/n): ")
    while not game_over(play):
        if lBound == uBound:
            print("Ah, this must be your number: {num}".format(num=uBound))
        guess = get_guess(lBound, uBound) 
        print("Is this your number?: {num}".format(num=guess))
        answer = input("Enter 'y' for yes or 'n' for no: ")
        if answer.lower()[0] == 'y':
            print(choice(WIN_MESSAGE))
            play = play_again(action='play')
            if play.lower()[0] == 'y':
                input("Think of another number, then press <enter>.")
                lBound, uBound = 1, get_upper_bound()
        else:
            print(choice(LOSE_MESSAGE))
            play = play_again()
            if play.lower()[0] == 'n': break
            direction = input("Was I too high (enter 'h') or too low (enter 'l')?: ")
            if direction.lower()[0] == 'h':
                uBound = guess - 1
            else: # guess was too low
                lBound = guess + 1
    print(choice(ENDING_MESSAGE))

def get_upper_bound():
    return int(input("Got a number?  Ok--what is the upper bound of your range?: "))

def play_again(action='guess'):
    questions = ["I'm feelin' good!  I think I've got your number.  Give it another shot? (y/n) ",
                 "Shall I guess again? (y/n) "] 
    return input(questions[0] if action == 'play' else questions[1])

def game_over(play):
    return False if play.lower()[0] == 'y' else True

def get_guess(lower, upper):
    return (upper + lower) // 2

WIN_MESSAGE = ["BAM!!!  I win!", "Simple minds are easy to read.", 
               "Looks like I've got you figured out."]
LOSE_MESSAGE = ["You must be wearing a tinfoil hat...",
                "I think you cheated.",
                "Darn it. Are you sure you weren't thinking of a letter?"]
ENDING_MESSAGE = ["Aww, c'mon!!! I was just getting warmed up!  Fine, then, get lost.",
                  "I'd be scared, too, if I were you.  Goodbye.",
                  "Don't like being that easy to read, huh?  Goodbye."]

if __name__ == '__main__': main()
