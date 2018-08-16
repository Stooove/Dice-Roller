# Dice Roller
This is a readme file for my simple 2 Dice simulator.

This application requires tkinter and pillow to run. tkinter is normally bundled into python 3, while pillow requires a separate install. When deploying this application to Heroku, it crashed just after reading Dice.py, when trying to run "from tkinter import Tk," with the error "import _tkinter # If this fails your Python may not be configured for Tk. ModuleNotFoundError: No module named '_tkinter'"

I checked the pipfile, and while it contains pillow as a dependency, it does not list tkinter as one. As I investigated which pipenv install command to run to add tkinter to the pip, I found some posts saying it was impossible. Because Heroku is using Ubuntu which uses python3 without tkinter, I can run command "apt install python3-tk", but this only works for my local machine. This doesn't help the application deploy and the application already runs through my IDE - where I have python3 and tkinter already installed. Looking at the project interpreter files of my IDE, there's a file "_tkinter_finder"_ which seems to be what Ubuntu/Heroku is missing. 

I recommend running this program through an IDE with python3 and pillow frameworks installed. If upon application launch the error: "no module named PIL" then use the terminal to install pillow "pip3 install pillow". It should launch a program titled "Python" which is a combination of Tcl 8.5 & Tk 8.5, which is what tkinter links together. 

As programmed, this application will roll 2 dice, either 4 or 6 sided. With minimum background changes, it should be dynamic enough to support additional faces and additional dice if the specifications change. Additional dice and additional faces would require additional GUI build. 
