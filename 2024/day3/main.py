import re


def part1(text: str):
    print(sum([int(i.group(1)) * int(i.group(2)) for i in re.finditer(r"mul\((\d+)\,(\d+)\)", text)]))


def part2(text: str):
    res = 0
    pat = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(?:do\(\))|(?:don't\(\))")
    ans = re.finditer(pat, text)

    track = True
    for i in ans:
        if i.group() == "do()":
            track = True
        elif i.group() == "don't()":
            track = False
        elif track:
            res += int(i.group(1)) * int(i.group(2))

    print(res)


if __name__ == "__main__":
    with open("2024/day3/input.txt") as file:
        text = file.read().strip()
    part1(text)
    part2(text)
