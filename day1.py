file_path = './data/day1.txt'
# file_path = './data/example1.txt'

def part1(data):
    _sum = 0
    for line in data:
        digits = [int(i) for i in line if i.isdigit()]
        _sum += digits[0] * 10 + digits[-1]
    return _sum

def part2(data):
    mappings = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    new_data = [[x if (x := "".join([v for k, v in mappings.items() if line[i:].startswith(k)])) else line[i] for i in range(len(line))] for line in data]
    return part1(new_data)

total_sum1 = 0
total_sum2 = 0

with open(file_path, 'r') as file:
    total_sum1 = part1(file)

with open(file_path, 'r') as file:
    total_sum2 = part2(file)

print("Answer 1: ", total_sum1)
print("Answer 2: ", total_sum2)

