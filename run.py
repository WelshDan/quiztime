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

def new_player():
    """
    Get username from the user
    """
    print("Please enter your name")

    username = input("Username: ")
    print(f"Welcome {username}!")

new_player()

def target_score():
    """
    Get user's target score out of 10
    """
    print("The quiz contains 10 questions. What is your target score out of 10?")
    target_score = input("My goal is: ")

target_score()

#data = questions.get_all_values()

#print(data)