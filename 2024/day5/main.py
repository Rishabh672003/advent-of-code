from collections import defaultdict

wrong_updates: list[list[int]] = []


def part1(rules: list[list[int]], updates: list[list[int]]):
    next_map: dict[int, set[int]] = defaultdict(set[int])
    for i in rules:
        a, b = i
        next_map[a].add(b)
        if b not in next_map:
            next_map[b] = set()

    safe_middle: list[int] = []
    for update in updates:
        exit_loop = False
        for index, element in enumerate(update):
            if exit_loop:
                break
            for i in range(index + 1, len(update)):
                if update[i] in next_map[element]:
                    continue
                else:
                    safe_middle.append(update[len(update) // 2])
                    wrong_updates.append(update)
                    exit_loop = True
                    break
    rest_sum = 0
    for update in updates:
        rest_sum += update[len(update) // 2]

    print(rest_sum - sum(safe_middle))


def part2(rules: list[list[int]], updates: list[list[int]]):
    next_map: dict[int, set[int]] = defaultdict(set[int])
    for i in rules:
        a, b = i
        next_map[a].add(b)
        if b not in next_map:
            next_map[b] = set()

    for update in updates:
        for i in range(len(update)):
            for j in range(1, len(update)):
                if update[j] not in next_map:
                    continue
                if update[j - 1] in next_map[update[j]]:
                    update[j], update[j - 1] = update[j - 1], update[j]

    res = 0
    for update in updates:
        res += update[len(update) // 2]
    print(res)


if __name__ == "__main__":
    rules: list[list[int]] = []
    updates: list[list[int]] = []
    with open("2024/day5/input.txt") as file:
        for i in file:
            if "|" in i.strip():
                rules.append(list(map(int, i.strip().split("|"))))
            elif "," in i.strip():
                updates.append(list(map(int, i.strip().split(","))))

    part1(rules, updates)
    part2(rules, wrong_updates)
