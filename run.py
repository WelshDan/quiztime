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

questions = SHEET.worksheet('questions')

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
    Get user's target score out of 10
    """
    while True:
        print("The quiz contains 10 questions.\nWhat is your target score out of 10?")
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
            return True

target_score()

#def question_test()



#data = questions.get_all_values()

#print(data)