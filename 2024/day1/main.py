from typing import Counter


text1: list[int] = []
text2: list[int] = []

with open("input.txt") as file:
    for line in file:
        text1.append(int(line.split()[0]))
        text2.append(int(line.split()[1]))

def part1():
    text1.sort()
    text2.sort()

    res = 0

    for (i, j) in zip(text1, text2):
        res += abs(i - j)

    # print(res)
    print(sum([abs(x - y) for x, y in zip(sorted(text1), sorted(text2))]))

def part2():
    num_freq_2 = Counter(text2)

    res = 0

    for i in text1:
        if i in text2:
            res += (i * num_freq_2[i])
    print(res)
    print(sum([i * text2.count(i) for i in text1]))
    

# part1()
part2()
