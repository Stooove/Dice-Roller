'''Better UI:
1. a better framework than tkinter to more easily change the background color from grey. (tkk doesn't allow this directly).
2. better pictures of dice, 4 sided, and 6 sided
3. add additional dice faces, either with more buttons or a slider
4. add dice animation and sounds
5. add additional dice
'''

from tkinter import Tk  # for window
from tkinter import ttk  # for frames, labels, and buttons
import random  # to make dice work
from PIL import Image, ImageTk  # to display pictures


class DiceRoller(object):
    '''
    This class simulates rolling dice with varying number of sides
    '''

    def __init__(self, parent): #self is the app
        '''
        creates all buttons and labels
        '''
        '''
        Grid Layout:
        row 1: current dice face count 
        row 2: sum and flair
        row 3: images
        row 4: blank - row between displays and buttons. can be used for additional buttons or display as needed.
        row 5: individual roll buttons
        row 6: combined roll button
        row 7: dice face button
        '''

        parent.title('Dice Roller')  # window name
        parent.geometry('265x215')  # window size

        self.mainFrame = ttk.Frame(parent)  # housing for all buttons (within self, put a frame into it)
        self.mainFrame.grid()  # make mainFrame organized by grid

        self.Sides = 6  # default for number of faces on dice
        self.Count = 2  # default for number of dice
        self.Rolled = False  # control for first pass through, used for blanking pictures if they exist

        self.rolls = []  # keep track of the numerical answers

        self.BlankerX = []  # keep track of dice images
        self.BlankerX = self.ListInit(self.BlankerX)  # initialize list (used as part of application load)
        for i in range(self.Count):
            self.BlankerX[i] = ttk.Label(self.mainFrame)  # build labels for each

        '''Initial title. Updated in DiceSwitch()'''
        self.CurrentlyRolling = 'Currently Rolling: ' + str(self.Sides) + '-faced Dice'
        self.Title = ttk.Label(self.mainFrame, text=self.CurrentlyRolling, font='Helvetica 16 bold')
        self.Title.grid(row=1, column=0, columnspan=self.Count)

        '''Ensure app loads with correct spacing for pictures'''
        self.SumFlair = ttk.Label(self.mainFrame, text='Sum: 0')  # initial 0, dice don't roll upon open.
        self.SumFlair.grid(row=2, column=0, columnspan=self.Count)
        blank = Image.open('blank space.png')
        self.ShowImg(blank, 1)
        self.ShowImg(blank, 2)

        '''Button creation'''
        self.Roll = ttk.Button(self.mainFrame, text='Roll Dice 1', command=(lambda: self.RollDiceX(0)))  # lambda in use to make it a function object - prevents the application from running on startup. Not used in other buttons as I'm not passing a value to them)
        self.Roll.grid(row=5, column=0)

        self.Roll2 = ttk.Button(self.mainFrame, text='Roll Dice 2', command=(lambda: self.RollDiceX(1)))
        self.Roll2.grid(row=5, column=1)

        self.RollAll = ttk.Button(self.mainFrame, text='Roll Both', command=self.RollAll)
        self.RollAll.grid(row=6, column=0, columnspan=self.Count)

        self.DiceButton = ttk.Button(self.mainFrame, text='Switch to: 4-Sided', command=self.DiceSwitch)
        self.DiceButton.grid(row=7, column=0, columnspan=self.Count)

    def RollAll(self):  # allow for additional dice in the future. RollAll would pass all number of Dice to RollDiceX.
        '''Corresponds to the 'Roll Both' button, and iteratively passes all dice to RollDiceX.'''
        for i in range(self.Count):
            self.RollDiceX(i)

    def RollDiceX(self, i):
        '''Randomly generates a number between 1 and self.Sides (inclusively). Stores these rolls in the list 'self.rolls.' Checks and initializes self.rolls '''
        answer = random.randint(1, self.Sides)
        self.rolls = self.ListInit(self.rolls) #ensure self.rolls has enough space in it. performed here incase adding dice is a later feature and could be added after some dice on screen.
        self.rolls[i] = answer
        self.BlankerX[i] = (self.LoadImg(answer, (i+1), self.BlankerX[i]))
        self.RollSum()

    def ListInit(self, arr):
        if len(arr) == 0: #first time its run
            arr = [0] * self.Count
        elif len(arr) < self.Count: #if extra dice are added later, and you have some already on screen. Append by difference.
            missing = [0] * (self.Count - (len(arr)))
            arr.extend(missing)
        elif len(arr) > self.Count: #if dice are later removed, should only add dice on screen.
            n = ((len(arr))- (self.Count))
            del arr[-n]
        else:
            pass
        return arr

    def LoadImg(self, answer, n, img):
        '''Select image to show. Takes n for position (passthrough), and current img in BlankerX[n-1]'''
        # if additional dice faces are added, need to load new pictures, and controls below.
        # opportunity to improve, display a dice rolling/spinning
        # OTI: Play sounds, dice clacking then landing as answer 'settles in.'
        if self.Rolled == True:
            self.BlankOut(img)
        if self.Sides == 6:
            if answer == 1:
                load = Image.open('1d6pip.png')
            elif answer == 2:
                load = Image.open('2d6pip.png')
            elif answer == 3:
                load = Image.open('3d6pip.png')
            elif answer == 4:
                load = Image.open('4d6pip.png')
            elif answer == 5:
                load = Image.open('5d6pip.png')
            elif answer == 6:
                load = Image.open('6d6pip.png')
            else:
                load = Image.open('No Dice.png')
                print('6 sided dice has answer not between 1-6')
        elif self.Sides == 4:
            if answer == 1:
                load = Image.open('1D4.png')
            elif answer == 2:
                load = Image.open('2d4.png')
            elif answer == 3:
                load = Image.open('3D4.png')
            elif answer == 4:
                load = Image.open('4d4.png')
            else:
                load = Image.open('No Dice.png')
                print('4 sided dice has answer not between 1-4')
        else:
            load = Image.open('No Dice.png')
            print('Dice is neither 4 nor 6 sided')
        img = self.ShowImg(load, n)
        return img

    def ShowImg(self,load, n):
        '''given and image "load" and a position it should go "n", create the label for pictures, put the image in it, show the label, and position it'''
        load.thumbnail((90, 90))  # load is "open X image", now make it small- but preserve aspect ratio.
        render = ImageTk.PhotoImage(load)  # open the now small version of the .png into PhotoImage. render is the photo in imagetk.PhotoImage
        img = ttk.Label(self.mainFrame, image=render)  # make a label (img) to display an image, specifically render, put it onto my frame.
        img.image = render  # show program img is an image, put it in "img", pic is "render" from above
        if n == 1:
            img.grid(row=3, column=0)  # picture space 1
        elif n == 2:
            img.grid(row=3, column=1)  # picture space 2
        self.Rolled = True  # program has run at least once, blank out the images on subsequent runs to prevent pictures overlapping.
        return img

    def BlankOut(self, img):
        '''removes item from grid'''
        img.grid_forget() #wipe the space and forget what was there. (prevents previous picture from underlaying new pictures).

    def RollSum(self):
        '''add the results in self.rolls. Compile any Flair with Sum, rename SumFlair text.'''
        self.Sum = sum(self.rolls)
        funFlair = str(self.FunFlair(self.Sum))
        self.SumLabel = 'Sum: ' + str(self.Sum) + ' ' + funFlair
        self.SumFlair["text"] = self.SumLabel

    def FunFlair(self, sum):
        '''Checks whether Flair is appropriate'''
        # if adding additional dice, consider if flair should only be for 2 dice, just for the sum, or for for only 1's or only 6's
        if sum == 2:
            return "SNAKE EYES!"
        elif sum == 12:
            return "Box Car!"
        else:
            return ""

    def DiceSwitch(self):  # 'scale' would be more efficient for additional dice faces. Set scale to directly change self.Sides. Remove button
        '''Switch DiceButton text and self.Sides to 4 or 6'''
        if self.DiceButton["text"] == 'Switch to: 4-Sided':
            self.Sides = 4  # sides in use is 4
            self.DiceButton["text"] = 'Switch to: 6-Sided'
        else:
            self.Sides = 6
            self.DiceButton["text"] = 'Switch to: 4-Sided'
        self.CurrentlyRolling = 'Currently Rolling: ' + str(self.Sides) + '-faced Dice'
        self.Title["text"] = self.CurrentlyRolling


if __name__ == '__main__':
    root = Tk()  # new window
    dice = DiceRoller(root)  # instance, give it window
    root.mainloop()  # run it
