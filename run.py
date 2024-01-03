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


def show_welcome_screencreen():
    """
    Start screen that welcomes the user
    """
    print("Hello!\n")
    # time.sleep(2)
    print("and welcome to...\n")
    # time.sleep(3)
    print("QUIZTIME\n")
    # time.sleep(2)


def get_player_name():
    """
    Get username from the user. A while loop with a true check to
    stop users entering a blank name
    """
    while True:
        username = input("Please enter your name: ")
        if username.strip():
            break
        print("Name cannot be empty. Please enter your name")

    # time.sleep(1)
    print(f"Welcome {username}!")
    # time.sleep(1)
    return username


def choose_difficulty():
    """
    User is to select one of three options: easy, medium or hard.
    The options are connected to three different tabs of the worksheet
    with containing a set of easy, medium or hard questions
    """
    print("You will now need to choose the difficulty level of the quiz \n")
    # time.sleep(1)
    print("You can select from easy, medium or hard\n")
    # time.sleep(1)
    print("Select your difficulty by pressing 1,2 or 3 and then enter\n")
    # time.sleep(1)
    print("1 = Easy , 2 = Medium, 3 = Hard\n")
    # time.sleep(1)

    while True:
        try:
            users_difficulty = int(input("My choice is: \n"))
            if users_difficulty not in range(1, 4):
                raise ValueError(f"You must choose either 1,2 or 3. You provided {users_difficulty}\n")
            else:
                print("You have chosen an " + DIFFICULTY_LEVEL_TO_NAME_MAP[users_difficulty] + " difficulty level\n")
                return users_difficulty    
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")
 

def initialise_questions(difficulty):
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
    while True:
        print("The quiz contains " + str(TOTAL_QUESTIONS) + " questions.\n")
        print("What is your target score?\n")
        # time.sleep(2)
        try:
            users_goal = int(input("My goal is: \n"))
            # time.sleep(1)
            if users_goal not in range(1, 11):
                raise ValueError(f"Your target must be between 1 and 10. You provided {users_goal}\n")
            else:
                if users_goal <= 5:
                    print(f"{users_goal} is your score to bear, good luck!\n")
                else:
                    print(f"Challenging target! Best of luck trying to beat {users_goal}!\n")
                break
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")
        
    return users_goal


def ask_question():
    """
    Locate the first question in the list. Repeat \
        until all 10 questions are asked.
    """
    question = questions_list[question_index + 1]
    print(f"Here is question {question[0]}...\n")
    # time.sleep(2)
    print(question[1])


def accept_answer():
    """
    User enters answer with a letter between A and D.
    Answer is logged for later results.
    """
    global score
    while True:
        print("What is your answer? (A,B,C or D)\n")
        # time.sleep(2)
        answer = input("My answer is \n").lower()
        # time.sleep(2)
        correct_answer = questions_list[question_index + 1][2].lower()
        possible_answers = ["a", "b", "c", "d"]
        try:
            if answer not in possible_answers:
                raise ValueError("You can only answer with A, B, C or D\n")
            else:
                if answer == correct_answer:
                    score = score + 1
                    print(f"Good answer, {correct_answer} was correct!\n")
                else:
                    print(f"Thank you for your answer.\nThe correct answer was {correct_answer}\n")
                    print(f"The answer {answer} was incorrect\n")
                print(f"Your current score is {score} \n")
                # time.sleep(2)
                break
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")


def display_results(username, users_goal):
    """
    Target score and actual score are compared and the results are returned
    """
    print(f"Your final score is {score}\n")
    # time.sleep(2)

    if score > users_goal:
        print(f"Sadly, your target score was {users_goal} but you only got {score}\n")
        # time.sleep(1)
        print("You just missed your target, bad luck!\n")
    elif score == users_goal:
        print(f"Well done! Your target score was {users_goal} and you matched that it!\n")
        # time.sleep(1)
        print("You hit your goal, well done!\n")
    else:
        print(f"Congratulations! Your target was {users_goal} but you scored {score}!")
        # time.sleep(1)
        print("You beat your goal! Excellent work!\n")

    print("Scores are being saved to the history books\n")
    data = [username, score]
    saves_worksheet = SHEET.worksheet("results")
    saves_worksheet.append_row(data)

    print("Thank you for playing \n\n ")
    print("(Dan Roberts 2023)")

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
    show_welcome_screencreen()
    username = get_player_name()
    difficulty = choose_difficulty()
    initialise_questions(difficulty)
    users_goal = target_score()
    start_quiz(username, users_goal)
   

main()
