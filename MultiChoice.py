
#Check if the question exists already
def checkForQuestion(question):
    try:
        f = open("Aright.txt", "r", encoding='cp1252')
        isIn = False
        for x in f:
            if question in x:
                isIn = True
        f.close()
        return isIn
    except:
        f = open("Aright.txt", "r")
        isIn = False
        for x in f:
            if question in x:
                isIn = True
        f.close()
        return isIn

#Gather correct option from user and append all data to coorisponding files
def inputAndSend(q, a, b, c, d):
    rightOption = input("Which letter option was correct: ")
    if rightOption == "a":
        appendRightFile(a, q)

        appendWrongFile(b, q)
        appendWrongFile(c, q)
        appendWrongFile(d, q)
    elif rightOption == "b":
        appendRightFile(b, q)

        appendWrongFile(a, q)
        appendWrongFile(c, q)
        appendWrongFile(d, q)
    elif rightOption == "c":
        appendRightFile(c, q)

        appendWrongFile(a, q)
        appendWrongFile(b, q)
        appendWrongFile(d, q)
    elif rightOption == "d":
        appendRightFile(d, q)

        appendWrongFile(a, q)
        appendWrongFile(b, q)
        appendWrongFile(c, q)

#Append Question and right option to aRight text file
def appendRightFile(option, question):
    try:
        f = open("Aright.txt", "a", encoding='cp1252')
        f.write("\n" + "\n" + question + "\n" + option)

        f.close()
    except:
        f = open("Aright.txt", "a", encoding='utf-8')
        f.write("\n" + "\n" + question + "\n" + option)
        f.close()

#Append Question and wrong option to aWrong text file
def appendWrongFile(option, question):
    try:
        f = open("Awrong.txt", "a", encoding='cp1252')
        f.write("\n" + "\n" + question + "\n" + option)
        f.close()
    except:
        f = open("Awrong.txt", "a", encoding='utf-8')
        f.write("\n" + "\n" + question + "\n" + option)
        f.close()

#Read and Search Question and Option in the aRight text file
def readRightFile(option, question):
    try:
        f = open("Aright.txt", "r", encoding='cp1252')
        isIn = False
        #For lines in file
        for x in f:
            #Search if question exists
            if question in x:
                #Then search if next line is option
                nextLine = next(f, None)
                if option in nextLine:
                    isIn = True
        f.close()
        return isIn
    except:
        f = open("Aright.txt", "r")
        isIn = False
        #For lines in file
        for x in f:
            #Search if question exists
            if question in x:
                #Then search if next line is option
                nextLine = next(f, None)
                if option in nextLine:
                    isIn = True
        f.close()
        return isIn

#Read and Search Question and Option in the aWrong text file
def readWrongFile(option, question):
    try:
        f = open("Awrong.txt", "r", encoding='cp1252')
        isIn = False
        #For lines in file
        for x in f:
            #Check if Question Exists
            if question in x:
                #Then Check if next line is option
                nextLine = next(f, None)
                if option in nextLine:
                    isIn = True
        f.close()
        return isIn
    except:
        f = open("Awrong.txt", "r")
        isIn = False
        #For lines in file
        for x in f:
            #Check if Question Exists
            if question in x:
                #Then Check if next line is option
                nextLine = next(f, None)
                if option in nextLine:
                    isIn = True
        f.close()
        return isIn


def main():
    # looping program to prevent it from stopping
    while True:
        print("Ctrl V, enter, period, enter.")

        # Get Long String from the user and split it into lines
        buffer = []
        while True:
            print("> ", end="")
            line = input()
            if line == ".":
                break
            buffer.append(line)
        collection = "\n".join(buffer)

        # Split Each Line
        count = 0
        for line in collection.split('\n'):
            if count == 0:
                q = line
            if count == 1:
                a = line
            if count == 2:
                b = line
            if count == 3:
                c = line
            if count == 4:
                d = line
            count += 1

        # tell whether question exists or not
        if checkForQuestion(q) == True:
            print("Question Exists")
        else:
            print("Question Doesnt Exist")

        # -----------------------------------------------------------------------------------------------------------------------
        # Check Files for lines and Display Results

        # Check if a is in right file
        aRight = readRightFile(a, q)
        # Check if a is in wrong file
        aWrong = readWrongFile(a, q)

        #Counter of unlisted options
        nullCount = 0

        if aRight == True and aWrong == False:
            print("A == Correct++++++++++")
        elif aWrong == True and aRight == False:
            print("A == Wrong")
        elif aRight == False and aWrong == False:
            print("A == Null????????????")
            nullCount += 1
        elif aRight == True and aWrong == True:
            print("A == Error")

        # Check if b is in right file
        bRight = readRightFile(b, q)
        # Check if b is in wrong file
        bWrong = readWrongFile(b, q)

        if bRight == True and bWrong == False:
            print("B == Correct++++++++++")
        elif bWrong == True and bRight == False:
            print("B == Wrong")
        elif bRight == False and bWrong == False:
            print("B == Null????????????")
            nullCount += 1
        elif bRight == True and bWrong == True:
            print("B == Error")

        # Check if c is in right file
        cRight = readRightFile(c, q)
        # Check if c is in wrong file
        cWrong = readWrongFile(c, q)

        if cRight == True and cWrong == False:
            print("C == Correct++++++++++")
        elif cWrong == True and cRight == False:
            print("C == Wrong")
        elif cRight == False and cWrong == False:
            print("c == Null????????????")
            nullCount += 1
        elif cRight == True and cWrong == True:
            print("C == Error")

        # Check if d is in right file
        dRight = readRightFile(d, q)
        # Check if d is in wrong file
        dWrong = readWrongFile(d, q)

        if dRight == True and dWrong == False:
            print("D == Correct++++++++++")
        elif dWrong == True and dRight == False:
            print("D == Wrong")
        elif dRight == False and dWrong == False:
            print("D == Null????????????")
            nullCount += 1
        elif dRight == True and dWrong == True:
            print("D == Error")

        # -----------------------------------------------------------------------------------------------------------------------

        # if any are correct just append all the wrong ones
        if aRight == True:

            appendWrongFile(b, q)
            appendWrongFile(c, q)
            appendWrongFile(d, q)
        elif bRight == True:

            appendWrongFile(a, q)
            appendWrongFile(c, q)
            appendWrongFile(d, q)
        elif cRight == True:

            appendWrongFile(a, q)
            appendWrongFile(b, q)
            appendWrongFile(d, q)
        elif dRight == True:

            appendWrongFile(a, q)
            appendWrongFile(b, q)
            appendWrongFile(c, q)
        else:
            # if too many unknow options get the correct answer from the user
            if nullCount == 4 or nullCount == 3 or nullCount == 2:
                inputAndSend(q, a, b, c, d)

            # if all are wrong and only one is null
            elif nullCount == 1:
                if aWrong == True and bWrong == True and cWrong == True:
                    appendRightFile(d, q)

                elif aWrong == True and bWrong == True and dWrong == True:
                    appendRightFile(c, q)

                elif aWrong == True and cWrong == True and dWrong == True:
                    appendRightFile(b, q)

                elif bWrong == True and cWrong == True and dWrong == True:
                    appendRightFile(a, q)

main()
