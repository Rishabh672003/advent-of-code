import itertools
import numpy as np

def part1(lists: list[tuple[int, list[int]]]):
    count = 0
    for res, numbers in lists:
        numbers = np.array(numbers)
        num_ops = len(numbers) - 1
        total_combinations = 2 ** num_ops

        # Generate all possible operator combinations (0: '+', 1: '*')
        operator_codes = np.array(list(itertools.product([0, 1], repeat=num_ops)), dtype=np.int8)

        # Initialize results array
        results = np.full(total_combinations, numbers[0], dtype=np.int64)

        for i in range(num_ops):
            op_codes = operator_codes[:, i]
            next_number = numbers[i + 1]

            # Apply operation based on operator code
            results = np.where(
                op_codes == 0,
                results + next_number,
                results * next_number
            )

        # Check if any result matches the target
        if np.any(results == res):
            count += res

    print(count)

def part2(lists: list[tuple[int, list[int]]]):
    count = 0
    for res, numbers in lists:
        numbers = np.array(numbers, dtype=object)
        num_ops = len(numbers) - 1
        total_combinations = 3 ** num_ops

        # Generate all possible operator combinations (0: '+', 1: '*', 2: '||')
        operator_codes = np.array(list(itertools.product([0, 1, 2], repeat=num_ops)), dtype=np.int8)

        # Initialize results array
        results = np.full(total_combinations, numbers[0], dtype=object)

        for i in range(num_ops):
            op_codes = operator_codes[:, i]
            next_number = numbers[i + 1]

            # Apply addition
            add_mask = op_codes == 0
            results[add_mask] = results[add_mask] + next_number

            # Apply multiplication
            mul_mask = op_codes == 1
            results[mul_mask] = results[mul_mask] * next_number

            # Apply concatenation
            concat_mask = op_codes == 2
            results[concat_mask] = results[concat_mask].astype(str) + str(next_number)
            results[concat_mask] = results[concat_mask].astype(int)

        # Convert results to integers for comparison
        final_results = results.astype(int)

        # Check if any result matches the target
        if np.any(final_results == res):
            count += res

    print(count)

if __name__ == "__main__":
    lines: list[tuple[int, np.ndarray]] = []
    with open("2024/day7/input.txt") as file:
        for i in file:
            a, b = i.split(":", 2)
            lines.append((int(a), list(map(int, b.split()))))
    part1(lines)
    part2(lines)
