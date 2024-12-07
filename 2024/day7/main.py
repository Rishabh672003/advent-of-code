import itertools


def part1(lists: list[tuple[int, list[int]]]):
    operators = ["+", "*"]
    count = 0
    for res, numbers in lists:
        op_combinations = list(itertools.product(operators, repeat=len(numbers) - 1))

        for ops in op_combinations:
            expression = " ".join(
                str(numbers[i]) + " " + ops[i] if i < len(ops) else str(numbers[i])
                for i in range(len(numbers))
            )
            tokens = expression.split()
            result = int(tokens[0])
            for i in range(1, len(tokens), 2):
                operator = tokens[i]
                number = int(tokens[i + 1])
                if operator == "*":
                    result *= number
                else:
                    result += number
            if result == res:
                count += res
                break

    print(count)


def part2(lists: list[tuple[int, list[int]]]):
    operators = ["+", "*", "||"]
    count = 0
    for res, numbers in lists:
        op_combinations = list(itertools.product(operators, repeat=len(numbers) - 1))

        for ops in op_combinations:
            expression = " ".join(
                str(numbers[i]) + " " + ops[i] if i < len(ops) else str(numbers[i])
                for i in range(len(numbers))
            )
            tokens = expression.split()
            result = int(tokens[0])
            for i in range(1, len(tokens), 2):
                operator = tokens[i]
                number = int(tokens[i + 1])
                if result == res or result > res:
                    break
                if operator == "*":
                    result *= number
                elif operator == "+":
                    result += number
                elif operator == "||":
                    result = int(str(result) + str(number))
            if result == res:
                count+=res
                break

    print(count)


if __name__ == "__main__":
    lines: list[tuple[int, list[int]]] = []
    with open("2024/day7/input.txt") as file:
        for i in file:
            a, b = i.split(":", 2)
            lines.append((int(a), list(map(int, b.split()))))
    part1(lines)
    part2(lines)
