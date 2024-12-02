def part1(text: list[list[int]]):
    no_of_safe = 0
    for line in text:
        diffs: list[int] = [line[i] - line[i - 1] for i in range(1, len(line))]
        if all(d > 0 and d <= 3 for d in diffs):
            no_of_safe += 1
        elif all(d < 0 and d >= -3 for d in diffs):
            no_of_safe += 1
    return no_of_safe


def part2(text: list[list[int]]):
    no_of_safe = 0
    for line in text:
        diffs: list[int] = [line[i] - line[i - 1] for i in range(1, len(line))]
        if all(d > 0 and d <= 3 for d in diffs):
            no_of_safe += 1
            text.remove(line)
        elif all(d < 0 and d >= -3 for d in diffs):
            no_of_safe += 1
            text.remove(line)

    for line in text:
        for i, curr in enumerate(line):
            del line[i]
            diffs2: list[int] = [line[i] - line[i - 1] for i in range(1, len(line))]
            if all(d > 0 and d <= 3 for d in diffs2):
                no_of_safe += 1
                break
            elif all(d < 0 and d >= -3 for d in diffs2):
                no_of_safe += 1
                break
            else:
                line.insert(i, curr)

    return no_of_safe


if __name__ == "__main__":
    text: list[list[int]] = []
    with open("input.txt") as file:
        for line in file:
            text.append(list(map(int, line.split())))

    print(part1(text))
    print(part2(text))
