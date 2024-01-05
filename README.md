# QUIZTIME

![Favicon image](assets/images/favicon-32x32.png)

**Quiztime is a Python terminal game that uses the mock terminal by Code Institute on Heroku**

This general knowledge quiz is played by one player. They set a target but can they beat it?

-------------

## Table of contents

1. What is Quiztime?<br/>
    1.1 Brief introduction<br/>
    1.2 Basic mechanics<br/>
    1.3 Link to Quiztime<br/>
2. Planning<br/>
    2.1 What? Why? Who?<br/>
    2.2 User Stories<br/>
3. Gameplay & Design<br/>
    3.1 Gameplay<br/>
    3.2 Excel file<br/>
    3.3 Interactability<br/>
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

## 1. What is Quiztime?


#### 1.1 Brief Intruction

- Quiztime is a general knowledge game
- There are 3 difficulty levels to choose from
- Users set their target for correct answers before they start
- Questions come with 4 possible answers alternatives to choose from
- When all 10 questions are answered, the scores and targets are checked and logged

#### 1.2 Basic mechanics

- Quiztime is run on a mock Python terminal created by Code Institute
- It is connected to an excel file which not only supplies the questions but stores the results
- An import of rich has been used to provide color to text
- The project is deployed via Heroku

#### 1.3 Link to Quiztime

