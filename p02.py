def p02():
    with open("data_day01.txt") as data_file:
        data_str = data_file.read().splitlines()

    data = [int(value) for value in data_str]
    
    # calculate the sliding window sums
    window_size = 3
    window_start_max = len(data) - window_size
    window_sums = [sum(data[window_start:window_start+window_size]) 
                   for window_start in range(0, window_start_max + 1)]
    
    # calculate how many window sums are bigger than the previous window sum
    increase_count = 0
    previous_value = 1e10
    for value in window_sums:
        if value > previous_value:
            increase_count += 1
        previous_value = value
    
    return increase_count

if __name__ == "__main__":
    print(p02())