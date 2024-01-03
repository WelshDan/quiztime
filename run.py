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

easy_questions = SHEET.worksheet('easy')
medium_questions = SHEET.worksheet('medium')
hard_questions = SHEET.worksheet('hard')

total_questions = 10
score = 0
questions_list = []
question_index = 0
USERNAME = ""


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


def get_player_name():
    """
    Get username from the user. A while loop with a true check to
    stop users entering a blank name
    """
    while True:
        USERNAME = input("Please enter your name: ")
        if USERNAME.strip():
            break
        print("Name cannot be empty. Please enter your name")

    time.sleep(2)
    print(f"Welcome {USERNAME}!")
    time.sleep(2)
    return USERNAME


def users_difficulty():
    """
    User is to select one of three options: easy, medium or hard.
    The options are connected to three different tabs of the worksheet
    with containing a set of easy, medium or hard questions
    """
    print("You will now need to choose the difficulty level of the quiz \n")
    time.sleep(1)
    print("You can select from easy, medium or hard\n")
    time.sleep(1)
    print("Select your difficulty by pressing 1,2 or 3 and then enter\n")
    time.sleep(1)
    print("1 = Easy , 2 = Medium, 3 = Hard\n")
    time.sleep(1)

    try:
        users_difficulty = int(input("My choice is: \n"))
        time.sleep(1)
        if users_difficulty not in range(1, 4):
            raise ValueError(f"You must choose either 1,2 or 3. You provided {users_difficulty}\n")
    except ValueError as error:
        print(f"Invalid data: {error}, please try again.\n")
    else:
        if users_difficulty == 1:
            users_difficulty == easy_questions
            print("You have chosen an easy difficulty level\n")
        elif users_difficulty == 2:
            users_difficulty == medium_questions
            print("You have chosen an medium difficulty level\n")
        else:
            users_difficulty == hard_questions
            print("You have chosen an hard difficulty level\n")
        return users_difficulty
        

def target_score():
    """
    Get user's target score out of 10. Run a while loop to collect the
    players guess of their correct answer target, via the terminal which
    has to be a number between 1 and 10. The loop will repeat until a
    number between 1 and 10 is entered.
    """
    while True:
        print("The quiz contains " + str(total_questions) + " questions.\n")
        print("What is your target score?\n")
        time.sleep(2)
        try:
            users_goal = int(input("My goal is: \n"))
            time.sleep(1)
            if users_goal not in range(1, 11):
                raise ValueError(f"Your target must be between 1 and 10. You provided {users_goal}\n")
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")
        else:
            if users_goal <= 5:
                print(f" {users_goal} is quite a low target, you should get more than that!\n")
            else:
                print(f"Challenging target! Best of luck trying to beat {users_goal}!\n")
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
                if answer == current_answer:
                    print(f"Good answer, {current_answer} was correct!")
                else:
                    print(f"The answer {current_answer} was incorrect")
                print(f"Your current score is {score} \n")
                time.sleep(2)
                break
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")


def display_results(users_goal):
    """
    Target score and actual score are compared and the results are returned
    """
    print(f"Your final score is {score}")
    time.sleep(2)

    if score > users_goal:
        print(f"Sadly, your target score was {users_goal} but you only got {score}.")
        time.sleep(1)
        print("You are not as clever as you think")
    elif score == users_goal:
        print(f"Well done! Your target score was {users_goal} and you matched that it!")
        time.sleep(1)
        print("You are exactly as clever as you think you are!")
    else:
        print(f"Congratulations! Your target was {users_goal} but you scored {score}!")
        time.sleep(1)
        print("You are much smarter than you think you are!")

    print("Scores are being saved to the history books")
    saves_worksheet = SHEET.worksheet("results")
    data = [USERNAME, score]
    saves_worksheet.append_row(data)

    print("Thank you for playing \n\n ")
    print("(Dan Roberts 2023)")


def initialise_questions(users_difficulty):
    global questions_list
    questions_list = users_difficulty.get_values()


def main():
    global question_index
    global score
    initialise_questions(users_difficulty)
    welcome_screen()
    get_player_name()
    users_difficulty()
    users_goal = target_score()
    while question_index < total_questions:
        ask_question()
        save_answer()
        question_index += 1
    display_results(users_goal)


main()
