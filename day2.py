import sys
from collections import defaultdict 
from functools import reduce

target = defaultdict(int, {'red': 12, 'green': 13, 'blue': 14})

def parse(data):
    return [{color: max(int(num) if color == c else 0 for game_result in line.strip().split(': ')[-1].split("; ") for num, c in (r.split(' ') for r in game_result.split(", "))) for color in ['red', 'green', 'blue']} for line in data]


def part1(data):
    return sum(index + 1 for index, max_result in enumerate(parse(data)) if all(target[color] >= max_result[color] for color in max_result))

def part2(data):
    return sum(reduce(lambda x, y: x * y, (num for _ ,num in max_result.items())) for max_result in parse(data))

def execute(file_path):
    print("Answer 1: ", part1(open(file_path, 'r')))
    print("Answer 2: ", part2(open(file_path, 'r')))

print("EXAMPLE")
execute('./data/'+sys.argv[0].split(".py")[0]+'/example.txt')

print("SOLUTION")
execute('./data/'+sys.argv[0].split(".py")[0]+'/data.txt')
