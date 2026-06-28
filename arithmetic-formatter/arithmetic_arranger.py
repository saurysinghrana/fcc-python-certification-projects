"""
Arithmetic Formatter

Formats arithmetic problems vertically as required by the
freeCodeCamp Scientific Computing with Python certification project.
"""


def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        parts = problem.split()
        num1 = parts[0]
        operator = parts[1]
        num2 = parts[2]

        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Format the first line
        width = max(len(num1), len(num2)) + 2
        top = " " * (width - len(num1)) + num1

        # Format the second line
        bottom = operator + " " * (width - len(num2) - 1) + num2

        # Separator line
        dash = "-" * width

        # Calculate and format the answer
        if operator == "+":
            result = str(int(num1) + int(num2))
        else:
            result = str(int(num1) - int(num2))

        answer = " " * (width - len(result)) + result

        first_line.append(top)
        second_line.append(bottom)
        dash_line.append(dash)
        answer_line.append(answer)

    arranged_problems = "    ".join(first_line)
    arranged_problems += "\n"
    arranged_problems += "    ".join(second_line)
    arranged_problems += "\n"
    arranged_problems += "    ".join(dash_line)

    if show_answers:
        arranged_problems += "\n"
        arranged_problems += "    ".join(answer_line)

    return arranged_problems


if __name__ == "__main__":
    print(
        arithmetic_arranger(
            ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],
            True,
        )
    )