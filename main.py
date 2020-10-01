from random import randint
from random import choice

#function turns .txt file lines into a list of strings
def get_file_lines(filename):
    with open(filename, "r") as outfile:
        lines = outfile.readlines()
    return lines

#assigns poem.txt into variable poem using get_file_lines function
poem = get_file_lines("cs1.0/poetry-slam/poem.txt")

#function prints out poem normally
def lines_printed_normal(lines_list):
    lineNum = 1
    for line in (lines_list):
        print(lineNum, line, end=' ')
        lineNum += 1

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
    random_interruption = ['*cough* *cough*', '--> easter egg <--', '--Remember to take breaks regularly--',
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

#while loop to let bot run until user inputs "done"
user_response = ''
while user_response != "done":
    #introduction
    print("\n Poetry Slam: Jabberwocky by Lewis Carroll")
    print("Please enter normal, backwards, random, or custom to print the poem in that way or enter done to exit.")
    #prompts user for an input
    user_response = input('Please enter a mode: ')

    #if statements to output specialized lines
    #prints out poem normally
    if user_response == "normal":
        lines_printed_normal(poem)

    #prints out poem backwards
    elif user_response == "backwards":
        lines_printed_backwards(poem)

    #prints out poem randomly
    elif user_response == "random":
        lines_printed_random(poem)

    #prints out poem using custom method
    elif user_response == "custom":
        lines_printed_custom(poem)

    #prints out exit message
    elif user_response == "done":
        print("Thank you, have a nice day!")

    #prints out error when entering invalid value
    else:
        print("You have input an invalid value, please try again.")