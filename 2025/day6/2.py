"""
--- Part Two ---
The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:

123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
Reading the problems right-to-left one column at a time, the problems are now quite different:

The rightmost problem is 4 + 431 + 623 = 1058
The second problem from the right is 175 * 581 * 32 = 3253600
The third problem from the right is 8 + 248 + 369 = 625
Finally, the leftmost problem is 356 * 24 * 1 = 8544
Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?

Your puzzle answer was 9695042567249.


"""

from math import prod

with open("input.txt", "r") as f:
    lines = [line.rstrip("\n") for line in f.readlines()]

    max_col = max(len(line) for line in lines)
    rows = len(lines)
    result = 0

    # Helper: check if column is all spaces
    def is_separator(col):
        return all(col >= len(lines[r]) or lines[r][col] == " " for r in range(rows))

    # Helper: read number from column (top to bottom)
    def read_number(col):
        digits = [
            lines[r][col]
            for r in range(rows - 1)
            if col < len(lines[r]) and lines[r][col].isdigit()
        ]
        return int("".join(digits)) if digits else None

    # Process columns right to left
    col = max_col - 1
    while col >= 0:
        if is_separator(col):
            col -= 1
            continue

        # Collect all columns in this problem and find operator
        problem_cols = []
        operator = None

        while col >= 0 and not is_separator(col):
            problem_cols.append(col)
            # Check for operator in last row
            if col < len(lines[rows - 1]):
                op = lines[rows - 1][col].strip()
                if op in "*+":
                    operator = op
            col -= 1

        if operator and problem_cols:
            # Read numbers from each column (rightmost first)
            numbers = [read_number(c) for c in reversed(problem_cols)]
            numbers = [n for n in numbers if n is not None]

            # Calculate problem result
            if numbers:
                problem_result = prod(numbers) if operator == "*" else sum(numbers)
                result += problem_result

    print(result)
