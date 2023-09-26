enter_score = input("Enter Score: ")
try:
    score = int(enter_score)
    if 0 <= score <= 100:
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        print("Grade is", grade)
    else:
        print("Error, please enter a numeric input between 0 and 100")
except ValueError:
    print("Error, please enter a valid numeric input")
