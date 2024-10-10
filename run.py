import time
import gspread
from google.oauth2.service_account import Credentials
from rich import print
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({"success": "green", "error": "red", "question": "cyan", "info": "yellow", "command": "blue", "quiztime": "bold magenta"})
console = Console(theme=custom_theme)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
   ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('quiztime')

DIFFICULTY_LEVEL_TO_NAME_MAP = {
    1: "Easy",
    2: "Medium",
    3: "Hard"
}

DIFFICULTY_LEVEL_TO_SHEET_NAME_MAP = {
    1: "easy",
    2: "medium",
    3: "hard"
}

TOTAL_QUESTIONS = 10
score = 0
questions_list = []
question_index = 0


def show_welcome_screen():
    """ Start screen that welcomes the user."""
    console.print("   Hello!\n", style="info")
    time.sleep(0.5)
    console.print("   and welcome to...\n", style="info")
    time.sleep(1)
    console.print("   QUIZTIME\n", style="quiztime")
    time.sleep(0.5)


def get_player_name():
    """Get username from the user. A while loop with a true check to stop users entering a blank name."""
    while True:
        username = input(" Please enter your name: \n ")
        if username.strip():
            break
        console.print(" Name cannot be empty. Please enter your name\n", style="error")

    time.sleep(0.5)
    console.print(f"\n Welcome {username}!\n", style="info")
    time.sleep(0.5)
    return username


def choose_difficulty():
    """
    User is to select one of three options: easy, medium or hard.
    The options are connected to three different tabs of the worksheet
    with containing a set of easy, medium or hard questions
    """
    console.print(" You will now need to choose the difficulty level of the quiz \n", style="info")
    time.sleep(0.5)
    console.print(" You can select from easy, medium or hard\n", style="info")
    time.sleep(0.5)
    console.print(" Select your difficulty by pressing 1,2 or 3 and then enter\n", style="command")
    time.sleep(0.5)
    console.print(" 1 = Easy , 2 = Medium, 3 = Hard\n", style="info")
    time.sleep(0.5)

    while True:
        users_difficulty = input(" My choice is: \n ")

        if users_difficulty.strip() == "":
            console.print("You have entered a blank space. Please choose between 1, 2 and 3. \n", style="error")
            continue

        try:
            check_users_difficulty = int(users_difficulty)
            if check_users_difficulty in range(1, 4):
                console.print("\n You have chosen the " + DIFFICULTY_LEVEL_TO_NAME_MAP[check_users_difficulty] + " difficulty level\n", style="info")
                return check_users_difficulty
            else:
                console.print(f" You must choose between 1,2 and 3. You provided {users_difficulty}\n", style="error")
        except ValueError as error:
            console.print(f" {users_difficulty} is not a number. Please choose between 1,2 and 3.\n", style="error")
 

def initialise_questions(difficulty):
    """
    Using the difficulty level set in choose_difficulty, the correct questions are loaded.
    """
    global questions_list
    question_set = SHEET.worksheet(DIFFICULTY_LEVEL_TO_SHEET_NAME_MAP[difficulty])
    questions_list = question_set.get_values()

def target_score():
    """
    Get user's target score out of 10. Run a while loop to collect the
    players guess of their correct answer target, via the terminal which
    has to be a number between 1 and 10. The loop will repeat until a
    number between 1 and 10 is entered.
    """
    users_goal = None

    console.print(" The quiz contains " + str(TOTAL_QUESTIONS) + " questions.\n", style="info")
    console.print(" What is your target score? Please choose a target between 1 and 10. \n", style="command")
    time.sleep(0.5)

    while True:
        users_goal = input(" My goal is: \n ")
        time.sleep(0.5)

        if users_goal.strip() == "":
            console.print("You have entered a blank space. Please choose a target between 1 and 10. \n", style="error")
            continue

        try:
            check_users_goal = int(users_goal)
            if check_users_goal in range(1, 11):
                if users_goal <= 5:
                    console.print(f"\n {check_users_goal} is your score to beat, good luck!\n", style="info")
                else:
                    console.print(f"\n Challenging target! Best of luck trying to beat {check_users_goal}!\n", style="info")
                break
            else:
                console.print(f" Your target must be between 1 and 10. You provided {users_goal}\n", style="error")
        except ValueError as error:
            console.print(f" You entered {users_goal} but that is not a number. Please try again.\n", style="error")
        
    return check_users_goal


def ask_question():
    """
    Locate the first question in the list. Repeat until the
    total questions are asked.
    """
    question = questions_list[question_index + 1]
    console.print(f" Here is question {question[0]}...\n", style="info")
    time.sleep(0.5)
    console.print(question[1], style="question")


def accept_answer():
    """
    User enters answer with a letter between A and D.
    Answer is logged for later results.
    """
    global score
    while True:
        console.print(" What is your answer? (A,B,C or D)\n", style="command")
        time.sleep(0.5)
        answer = input(" My answer is \n ").upper()
        time.sleep(0.5)
        correct_answer = questions_list[question_index + 1][2].upper()
        possible_answers = ["A", "B", "C", "D"]
        try:
            if answer not in possible_answers:
                raise ValueError(" You can only answer with A, B, C or D\n")
            else:
                if answer == correct_answer:
                    score = score + 1
                    console.print(f" Good answer, {correct_answer} was correct!\n", style="success")
                else:
                    console.print(f"\n Thank you for your answer.\n The correct answer was {correct_answer}\n", style="info")
                    console.print(f" The answer {answer} was incorrect\n", style="error")
                console.print(f" Your current score is {score} \n", style="info")
                time.sleep(0.5)
                break
        except ValueError as error:
            console.print(f" You have not chosen A,B, C or D. Please try again.\n", style="error")


def display_results(username, users_goal):
    """
    Target score and actual score are compared and the results are returned
    """
    console.print(f" Your final score is {score}\n", style="info")
    time.sleep(0.5)

    if score < users_goal:
        console.print(f" Sadly, your target score was {users_goal} but you only got {score}\n", style="error")
        time.sleep(0.5)
        console.print("  You just missed your target, bad luck!\n", style="error")
    elif score == users_goal:
        console.print(f" Well done! Your target score was {users_goal} and you matched it!\n", style="info")
        time.sleep(0.5)
        console.print("  You hit your target, well done!\n", style="info")
    elif score > users_goal:
        console.print(f" Congratulations! Your target was {users_goal} and you scored {score}!", style="success")
        time.sleep(0.5)
        console.print("  You beat it! Excellent work!\n", style="success")

    console.print(" Scores are being saved to the history books\n", style="info")
    time.sleep(0.5)
    data = [username, score]
    saves_worksheet = SHEET.worksheet("results")
    saves_worksheet.append_row(data)

    console.print("   Thank you for playing\n ", style="info")
    time.sleep(0.5)
    console.print("   (Created by Dan Roberts 2023)")

def start_quiz(username, users_goal):
    global question_index
    question_index = 0
    while question_index < TOTAL_QUESTIONS:
        ask_question()
        accept_answer()
        question_index += 1
    display_results(username, users_goal)

def main():
    global question_index
    global score
    show_welcome_screen()
    username = get_player_name()
    difficulty = choose_difficulty()
    initialise_questions(difficulty)
    users_goal = target_score()
    start_quiz(username, users_goal)
   

main()
