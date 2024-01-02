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


def get_player_name():
    """
    Get username from the user. A while loop with a true check to
    stop users entering a blank name
    """
    while True:
        username = input("Please enter your name: ")
        if username.strip():
            break
        print("Name cannot be empt. Please enter your name")

    time.sleep(2)
    print(f"Welcome {username}!")
    time.sleep(2)
    return username


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
            users_goal = int(input("My goal is: "))
            time.sleep(1)
            if users_goal not in range(1, 11):
                raise ValueError(f"Your target must be between 1 and 10. You provided {users_goal}")
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")
        else:
            if users_goal <= 5:
                print(f" {users_goal} is quite a low target, you should get more than that!")
            else:
                print(f"Challenging target! Best of luck trying to beat {users_goal}!")
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
        score = final_score
        return final_score


def display_results(users_goal, final_score):
    """
    Target score and actual score are compared and the results are returned
    """
    print(f"Your final score is {final_score}")
    time.sleep(2)

    if final_score > users_goal:
        print(f"Sadly, your target score was {users_goal} but you only got {final_score}.")
        time.sleep(1)
        print("You are not as clever as you think")
    elif final_score == users_goal:
        print(f"Well done! Your target score was {users_goal} and you matched that it!")
        time.sleep(1)
        print("You are exactly as clever as you think you are!")
    else:
        print(f"Congratulations! Your target was {users_goal} but you scored {final_score}!")
        time.sleep(1)
        print("You are much smarter than you think you are!")


def initialise_questions():
    global questions_list
    questions_list = questions.get_values()


def save_scores(username, final_score):
    """
    Name and score from quiz are saved if quiz is completed. It is stored in the
    connected worksheet in the part called "results"
    """
    print("Scores are being saved to the history books")
    saves_worksheet = SHEET.worksheet("results")
    name = {username}
    data = [name, final_score]
    saves_worksheet.append_row(data)


def main():
    global question_index
    global score
    initialise_questions()
    welcome_screen()
    get_player_name()
    users_goal = target_score()
    while question_index < total_questions:
        ask_question()
        save_answer()
        question_index += 1
    display_results(users_goal, final_score)
    print("Your final score was...")
    time.sleep(3)
    print(f"...{score}")
    save_scores(name, final_score)
    print("Thank you for playing \n\n ")
    print("(Dan Roberts 2023)")


main()
