def p03():
    with open("data_day02.txt") as file:
        command_list = [line.split() for line in file]
    
    movements = {
        "forward": 0,
        "down": 0,
        "up" :0,
    }

    for command in command_list:
        movements[command[0]] += int(command[1])

    return movements["forward"] * (movements["down"] - movements["up"])

if __name__ == '__main__':
    print(p03())
