# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.

with open("questions.txt", "r") as file:
    score = 0
    qs = 0
    for line in file:
        if line.startswith("Answer"):
            qs += 1
            finished = False
            while not finished:
                answer = input("What is the answer? (type 'A', 'B', 'C', or 'D'): ")
                if answer != 'A' and answer != 'B' and answer != 'C' and answer != 'D':
                    print("Please type either 'A', 'B', 'C', or 'D' for the answer")
                else:
                    if answer == line[-2]:
                        score += 1
                        print("Correct!")
                        print("Here is your score: " + str(score))
                    elif answer != line[-2]:
                        print("Wrong! The correct answer is: " + str(line[-2]))
                        print("Here is your score: " + str(score))
                    finished = True
        else:
            print(line.rstrip())
    print("You have finished the quiz!")
    print("You scored " + str(score) + " out of " + str(qs) + ".")

