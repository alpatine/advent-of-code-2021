def p06():
    with open("data_day03.txt") as file:
        data = file.read().splitlines()

    oxygen_rating = calculate_rating(data, lambda digit_sum, entry_count : (digit_sum * 2) // entry_count)
    scrubber_rating = calculate_rating(data, lambda digit_sum, entry_count : 1 - ((digit_sum * 2) // entry_count))

    return oxygen_rating * scrubber_rating

def calculate_rating(candidates, value_to_keep_calculation):
    for position in range(0, len(candidates)):
        entry_count = len(candidates)
        if entry_count <= 1:
            break
        digit_sum = sum(int(entry[position]) for entry in candidates)
        value_to_keep = value_to_keep_calculation(digit_sum, entry_count)
        candidates = [candidate for candidate in candidates if candidate[position] == str(value_to_keep)]
    return int(candidates[0], 2)

if __name__ == "__main__":
    print(p06())
