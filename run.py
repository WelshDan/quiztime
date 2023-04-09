import gspread
from google.oauth2.service_account import Credentials
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('quiztime')

questions = SHEET.worksheet('Alist')

total_questions = 10
score = 0
questions_list = []
question_index = 0


def welcome_screen():
    """
    Start screen that welcomes the user
    """
    print("Hello")
    time.sleep(2)
    print("Welcome to...")
    time.sleep(2)
    print("QUIZTIME")
    time.sleep(2)


def player_name():
    """
    Get username from the user
    """
    print("Please enter your name")

    username = input("My name is ")
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
        print("The quiz contains " + str(total_questions) + " questions.\
            What is your target score?\n")
        time.sleep(2)
        target_score = int(input("My goal is: "))
        time.sleep(2)
        target = range(1, 10)
        print(f"OK, good luck trying to get more than {target_score}!")
        try:
            if target_score is target:
                raise ValueError(
                    f"Your target must be between 1 and 10, \
                        you provided {target_score}"
                    )
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")
            return False
        else:
            print("Can you beat that target?")
            time.sleep(2)
            return True


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
        answer = input("My answer is ").lower()
        time.sleep(2)
        print(f"You've guessed answer {answer}")
        possible_answers = ["a", "b", "c", "d"]
        try:
            if answer not in possible_answers:
                raise ValueError("You can only answer with A, B, C or D")
            else:
                if questions_list[question_index + 1][2].lower() == answer:
                    score = score + 1
                print("Thank you for your answer.")
                time.sleep(3)
                break
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")


def display_results():
    """
    Target score and actual score are compared and the results are returned.
    """
    if total_questions == 10:
        print(f"Your final score is {score}")
        return target_score
        time.sleep(2)
    if score > target_score:
        print(f"Sadly, your target score was {target_score}\
            but you only got {score}.")
        print("You are not as clever as you think")
    if score == target_score:
        print(f"Well done! Your target score was {target_score} \
            and you matched that it!")
        print(f"You scored {score}. You know exactly how clever you are!")
    if score < target_score:
        print(f"Congratulations! Your target was {target_score}\
            but you scored {score}")
        print("You are much smarter than you think you are!")


def initialise_questions():
    global questions_list
    questions_list = questions.get_values()


def main():
    global question_index
    initialise_questions()
    welcome_screen()
    player_name()
    target_score()
    while question_index < total_questions:
        ask_question()
        save_answer()
        question_index = question_index + 1
        display_results()
    print("Thank you for taking part in the quiz")
    print("(Dan Roberts 2023)")


main()