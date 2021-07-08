import  random
from art import logo4
HARD_LEVEL_TURNS = 5
EASY_LEVEL_TURNS = 10
def check_guess(number,guess):
    if number>guess:
        print('Too low')
    elif number<guess:
        print('Too high')
    else:
        print(f'You have got correct {guess} number')

def difficultly():
    level = input('choose defficulatly level,type "hard" or "easy"')
    if level=='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
number = random.randint(1,100)
print(logo4)
print('Welcome to number guessing number!')
print("I'm thinking of a number between 1 and 100.")
turns = difficultly()
repeat = True
while repeat:
    guess = int(input('make guess number:'))
    print(f'you have {turns} remains')
    check_guess(number=number,guess=guess)
    turns -=1
    if number==guess:
        repeat=False
    elif turns<0:
        print('you have lost.')
        repeat=False

