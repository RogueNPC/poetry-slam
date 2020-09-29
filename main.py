
def get_file_lines(filename):
    with open(filename, "r") as outfile:
        lines = outfile.readlines()
    return lines

poem = get_file_lines("cs1.0/poetry-slam/poem.txt")

def lines_printed_backwards(lines_list):
    line_num = len(lines_list)
    for line in reversed(lines_list):
        print(line_num, line, end=' ')
        line_num -= 1

lines_printed_backwards(poem)