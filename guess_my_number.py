<<<<<<< HEAD
=======
#!/usr/local/bin/python3
>>>>>>> 99e127b827708c343dd12fb260556b9155da2427
# guess_my_number.py
"""
Guess My Number rules:
    The computer will choose a number between 1 and 10.  Your goal is to guess what the
    number is.  The computer will give you hints on whether you are too high or too low
    with your guess.  Keep playing until you get it right!!
<<<<<<< HEAD
=======

    I've removed separate functions that picked  a number and get the guess from user in
    order to shorten the lines of code used for competition.  I don't know if it matters
    or if tradeoffs in readability for what amounts to 4 fewer lines of code is worth it.

    Note that this is written in PYTHON 3.2.
>>>>>>> 99e127b827708c343dd12fb260556b9155da2427
"""
from random import randint, choice

def main():
<<<<<<< HEAD
    play = input("Hey!  Buddy!  Psst...over here: wanna play a game? (y/n): ") 
    number = pick_number() # Need to keep same number each time
    while not game_over(play):
        guess = get_guess()
        if guess == number:
            print(choice(YOU_WIN))
            play = play_again(action='play')
            number = pick_number()
        elif guess > number:
            print(choice(TOO_HIGH))
            play = play_again()
        else:
            print(choice(TOO_LOW))
            play = play_again()
=======
    play = input("Hey!  Buddy!  Psst...over here: wanna play guess my number? (y/n): ") 
    number = randint(1,10)
    while play.lower()[0] != 'n': 
        win = False
        guess = int(input("Pick a number between 1 and 10: "))
        if guess == number:
            print(choice(YOU_WIN))
            number = randint(1,10) 
            win = True  # informs play_again version to use 
        elif guess > number:
            print(choice(TOO_HIGH))
        else:
            print(choice(TOO_LOW))
        play = play_again(action='play') if win else play_again()
>>>>>>> 99e127b827708c343dd12fb260556b9155da2427
    print(choice(GOODBYE))

def play_again(action='guess'):
    questions = ["Feeling lucky? Want to go for another round? (y/n) ",
                 "Don't be a quitter.  Guess again? (y/n) "]
    return input(questions[1] if action == 'guess' else questions[0])
                
<<<<<<< HEAD
def pick_number():
    return randint(1,10)

def get_guess():
    return eval(input("Pick a number between 1 and 10: "))

def ready_to_play():
    p = input("Are you ready to play? (y/n): ")
    return p

def game_over(play):
    if play.lower()[0] == 'y':
        return False
    return True

=======
>>>>>>> 99e127b827708c343dd12fb260556b9155da2427
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
