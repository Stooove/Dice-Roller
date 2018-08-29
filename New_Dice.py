import random

def main():
    dice_faces = dice_face_prompt()
    number_of_dice = number_of_dice_prompt()
    for i in range(number_of_dice):
        random_number = roll(dice_faces)
        print_roll(random_number)

def dice_face_prompt():
    '''asks user for useful number of dice faces.'''
    while True:
        try:
            dice_faces = input('How many faces should the dice have?') #intentionally not using int(input(x)). If user puts 1.2, it will treat it as 1, user needs to know.
            if type(dice_faces) == float:
                print('You have chosen a number with a decimal. Instead, using ' + str(int(dice_faces)))
            dice_faces = int(dice_faces)
            assert 0 < dice_faces
            return dice_faces
        except NameError:  # in terminal: handles strings
            print("You must enter an integer greater than or equal to 1")
        except AssertionError:  # handles numbers <= 0
            print("You must enter an integer greater than or equal to 1")
        except: #in IDE: handles strings and decimals. In terminal: handles blanks
            print("You must enter an integer greater than or equal to 1")

def number_of_dice_prompt():
    '''asks user for useful number of dice.'''
    while True:
        try:
            number_of_dice = input('How many dice do you want to roll?')
            if type(number_of_dice) == float:
                print('You have chosen a number with a decimal. Instead, using ' + str(int(number_of_dice)))
            number_of_dice = int(number_of_dice)
            assert 0 < number_of_dice
            return number_of_dice
        except NameError:  # in terminal: handles strings
            print("You must enter an integer greater than or equal to 1")
        except AssertionError:  # handles numbers <= 0
            print("You must enter an integer greater than or equal to 1")
        except:  # in IDE: handles strings and decimals. In terminal: handles blanks
            print("You must enter an integer greater than or equal to 1")

def roll(dice_faces):
    random_number = random.randint(1, dice_faces)
    return random_number

def print_roll(random_number):
        print ('You rolled a ' + str(random_number))

main()
