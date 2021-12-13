def p05():
    index_digit_counts = [[0, 0] for _ in range(0, 12)]
    with open("data_day03.txt") as file:
        for line in file.read().splitlines():
            for index, digit in enumerate(line):
                index_digit_counts[index][int(digit)] += 1

    gamma_rate = 0
    epsilon_rate = 0
    for digit_counts in index_digit_counts:
        gamma_rate *= 2
        epsilon_rate *= 2
        if digit_counts[1] > digit_counts[0]:
            gamma_rate += 1
        else:
            epsilon_rate += 1

    return gamma_rate * epsilon_rate

if __name__ == "__main__":
    print(p05())