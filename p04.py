def p04():
    with open("data_day02.txt") as file:
        command_list = [line.split() for line in file]
    
    aim = 0
    horizontal_position = 0
    depth = 0

    for command in command_list:
        word = command[0]
        amount = int(command[1])
        if word == "forward":
            horizontal_position += amount
            depth += aim * amount
        elif word == "down":
            aim += amount
        elif word == "up":
            aim -= amount

    return horizontal_position * depth

if __name__ == '__main__':
    print(p04())
