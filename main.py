from random import randint

def get_file_lines(filename):
    with open(filename, "r") as outfile:
        lines = outfile.readlines()
    return lines

poem = get_file_lines("cs1.0/poetry-slam/poem.txt")

def lines_printed_backwards(lines_list):
    lineNum = len(lines_list)
    for line in reversed(lines_list):
        print(lineNum, line, end=' ')
        lineNum -= 1

#lines_printed_backwards(poem)

def lines_printed_random(lines_list):
    lastIndex = len(lines_list)-1
    for line in lines_list:
        randomIndex = randint(1, lastIndex)
        print(lines_list[randomIndex], end=' ')

lines_printed_random(poem)