def part1(text: list[str]):
    xmas_count = 0
    COLUMN = len(text[0])
    ROW = len(text)
    for i in range(0, ROW):
        for j in range(0, COLUMN):
            if text[i][j] == "X":
                if i + 3 <= ROW - 1:
                    if (
                        text[i + 1][j] == "M"
                        and text[i + 2][j] == "A"
                        and text[i + 3][j] == "S"
                    ):
                        xmas_count += 1

                if j + 3 <= COLUMN - 1:
                    if text[i][j + 1 : j + 4] == "MAS":
                        xmas_count += 1

                if i + 3 <= ROW - 1 and j + 3 <= COLUMN - 1:
                    if (
                        text[i + 1][j + 1] == "M"
                        and text[i + 2][j + 2] == "A"
                        and text[i + 3][j + 3] == "S"
                    ):
                        xmas_count += 1

                if i + 3 <= ROW - 1 and j - 3 >= 0:
                    if (
                        text[i + 1][j - 1] == "M"
                        and text[i + 2][j - 2] == "A"
                        and text[i + 3][j - 3] == "S"
                    ):
                        xmas_count += 1

            if text[i][j] == "S":
                if i + 3 <= ROW - 1:
                    if (
                        text[i + 1][j] == "A"
                        and text[i + 2][j] == "M"
                        and text[i + 3][j] == "X"
                    ):
                        xmas_count += 1

                if j + 3 <= COLUMN - 1:
                    if text[i][j + 1 : j + 4] == "AMX":
                        xmas_count += 1

                if i + 3 <= ROW - 1 and j + 3 <= COLUMN - 1:
                    if (
                        text[i + 1][j + 1] == "A"
                        and text[i + 2][j + 2] == "M"
                        and text[i + 3][j + 3] == "X"
                    ):
                        xmas_count += 1
                if i + 3 <= ROW - 1 and j - 3 >= 0:
                    if (
                        text[i + 1][j - 1] == "A"
                        and text[i + 2][j - 2] == "M"
                        and text[i + 3][j - 3] == "X"
                    ):
                        xmas_count += 1
    print(xmas_count)


def part2(text: list[str]):
    xmas_count = 0
    COLUMN = len(text[0])
    ROW = len(text)
    for i in range(1, ROW - 1):
        for j in range(1, COLUMN - 1):
            if text[i][j] == "A":
                if (
                    text[i - 1][j - 1] == "M"
                    and text[i - 1][j + 1] == "S"
                    and text[i + 1][j - 1] == "M"
                    and text[i + 1][j + 1] == "S"
                ):
                    xmas_count += 1

                if (
                    text[i - 1][j - 1] == "S"
                    and text[i - 1][j + 1] == "M"
                    and text[i + 1][j - 1] == "S"
                    and text[i + 1][j + 1] == "M"
                ):
                    xmas_count += 1
                if (
                    text[i - 1][j - 1] == "S"
                    and text[i - 1][j + 1] == "S"
                    and text[i + 1][j - 1] == "M"
                    and text[i + 1][j + 1] == "M"
                ):
                    xmas_count += 1
                if (
                    text[i - 1][j - 1] == "M"
                    and text[i - 1][j + 1] == "M"
                    and text[i + 1][j - 1] == "S"
                    and text[i + 1][j + 1] == "S"
                ):
                    xmas_count += 1

    print(xmas_count)


if __name__ == "__main__":
    text: list[str] = []
    with open("2024/day4/input.txt") as file:
        for line in file:
            text.append(line)
    part1(text)
    part2(text)
