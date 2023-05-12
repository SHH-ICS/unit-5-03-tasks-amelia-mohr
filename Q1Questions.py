# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.

finished = False
qs = 0
while not finished:
    f = open("questions.txt", "a")
    question = input("To quit, type 'q' or write a multiple choice question: ")
    if question == 'q':
        f.close()
        finished = True
    else:
        a = input("What is the answer for choice A: ")
        b = input("What is the answer for choice B: ")
        c = input("What is the answer for choice C: ")
        d = input("What is the answer for choice D: ")
        done = False
        while not done:
            answer = input("What is the answer to your question (type 'A', 'B', 'C', or 'D'): ")
            if answer != 'A' and answer != 'B' and answer != 'C' and answer != 'D':
                print("Please type either 'A', 'B', 'C', or 'D' for the answer")
            else: 
                f.write(question)
                f.write("A. " + a)
                f.write("B. " + b)
                f.write("C. " + c)
                f.write("D. " + d)
                f.write("Answer: " + answer + "\n")
                done = True
