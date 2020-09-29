
def get_file_lines(filename):
    with open(filename, "r") as outfile:
        lines = outfile.readlines()
    return lines

get_file_lines('poem.txt')