Quiztime can be found using this [link](https://quiztime.herokuapp.com/)

---------------

## 2. Planning

#### 2.1 What? Why? Who?

What is the project about?

- This project aims to show the python terminal and several functions that show that a simple Python project can create a basic but interesting game

Why choose this project?

- I am interesting in quizzes and so it was interesting to me to design a quiz game using this (relatively) simplistic form of Python
- This was very challenging but it has also helped me to learn more not only about Python but coding in general

Who is this project aimed at?

- The kind of people who I feel would like this project would either be people interested in general knowledge quizzes or people who have an interest in how Python can work

#### 2.2 User Stories

*Developer*

- As a **developer** I can **create easy to follow instructions**<br>so that **I can provide a game that is fun immediately**
- As a **developer** I can **create a target score function**<br>so that **I can give the user a heightened sense of challenge**
- As a **developer** I can **add small time delays**<br>so that **users can easily see when things have been added to the screen**
- As a **developer** I can **create questions that are concise and easy to understand**<br>so that **the game is not confusing for the user and to provide a good user experience**
- As a **developer** I can **provide questions on a range of topics**<br>so that **I can provide a variety of questions that challenges all different subjects for the user**
- As a **developer** I can **create a range of difficulties**<br>so that **the user is finds the game more challenging and more dynamic**
- As a **developer** I can **provide multiple choice answers per question**<br>in order to **make the answering easier by providing choices for the user instead of asking them to type out an answer**
- As a **developer** I can **check users answer after every question**<br>so that **the user is kept updated and involved in their progress**
- As a **developer** I can **a visual that has alternating colours**<br>in order to **give the game a less dull appearance despite its text-only visuals**
- As a **developer** I can **create a database for questions**<br>so that **it is easier to add or update questions or topics
- As a **developer** I can **create a database to store user information**<br>so that **I can monitor the difficulty levels and how often the quiz is played**
- As a **developer** I can **create functioning error handling**<br>so that **the game doesn’t crash if an incorrect value is entered by the user**


*User*

- As a **user** I can **see instructions**,<br>so that **I can understand the game quickly to make playing more enjoyable**
- As a **user** I can **enter my name**,<br>so that **I feel personally attached to the game to heighten my experience**
- As a **user** I can **Play different levels**,<br>so that **I am able to play the game many times over and find it enjoyable**
- As a **user** I can **Have several possible options**,<br>in order to **to provide a challenge of choosing the correct answer to questions I’m not sure about**
- As a **user** I can **See what the correct was after every question**,<br>in order to **to inform me of the correct answer if I did get the answer wrong**
- As a **user** I can **Store my details**,<br>in order to **provide feedback to the developer for possible improvements**

---------------

## 3. Gameplay & Design

#### 3.1 Gameplay:

On page loading, the game starts

![Screenshot of whole page](assets/images/start_page.jpg)

...and the player enters their chosen name

![Screenshot of player having chosen their name](assets/images/enter_name.jpg)

The user will be asked what their chosen difficulty level of their 10 questions would be

![Screenshot of choice of difficulty](assets/images/choose_difficulty.jpg)

They can choose between easy...

![Screenshot of after the easy choice is taken](assets/images/easy_difficulty.jpg)

...medium...

![Screenshot of after the medium choice is taken](assets/images/medium_difficulty.jpg)

...or hard

![Screenshot of after the hard choice is taken](assets/images/hard_difficulty.jpg)

Their next choice is to set their target. They can choose between 1 and 10.
If they set 1 and 5

![Screenshot of choosing a target of 3](assets/images/goal_onetofive.jpg)

or between 6 and 10

![Screenshot of choosing a target of 6](assets/images/goal_sixtoten.jpg)

The player will then be shown the first question and it's 4 alternative answers. 

![Screenshot of the first question in the easy category and four alternative answers](assets/images/q1_easy.jpg)

The players enter their answers by pressing the A, B, C or D keys on the keyboard and pressing enter.
The answer is revealed and their current score is also updating after every answer.

An incorrect answer will give a score of 0 for that question

![Screenshot of the result of a wrong answer and the score being added is 0](assets/images/q1_wrong_answer.jpg)

While a correct answer gives a score of 1 for that question

![Screenshot of the result of a correct answer and the score being add is 1](assets/images/q1_correct_answer.jpg)

After all 10 questions are answered, the results of the quiz and if the target was beaten are calculated
If the user doesn't beat their target

![Screenshot of the message that the user has not beaten their target](assets/images/missed_target.jpg)

If the user matches their target

![Screenshot of the message that the user has matched their target](assets/images/matched_target.jpg)

If the user beats their target

![Screenshot of the message that the user has beaten their target](assets/images/beat_target.jpg)

Their results are then saved and stored in the same database that stores the questions and the final message is displayed

![Screenshot of the message that the users results have been saved, thanks for playing and the author & date](assets/images/final_message.jpg)

**New Game and cancel game**

A new game can be run by pressing the "run program" button at the top of the page

![Screenshot of the run program button on the webpage](assets/images/run_program.jpg)

A game can be canceled during play by holding the ctrl button and pressing the c key on your keyboard

![Screenshot of canceling a game by pressing ctrl and c on the keyboard](assets/images/cancel_game.jpg)

#### 3.2 Excel file

The excel file called quiztime is connected through the gspread import.

![Screenshot of the easy tab in the excel file called quiztime](assets/images/excelfile_easyquestions.jpg)

In total there are 5 tabs in the file
- "easy" containing the 10 easy questions
- "medium" containing the 10 medium questions
- "hard" containing the 10 medium questions
- "all_questions" containing all questions
- "results" containing a list of the completed user quizzes and their total score

![Screenshot showing all of the tabs in the excel file called quiztime](assets/images/excel_tabs.jpg)

![Screenshot showing the results tab in the excel file called quiztime](assets/images/excel_scores.jpg)

#### 3.3 Interactability

**Interactive buttons**

There is one clickable button and that is above the mock terminal
- the "run program" button as shown in 3.1

As the program uses the terminal the keyboard is most important and these uses for keys are as follows:
- entering username (whole keyboard + enter)
- choosing difficulty level (1,2 or 3 + enter)
- setting target goal (1-10 + enter)
- answering questions (A,B,C or D + enter)
- canceling a game (holding ctrl button while pressing the c key)

--------





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

![Screenshot of start screen taken using https://techsini.com/multi-mockup/index.php](assets/images/multi_device_website_check.jpg)

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

