from random import randint
from random import choice

#function turns .txt file lines into a list of strings
def get_file_lines(filename):
    with open(filename, "r") as outfile:
        lines = outfile.readlines()
    return lines

#assigns poem.txt into variable poem using get_file_lines function
poem = get_file_lines("cs1.0/poetry-slam/poem.txt")

#function prints out poem in reverse order
def lines_printed_backwards(lines_list):
    lineNum = len(lines_list)
    for line in reversed(lines_list):
        print(lineNum, line, end=' ')
        lineNum -= 1

#function prints out poem in a random order
def lines_printed_random(lines_list):
    lastIndex = len(lines_list)-1
    for line in lines_list:
        randomIndex = randint(0, lastIndex)
        print(lines_list[randomIndex], end=' ')

#helper function to randomly generate an interruption phrase
def get_interruption():
    #list of possible interruption phrases
    random_interruption = ['*cough* *cough*', '--> easter egg <--', '--Take a 10 min break--',
                            "--Don't forget to stand up and stretch!--", '*clears throat*',
                            '--Drink Pepsi!--', '--> click here for free iphone 11 <--']
    #returns a random interruption phrase
    return choice(random_interruption)

#fuction prints out poem with a chance to print out random interruption phrases
def lines_printed_custom(lines_list):
    for line in lines_list:
        #prints out poem normally
        print(line, end=' ')

        #generates a random number each loop between 0 and 9 and assigns it to variable chaosNum
        chaosNum = randint(0,10)
        #if chaosNum == 0, calls helper function for an interruption phrase
        if chaosNum == 0:
            print(get_interruption())

#calling functions with new lines in between each call
lines_printed_backwards(poem)
print()
lines_printed_random(poem)
print()
lines_printed_custom(poem)