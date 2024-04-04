import random

def generate_equation():
    # Generate random numbers and an operator to create a simple equation
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        # Round division answers to 2 decimal places
        answer = num1 / num2
        answer = round(answer, 2)
    return f"{num1} {operator} {num2} =", answer

def generate_test(num_questions):
    # Generate a list of questions by calling generate_equation() num_questions times
    questions = []
    for _ in range(num_questions):
        question, answer = generate_equation()
        questions.append((question, answer))
    return questions

def main():
    num_questions = 10
    # Generate a test with 10 questions
    questions = generate_test(num_questions)
    score = 0
    for i, (question, answer) in enumerate(questions, start=1):
        # Ask each question and get the user's answer
        user_answer = input(f"Question {i}: {question} ")
        try:
            user_answer = float(user_answer)
        except ValueError:
            # Handle invalid input
            print("Invalid input. Please enter a number.")
            continue
        # Check if the user's answer is correct
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            # Display the correct answer for incorrect responses
            print(f"Incorrect. The correct answer is {answer}")
    # Display the final score
    print(f"You scored {score} out of {num_questions}")

if __name__ == "__main__":
    main()

def main():
    num_questions = 10
    questions = generate_test(num_questions)
    score = 0
    for i, (question, answer) in enumerate(questions, start=1):
        while True:
            user_answer = input(f"Question {i}: {question} ")
            try:
                user_answer = float(user_answer)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if user_answer == answer:
                print("Correct!")
                score += 1
                break  # Exit the loop if the answer is correct
            else:
                print("Incorrect. Please try again.")
    print(f"You scored {score} out of {num_questions}")

if __name__ == "__main__":
    main()