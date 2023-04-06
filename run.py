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

TOTAL_QUESTIONS = 10
score = 0
questions_list = []
question_index = 0

def player_name():
    """
    Get username from the user
    """
    print("Please enter your name")

    username = input("Username: ")
    print(f"Welcome {username}!")


def target_score():
    """
    Get user's target score out of 10. Run a while loop to collect the
    players guess of their correct answer \n target, via
    the terminal which has to be a number between 1 and 10. The loop will
    \n repeat until a figure between 1 and 10 is entered.
    """
    while True:
        print("The quiz contains " + str(TOTAL_QUESTIONS) + "questions.\nWhat is your target score out of 10?")
        target_score = input("My goal is: ")
        target = range(1, 10)
        print(f"OK, good luck trying to get more than {target_score}!")
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
            return True

def ask_question():
    """
    Locate the first question in the list
    """
    question = questions_list[question_index + 1]
    print(f" Here is question {question[0]}...")
    print(question[1])

def save_answer():
    """
    User enters answer with a letter between A and D.
    Answer is logged for later results.
    """
    global score
    while True:
        print("What is your answer? A,B,C or D")
        answer = input("My answer is ").lower()
        print(f"You've guessed answer {answer}")
        possible_answers = ["a", "b", "c", "d"]
        try:
            if answer not in possible_answers:
                raise ValueError(f"You can only answer with A, B, C or D")
            else: 
                if questions_list[question_index + 1][2].lower() == answer:
                    score = score + 1
                print("Thank you for your answer.")
                break
        except ValueError as error:
                print(f"Invalid data: {error}, please try again.\n")
       


#ask_next_question()

#check_quiz_complete()

#display_results

#close_quiz

#print(data)

def initialise_questions():
    global questions_list
    questions_list = questions.get_values()


def main():
    global question_index
    initialise_questions()
    player_name()
    target_score()
    while question_index < TOTAL_QUESTIONS:
        ask_question()
        save_answer()
        question_index = question_index + 1
    print(f"\n\n\n\n\n\nYour score is: {score}\n")



main()