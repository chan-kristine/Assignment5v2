import math
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

def letter():
    quest_ = input("Is your grade INC, W, or D? Please enter Yes or No: ")
    if quest_ == "Yes":
        t_grade = input("Please enter if your grade is INC, W, or D: ") 
        return t_grade
    else:
        if quest_ == "No":
            grade = float(input(("Enter your grade here: ")))
            grade_ = round_half_up(grade)
            return grade_

def mark():
    if your_mark == "INC":
        print("Your status on this subject is INCOMPLETE.")
    elif your_mark == "W":
        print("Your status on this subject is WITHDRAWN")
    elif your_mark == "D":
        print("Your status is DROPPED")
    elif your_mark >= 97 and your_mark <= 100:
        print("Excellent!")
        print("Your mark is 1.0!")
    elif your_mark >= 94 and your_mark <= 96:
        print("Excellent!")
        print("Your mark is 1.25!")
    elif your_mark >= 91 and  your_mark <= 93:
        print("Very Good!")
        print("Your mark is 1.5!")
    elif your_mark >= 88 and your_mark <= 90:
        print("Very Good!")
        print("Your mark is 1.75!")
    elif your_mark >= 85 and your_mark <= 87:
        print("Good!")
        print("Your mark is 2.0!")
    elif your_mark >= 82 and your_mark <= 84:
        print("Good!")
        print("Your mark is 2.25!")
    elif your_mark >= 79 and your_mark <= 81:
        print("Satisfactory!")
        print("Your mark is 2.50!")
    elif your_mark >= 76 and your_mark <= 78:
        print("Satisfactory!")
        print("Your mark is 2.75!")
    elif your_mark == 75:
        print("Passing!")
        print("Your mark is 3.0!")
    elif your_mark >= 65 and your_mark <= 74:
        print("Failure!")
        print("Your mark is 5.0!")


your_mark = letter()
Mark= mark()

print("Your grade is recorded!")