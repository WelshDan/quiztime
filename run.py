import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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


def player_name():
    """
    Get username from the user
    """
    print("Please enter your name")

    username = input("Username: ")
    print(f"Welcome {username}!")

player_name()

def target_score():
    """
    Get user's target score out of 10. Run a while loop to collect the
    players guess of their correct answer \n target, via
    the terminal which has to be a number between 1 and 10. The loop will
    \n repeat until a figure between 1 and 10 is entered.
    """
    while True:
        print("The quiz contains 10 questions.\n What is your target score out of 10?")
        target_score = input("My goal is: ")
        target = range(1,10)
        print(target_score)
        try:
            if target_score is target:
                raise ValueError(
                    f"Your target must be between 1 and 10, you provided {target_score}"
                    )
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")
            return False
        else:
            print("Can you beat that target? Good luck with the quiz.")
            print("Here comes your first question...")
            return True

target_score()

def start_quiz():
    """
    Locate the first question in the list
    """
    question_number = questions.acell("A2").value
    print(f" Here is question {question_number}...\n")
    question = questions.acell("B2").value
    print(question)

start_quiz()

#ask_question()

#save_answer()

#ask_next_question()

#check_quiz_complete()

#display_results

#close_quiz

#print(data)