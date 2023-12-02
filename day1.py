import sys

def part1(data):
    return sum((int(digits[0]) * 10 + int(digits[-1]) for digits in ([i for i in line if i.isdigit()] for line in data) if len(digits) > 0))

def part2(data):
    mappings = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    return part1([[x if (x := "".join([v for k, v in mappings.items() if line[i:].startswith(k)])) else line[i] for i in range(len(line))] for line in data])

def execute(file_path):
    print("Answer 1: ", part1(open(file_path, 'r')))
    print("Answer 2: ", part2(open(file_path, 'r')))

print("EXAMPLE")
execute('./data/'+sys.argv[0].split(".py")[0]+'/example.txt')

print("SOLUTION")
execute('./data/'+sys.argv[0].split(".py")[0]+'/data.txt')
