total = 0
count = 0
while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input == "done":
        break
    try:
        number = float(user_input)
        total += number
        count += 1
    except ValueError:
        print("Invalid input. Enter a number.")
if count > 0:
    average = total / count
    print("Sum of input numbers:", total)
    print("Number of input values:", count)
    print("Average of input numbers:", average)
else:
    print("No numbers entered.")
