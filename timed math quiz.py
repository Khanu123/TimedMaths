import operator
import random
import time


OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem(min_operand=MIN_OPERAND, max_operand=MAX_OPERAND):
    """Return a safe arithmetic expression and its answer without using eval."""
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    symbol = random.choice(list(OPERATORS))
    answer = OPERATORS[symbol](left, right)
    return f"{left} {symbol} {right}", answer


def ask_problem(problem_number, expression, answer, input_func=input):
    attempts = 0
    while True:
        guess = input_func(f"Problem #{problem_number}: {expression} = ").strip()
        attempts += 1
        if guess == str(answer):
            return attempts
        print("Incorrect, try again.")


def run_quiz(total_problems=TOTAL_PROBLEMS):
    wrong_attempts = 0
    input("Press enter to start!")
    print("----------------------")

    start_time = time.time()
    for i in range(total_problems):
        expression, answer = generate_problem()
        attempts = ask_problem(i + 1, expression, answer)
        wrong_attempts += attempts - 1

    total_time = round(time.time() - start_time, 2)
    print("----------------------")
    print(f"Nice work! You finished in {total_time} seconds.")
    print(f"Wrong attempts: {wrong_attempts}")


if __name__ == "__main__":
    run_quiz()
