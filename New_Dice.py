import random
import sys


def main():
    '''main run for program'''
    dice_faces = dice_face_prompt()
    number_of_dice = number_of_dice_prompt()
    for i in range(number_of_dice):
        random_number = roll(dice_faces)
        show_roll(random_number)

def dice_face_prompt():
    '''asks user for useful number of dice faces.'''
    while True:
        try:
            dice_faces = int(input('How many faces should the dice have?'))
            assert 0 < dice_faces
            return dice_faces
        except:
            print("The dice must have an integer number of faces greater than or equal to 1")

def number_of_dice_prompt():
    '''asks user for useful number of dice.'''
    while True:
        try:
            number_of_dice = int(input('How many dice do you want to roll?'))
            assert 0 < number_of_dice
            return number_of_dice
        except :  # in IDE: handles strings and decimals. In terminal: handles blanks
            print("You must have an integer number of Dice greater than or equal to 1")

def roll(dice_faces):
    '''generates a random number between 1 and dice_faces'''
    random_number = random.randint(1, dice_faces)
    return random_number


def show_roll(random_number, output=sys.stdout): #use sys.stdout.write for unit testing, to verify expected matches actual.
    '''prints random_number (roll result) with text'''
    output.write('You rolled a {}\n'.format(random_number))

if __name__ == '__main__':
    main()