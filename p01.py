def p01():
    with open("data_day01.txt") as data_file:
        data = data_file.read().splitlines()
    
    increase_count = 0
    previous_value = 1e10
    for value_str in data:
        value = int(value_str)
        if value > previous_value:
            increase_count += 1
        previous_value = value
    
    return increase_count

if __name__ == '__main__':
    print(p01())