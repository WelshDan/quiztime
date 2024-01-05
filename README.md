# QUIZTIME
![Favicon image](assets/images/favicon-32x32.png)

Quiztime is a Python terminal game that uses the mock terminal by Code Institute on Heroku.

This general knowledge quiz is played by one player. They set a target but can they beat it?

---------------

## Table of contents

1. How to play Quiztime<br/>
    1.1 Basic Rules<br/>
2. Planning<br/>
    2.1 Aim of simplicity<br/>
    2.2 Used languages<br/>
3. Layout & Design<br/>
    3.1 Website structure<br/>
    3.2 Page layout<br/>
    3.3 Icons<br/>
4. Description of game screen<br/>
    4.1 Interactive parts<br/>
    4.2 Non-interactive parts<br/>
5. Important code functions<br/>
    5.1 JavaScript functions<br/>
    5.2 Python start code<br/>
6. Testing, issues & Bugs<br/>
    6.1 Online tests<br/>
    6.2 Manual testing<br/>
7. Issues & Bugs<br/>
    7.1 Resolved issues<br/>
    7.2 Unresolved issues<br/>
    7.3 Possible future developments<br/>
    7.4 Validator testing<br/>
8. Deployment<br/>
    8.1 Github deployment<br/>
    8.2 Link<br/>
9. 404 page<br/>
    9.1 Page layout<br/>
    9.2 Interactive parts<br/>
    9.3 Non-interactive parts<br/>
10. Credits<br/>
    10.1 Credits, references and thanks<br/>

---------------

## 1. How to play

Quiztime is a general knowledge game where a player answers questions, having 4 alternatives to choose from. The questions are taken from a range of subjects. The game continues until all 10 questions are answered.



![Screenshot of start screen taken using https://techsini.com/multi-mockup/index.php](assets/images/multi_device_website_check.jpg)

#### 1.1 Basic Rules:

The game starts...

![Screenshot](assets/images/pic1.jpg)

...and the player enters their chosen name.

![Screenshot](assets/images/pic1.jpg)

...and then a target score for them to try and beat.

![Screenshot](assets/images/pic2.jpg)

The player will then be shown 10 questions and the 4 alternative answers. The players enter their answers by pressing the A, B, C or D keys on the keyboard and pressing enter.

![Screenshot](assets/images/pic3.jpg)

Their score is checked and then the correct answer is shown.

![Screenshot](assets/images/pic3.jpg)

Their running score is logged.

![Screenshot](assets/images/pic3.jpg)

Once the 10th question is answered, that score checked then the final score is revealed and also if the user beat their target score!

![Screenshot](assets/images/pic3.jpg)

Their results are then saved and stored in the same database that stores the questions

### Features

  This score is out of 10.
   

### Existing features

One player game
Player plans to beat their projected final score
Questions appear one at a time
Input validation and error checking
All four possible answer alternatives are used during the quiz

### Future features

New questions to be added
Players could type in their answer
Colours could be added to make the game more dynamic

## TESTING

The code has been run through the PEP8 validator online program.

### Bugs

#### Removed Bugs

#### Remaining Bugs

A function called display results which compares the final score and the target score to return a comment about the result has been commented out in the code.

#### Validator testing

PEP8 - online test

![Screenshot](assets/images/PEP8check.jpg)

## DEPLOYMENT

The project was deployed using the mock terminal made by Code Institute on Herokus website.

## CREDITS

### Deployment

Code Institute for deployment terminal
Quiztime deployed via Heroku
Quiztime is an idea created and deployed by Dan Roberts 2023

### Help and guidance

GURU99.com - time delay function
(https://www.guru99.com/python-time-sleep-delay.html#:~:text=Python%20sleep()%20is%20a,the%20execution%20of%20your%20code)

Akhsat Garg - mentor at Code Institute

Problem with not loading:
sudo apt install libcairo2-dev pkg-config python3-dev
pip3 install pycairo
pip install gspread
pip install -r requirements.txt
python3 run.py

https://www.youtube.com/watch?v=4zbehnz-8QU
Color and text format:
pip install rich
from rich import print ( adds color to numbers)
from rich.console import Console (add color to by adding console to print ie console.print and adding stylings)
from rich.theme import Theme (add themes and then repeat using console.print and adding stylings code)

