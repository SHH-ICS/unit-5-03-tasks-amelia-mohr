# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.

finished = False
while not finished:
    f = open("questions.txt")
    score = 0
    for line in f:
        p
        if line.startswith("Answer:"):
            answered = False
            while not answered:
                answer = input("What is the answer? (type 'A', 'B', 'C', or 'D'): ")
                if answer != 'A' and answer != 'B' and answer != 'C' and answer != 'D':
                    print("Please type either 'A', 'B', 'C', or 'D' for the answer") 
                else:
                    if answer == line[-2]:
                        score += 1
                        print("Correct!")
                        print("Here is your score: " + str(score))
                    else:
                        print("Wrong! The correct answer is" + str(line[-1]))
                        print("Here is your score: " + str(score))
                    

