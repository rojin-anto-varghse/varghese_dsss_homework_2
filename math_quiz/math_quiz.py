import random


def integer_range(min, max):
    """
    Generate a random integer within a specified range.

    Parameters:
        min_value (int) is the minimum value in the range.
        max_value (int) is the maximum value in the range.

    Returns:
        int is a random integer between min_value and max_value.
    """
    return random.randint(int(min), int(max))


def arithmetic_operator():
    """"
     Randomly select an arithmetic operator.

    Returns:
        str is a randomly selected operator.
    """
    return random.choice(['+', '-', '*'])


def numbers(n1, n2, operator):
    """"
    it generate a math equation and compute the answer based on given numbers and operator.

    Parameters:
        n1 (int) is the first operand.
        n2 (int) is the second operand.
        operator (str) is the arithmetic operator ('+', '-', or '*').

    Returns:
        A tuple containing the formatted equation as a string and the calculated answer as an integer.
    """
    equation = f"{n1} {operator} {n2}"
    if operator == '+': answer = n1 + n2
    elif operator == '-': answer = n1 - n2
    else: answer = n1 * n2
    return equation, answer

def math_quiz():
    """"
    Run a math quiz game that presents random math problems to the user.

    The game asks three questions (based on the value of pi), and the user earns a point for each correct answer.
    At the end of the game, the total score is displayed.
    """
    mark = 0
    pi = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    # Loop through each question
    for _ in range(int(pi)):
        # it helps in generate random numbers and operator for the question
        try:
            n1 = integer_range(1, 10)
            n2 = integer_range(1, 5.5)
            operator = arithmetic_operator()

            # Create a problem and get the correct answer
            PROBLEM, ANSWER = numbers(n1, n2, operator)
            print(f"\nQuestion: {PROBLEM}")

            # Get and validate user input
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
            # Skip to the next question if input is invalid

        except ValueError:
            print("Invalid input! Please enter a valid integer.")  # Error message for non-integer input

            # Check if the answer is correct
            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                mark += -(-1)
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")



    # Display the final score
    print(f"\nGame over! Your score is: {mark}/{int(pi)}")

if __name__ == "__main__":
    math_quiz()
