import time
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
   ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('quiztime')

questions = SHEET.worksheet('blist')

total_questions = 10
score = 0
questions_list = []
question_index = 0


def welcome_screen():
    """
    Start screen that welcomes the user
    """
    print("Hello!")
    time.sleep(2)
    print("and welcome to...")
    time.sleep(3)
    print("QUIZTIME")
    time.sleep(2)


def player_name():
    """
    Get username from the user
    """
    print("Please enter your name")

    username = input("My name is \n")
    time.sleep(2)
    print(f"Welcome {username}!")
    time.sleep(2)


def target_score():
    """
    Get user's target score out of 10. Run a while loop to collect the
    players guess of their correct answer \n target, via
    the terminal which has to be a number between 1 and 10. The loop will
    \n repeat until a figure between 1 and 10 is entered.
    """
    while True:
        print("The quiz contains " + str(total_questions) + " questions.\n \
            What is your target score?\n")
        time.sleep(2)
        users_goal = int(input("My goal is: "))
        time.sleep(1)
        target = range(1, 11)
        print(f"OK, good luck trying to get more than {users_goal}!")
        try:
            if users_goal not in target:
                raise ValueError(
                    f"Your target must be between 1 and 10. You provided {users_goal}")
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")
            return False
        else:
            print("Are you sure you are up to it?")
            time.sleep(2)
            return {users_goal}


def ask_question():
    """
    Locate the first question in the list. Repeat \
        until all 10 questions are asked.
    """
    question = questions_list[question_index + 1]
    print(f" Here is question {question[0]}...\n")
    time.sleep(2)
    print(question[1])


def save_answer():
    """
    User enters answer with a letter between A and D.
    Answer is logged for later results.
    """
    global score
    while True:
        print("What is your answer? A,B,C or D\n")
        time.sleep(2)
        answer = input("My answer is \n").lower()
        time.sleep(2)
        current_answer = questions_list[question_index + 1][2].lower()
        possible_answers = ["a", "b", "c", "d"]
        try:
            if answer not in possible_answers:
                raise ValueError("You can only answer with A, B, C or D")
            else:
                if questions_list[question_index + 1][2].lower() == answer:
                    score = score + 1
                print(f"Thank you for your answer.\n \
                    \n\nThe correct answer was {current_answer}\n")
                print(f"Your current score is {score} \n")
                time.sleep(2)
                break
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")


def display_results(users_goal, score):
    """
    Target score and actual score are compared and the results are returned
    """
    print(f"Your final score is {score}")
    time.sleep(2)

    if score > users_goal:
        print(f"Sadly, your target score was {users_goal}")
        time.sleep(1)
        print(f"but you only got {score}.")
        time.sleep(1)
        print("You are not as clever as you think")
    elif score == users_goal:
        print(f"Well done! Your target score was {users_goal}")
        time.sleep(1)
        print("and you matched that it!")
        time.sleep(1)
        print(f"You scored {score}. You know exactly how clever you are!")
    else:
        print(f"Congratulations! Your target was {users_goal}")
        time.sleep(1)
        print(f"but you scored {score}")
        time.sleep(1)
        print("You are much smarter than you think you are!")


def initialise_questions():
    global questions_list
    questions_list = questions.get_values()


def main():
    global question_index
    initialise_questions()
    welcome_screen()
    player_name()
    users_goal = target_score()
    while question_index < total_questions:
        ask_question()
        save_answer()
        question_index += 1
    display_results(users_goal, score)
    print("Your final score was...")
    time.sleep(3)
    print(f"...{score}")
    print("Thank you for playing \n\n ")
    print("(Dan Roberts 2023)")


main()
