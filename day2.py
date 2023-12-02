import sys
from collections import defaultdict 

target = defaultdict(int, {'red': 12, 'green': 13, 'blue': 14})

def parse(data):
    result = []
    for line in data:
        _, result_str = line.strip().split(': ')
        max_numbers = defaultdict(int, {'red': 0, 'green': 0, 'blue': 0})
        for game_result in result_str.split("; "):
            for r in game_result.split(", "):
                num, color = r.split(' ')
                if(max_numbers[color] < int(num)):
                    max_numbers[color] = int(num)
        result.append(max_numbers)
    return result


def part1(data):
    result = 0
    max_result_list = parse(data)
    for index, max_result in enumerate(max_result_list):
        is_valid = True
        for _, color in enumerate(max_result):
            if(target[color] < max_result[color]):
                is_valid = False
        if is_valid:
            result += index + 1
    return result

def part2(data):
    result = 0
    max_result_list = parse(data)
    for index, max_result in enumerate(max_result_list):
        power = 1
        for _, color in enumerate(max_result):
            power *= max_result[color]
        result += power
    return result

def execute(file_path):
    total_sum1 = 0
    total_sum2 = 0  
    with open(file_path, 'r') as file:
        total_sum1 = part1(file)

    with open(file_path, 'r') as file:
        total_sum2 = part2(file)

    print("Answer 1: ", total_sum1)
    print("Answer 2: ", total_sum2)


filePath = sys.argv[0].split(".py")[0]

print("EXAMPLE")
execute('./data/'+filePath+'/example.txt')

print("SOLUTION")
execute('./data/'+filePath+'/data.txt')
