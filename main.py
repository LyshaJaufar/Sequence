import os, datetime, time, argparse, re

parser = argparse.ArgumentParser(description="Evaluate a given sequence of numbers and display the results")
parser.add_argument("-l", "--login", help="Name of logfile", nargs=1)
parser.add_argument("-t", "--firstTerm", help="First term of sequence", nargs=1)
parser.add_argument("-p", "--patternRule", help="Pattern rule for sequence", nargs=1)
parser.add_argument("-s", "--sequenceLength", help="Length of the sequence", nargs=1, type=int)
parser.add_argument("-n", "--nthTerm", help="nth term to find in the sequence", nargs=1)
parser.add_argument("-o", '--output', help="Would you like to display the evaluation of each term of the sequence?", nargs=1)
parser.add_argument("-st", '--sequenceType', help='Sequence type: Arithmetic/Geometric')
args = parser.parse_args()

print("\n\nThis is a program that performs the following functions and displays the results: \n")
print("\t1.a Evaluates a sequence of any length by relating to its features (first term of the seequence, pattern rule..)")
print("\t1.b Or predicts the next n terms of a given arithmetic sequence of any length.")
print("\t2. Calculate the series formed by the sequence.")
print("\t3. Finds the value of the term a(n) for any positive integer n.")
print("\t4. And represents the sequence in its recursive and explicit notation.\n")

def main():
    global firstTerm, sequenceLength, patternRule, nthTerm, sequenceOfNumbers
    global defineSequenceOrNot, extendSequence, showVisualOutputYesOrNo, sequenceType, starttime, logFileName
    if __name__ == '__main__':
        starttime = time.time()
        # 4. Represent a given sequence in its recursive and explicit notation
        # 1.b Ask user if they wish to extend the sequence they already provided
        if args.firstTerm == None:
            if args.patternRule == None:
                defineSequenceOrNot = askToDefineSequenceOrNot()
            else:
                defineSequenceOrNot = False
        else:
            defineSequenceOrNot = False
        if defineSequenceOrNot == True:
            extendSequence = askToExtendSequenceOrNot()
        else:
            extendSequence = False
            sequenceOfNumbers = []

        # User chooses to extend sequence they provided
        if args.sequenceLength == None:
            sequenceLength = lengthOfSequence()
        else:
            sequenceLength = int(args.sequenceLength[0])


        # 1.a Evaluates a sequence of any length by relating to its features:
        if defineSequenceOrNot == False:
            # Features: 1.First term
            if args.firstTerm == None:
                firstTerm = startingTerm()
            else:
                firstTerm = int(args.firstTerm[0])
            # Features: 2. Pattern rule
            if args.patternRule == None:
                patternRule = pattern()
            else:
                patternRule = int(args.patternRule[0])
        # 4. Find the first term and the pattern rule of a sequence provided by the user
        else:
            firstTerm = int(sequenceOfNumbers[0])
            patternRule = int(findPatternRule(sequenceOfNumbers))


        # Ask user to input a positive integer n.
        if args.nthTerm == None:
            nthTerm = NthTerm()
        else:
            nthTerm = int(args.nthTerm[0])

        # Display tie evaluation of each term
        if args.output == None:
            showVisualOutputYesOrNo = askToShowVisualOutput()
        elif args.output[0].lower() == 'y' or args.output[0].lower() == 'yes':
            showVisualOutputYesOrNo = True
        else:
            showVisualOutputYesOrNo = False

        # Save data onto a logfile
        if args.login == None:
            logFileName = askToLogOrNot()
        elif args.login[0].lower() != 'n' or args.login[0].lower() != 'no':
            loginFileName = args.login[0]
        else:
            logFileName = 'n'



# Apply the recursive formula to:
#  --->  output the value of the term a(n), for any nth term
#  --->  find each term to simulate a sequence of numbers by relating to its features(feataures are provided by user in this case)
#  --->  generate the next terms of a sequence provided by the user
def findNthTermForArithmetic(n):
    if n == 1:
        return firstTerm
    else:
        return patternRule + findNthTermForArithmetic(n-1)

def findNthTermForGeometric(n):
    if n == 1:
        return firstTerm
    else:
        return patternRule * findNthTermForGeometric(n-1)

def findNthTermAExplicit(n):
    return (firstTerm + patternRule) * (n - 1) 

def findNthTermGExplicit(n):
    return firstTerm * (patternRule)**(n-1)

# 1.a Simulate a sequence of numbers 
# 1.b Or extend sequence provided by user
def evaluateSequence(counter=1):
    sequence = []
    while counter != (sequenceLength + 1 + len(sequenceOfNumbers)):
        if sequenceLength < 900:
            if sequenceType == 'arithmetic':
                nextTerm = findNthTermForArithmetic(counter)
            else:
                nextTerm = findNthTermForGeometric(counter)
            sequence.append(nextTerm)
            counter += 1
        else:
            if sequenceType == 'arithmetic':
                nextTerm = findNthTermAExplicit(counter)
            else:
                nextTerm = findNthTermGExplicit(counter)
            sequence.append(nextTerm)
            counter += 1
    return sequence

def findSeries(sequenceX):
    seriesSum = sum(sequenceX[x] for x in range(len(sequenceX))) 
    return seriesSum

def visualOutputExplicit():
    print(f"\ta(1) = {firstTerm}")
    for i in range(2, sequenceLength + 1):
        if sequenceType == 'arithmetic':
            prevFunc = int(findNthTermAExplicit(i - 1))
            print(f"\ta({i}) = {firstTerm} + {i - 1} * ({patternRule}) = {firstTerm + ((i-1) * patternRule)}")
        else:
            prevFunc = int(findNthTermGExplicit(i - 1))
            print(f"\ta({i}) = {firstTerm} * ({patternRule})**{i - 1}  = {firstTerm * patternRule**(i-1)}")

def visualOutputRecursive():
    print(f"\ta(1) = {firstTerm}")
    for i in range(2, sequenceLength + 1):
        if sequenceType == 'arithmetic':
            prevFunc = int(findNthTermForArithmetic(i - 1))
            print(f"\ta({i}) = a({i - 1}) + {patternRule} = {prevFunc} + {patternRule} = {prevFunc + patternRule}")
        else:
            prevFunc = int(findNthTermForGeometric(i - 1))
            print(f"\ta({i}) = a({i - 1}) * {patternRule} = {prevFunc} * {patternRule} = {prevFunc * patternRule}")

def outputAnalysis():
    global sequenceType, sequence, series, valueOfNthTermForArithmetic, valueOfNthTermForGeometric, elapsedtime
    if defineSequenceOrNot == True:
        sequenceType = determineArithmeticOrGeometric()
    else:
        if args.sequenceType == None:
            sequenceType = askArithmeticOrGeometric()
        elif args.sequenceType[0] == 'g' or args.sequenceType[0] == 'geometric':
            sequenceType = 'geometric'
        else:
            sequenceType = 'arithmetic'

    if nthTerm > 900:
        valueOfNthTermForArithmetic = findNthTermAExplicit(nthTerm)
        valueOfNthTermForGeometric = findNthTermGExplicit(nthTerm)
    else:
        valueOfNthTermForArithmetic = findNthTermForArithmetic(nthTerm)
        valueOfNthTermForGeometric = findNthTermForGeometric(nthTerm)

    # 1.a Evaulate a sequence of numbers by relating its features
    if defineSequenceOrNot == False: 
        sequence = evaluateSequence()
        print(f"\n\n\nEvaluate the given sequence from its first term upto its {sequenceLength}th term: ", end="")
        print(*sequence)

    # 1.b Extend a sequence provided by the user
    elif defineSequenceOrNot == True and extendSequence == True:
        sequence = evaluateSequence(len(sequenceOfNumbers) + 1)
        print(f"\n\n\nThe next {sequenceLength} terms of your sequence: ", end="")
        print(*sequence)

    if showVisualOutputYesOrNo == True:
        print("Evaluation of each term using the explicit formula: ")
        visualOutputExplicit()
        # program breaks if sequence length > 900 --> too many recursive calls 
        if sequenceLength < 900:
            print("\nEvaluation of each term using the recursive formula: ")
            visualOutputRecursive()

    series = findSeries(sequence)
    print(f"Series formed from the sequence: {series}\n", end="") 

    if sequenceType == 'arithmetic':
        print(f"\nFind a({nthTerm}) in the sequence given by:") 

        # 4. Explicit definition
        print("Explicit definiton: ")
        print(f"\ta(n) = {firstTerm} + {patternRule}(n - 1)\n")

        # 4. Recursive definition 
        print("Recursive definition: ")
        print("\ta(1) =", firstTerm)
        print(f"\ta(n) = a(n - 1) + {patternRule}\n")
        print(f"Therefore, a({nthTerm}) =", valueOfNthTermForArithmetic,"\n")

    else:
        print(f"\nFind a({nthTerm}) in the sequence given by:") 

        # 4. Explicit definition
        print("Explicit definiton: ")
        print(f"\ta(n) = {firstTerm} * ({patternRule})(n - 1)\n")

        # 4. Recursive definition 
        print("Recursive definition: ")
        print("\ta(1) =", firstTerm)
        print(f"\ta(n) = a(n - 1) * ({patternRule})\n")
        print(f"Therefore, a({nthTerm}) =", valueOfNthTermForGeometric,"\n")

    elapsedtime = str(datetime.timedelta(seconds=round(time.time()-starttime, 2)))
    elapsedtime = elapsedtime[:-4]
    print("Total execution time:", elapsedtime,"\n")


def outputLogfile():
    global logfile
    if logFileName.lower() != 'n':
        logfile = open(os.getcwd() + '/' + logFileName,'w')
        print("A logfile was published to ", os.getcwd() + '/' + logFileName)
        if defineSequenceOrNot == True:
            logfile.write("User inputted sequence: ")
            for i in range(len(sequenceOfNumbers)):
                logfile.write(str(sequenceOfNumbers[i] + " "))
        else:
            logfile.write("User inputted 'first term': " + str(firstTerm) + "\nUser inputted 'pattern rule': " + str(patternRule))
        logfile.write("\n\nSequence above extended upto its " + str(sequenceLength) + "th term: ")
        for i in range(len(sequence)):
            logfile.write(str(sequence[i]) + ' ')
        if showVisualOutputYesOrNo == True:
            logfile.write("\nEvaluation of each term using the explicit formula: \n")
            visualOutputExplicitForLogfile()
            if sequenceLength < 900:
                logfile.write("\nEvaluation of each term using the recursive formula:\n")
                visualOutputRecursiveForLogfile()
        logfile.write("\n\nSeries formed from the sequence: " +str(series) + "\n\n")
        if sequenceType == 'arithmetic':
            logfile.write("Find a("+str(nthTerm)+") in the sequence given by:\n")

            # Explicit definition
            logfile.write("Explicit definition: \n")
            logfile.write("\ta(n) = "+str(firstTerm)+" + "+str(patternRule)+"(n - 1)\n\n")
            
            # Recursive definition
            logfile.write("Recursive definition: \n")
            logfile.write("\ta(1) = " + str(firstTerm) + "\n")
            logfile.write("\ta(n) = a(n - 1) + " +str(patternRule)+"\n\n")
            logfile.write("Therefore, a("+str(nthTerm)+") = " +str(valueOfNthTermForArithmetic)+ "\n")
        logfile.write("Total execution time: " +str(elapsedtime)+ "\n\n")
    else:
        print("No log created")

def visualOutputExplicitForLogfile():
    logfile.write("\ta(1) = "+str(firstTerm)+"\n")
    for i in range(2, sequenceLength + 1):
        if sequenceType == 'arithmetic':
            prevFunc = int(findNthTermAExplicit(i - 1))
            logfile.write("\ta("+str(i)+") = "+str(firstTerm)+" + "+str(i - 1)+" * "+str(patternRule)+" = "+str(firstTerm + ((i-1) * patternRule))+"\n")
        else:
            prevFunc = int(findNthTermGExplicit(i - 1))
            logfile.write("\ta("+str(i)+") = "+str(firstTerm)+" * "+str(patternRule)+"**"+str(i - 1)+"  = "+str(firstTerm * patternRule**(i-1))+"\n")

def visualOutputRecursiveForLogfile():
    logfile.write("\ta(1) = "+str(firstTerm)+"\n")
    for i in range(2, sequenceLength + 1):
        if sequenceType == 'arithmetic':
            prevFunc = int(findNthTermForArithmetic(i - 1))
            logfile.write("\ta("+str(i)+") = a("+str(i - 1)+") + "+str(patternRule)+" = "+str(prevFunc)+" + "+str(patternRule)+" = "+str(prevFunc + patternRule)+"\n")
        else:
            prevFunc = int(findNthTermForGeometric(i - 1))
            logfile.write("\ta("+str(i)+") = a("+str(i - 1)+") * "+str(patternRule)+" = "+str(prevFunc)+" * "+str(patternRule)+" = "+str(prevFunc * patternRule)+"\n")


# 1.a Ask user to provide the first term of the sequence
def startingTerm():
    firstTerm = int(input("1.b Enter the first term: ")) 
    return firstTerm

# 1.a Ask user to provide the pattern rule of the sequence
def pattern():
    patternRule = int(input("1.b Enter the pattern rule for your sequence: "))
    return patternRule

# 1.b Find the pattern rule from a sequence provided by the user
def findPatternRule(sequenceOfNumbers):
    global sequenceType
    sequenceType = determineArithmeticOrGeometric()
    if sequenceType == 'arithmetic':
        patternRule = int(sequenceOfNumbers[1]) - int(sequenceOfNumbers[0])
    else:
        patternRule = int(sequenceOfNumbers[1]) / int(sequenceOfNumbers[0])
    return patternRule

def NthTerm():
    nthTerm = int(input("3. Enter any positive integer n to find the value of the term a(n) of your sequence: "))
    return nthTerm

def lengthOfSequence():
    if extendSequence == False and defineSequenceOrNot == False:
        sequenceLength = int(input("Enter the length of your sequence: ")) 
    else:
        sequenceLength = int(input("Number of additional terms to your sequence: "))
    return sequenceLength

def askToDefineSequenceOrNot():
    global sequenceOfNumbers
    defineSequenceYesOrNo = input("1.a Would you like the program to construct a recursive/explicit formula for a given sequence? Y/N: ")
    if re.search("y(es)?", defineSequenceYesOrNo, re.IGNORECASE):
        sequenceOfNumbers = list(input("Enter your sequence: ").rstrip().split())
        return True
    else:
        return False

def askToExtendSequenceOrNot():
    extendSequenceYesOrNo = input("Would you like to extend your sequence? Y/N: ")
    if re.search("y(es)?", extendSequenceYesOrNo, re.IGNORECASE):
        return True
    else:
        return False

def askToShowVisualOutput():
    askToShowVisualOutputOrNot = input("Would you like to visually output the evaluation of each term? Y/N: ")
    if re.search("y(es)?", askToShowVisualOutputOrNot, re.IGNORECASE):
        return True
    else:
        return False

def determineArithmeticOrGeometric():
    if defineSequenceOrNot == True:
        x = int(sequenceOfNumbers[1]) - int(sequenceOfNumbers[0])
        y = int(sequenceOfNumbers[2]) - int(sequenceOfNumbers[1])
        if x == y:
            return 'arithmetic'
    else:
        return 'geometric'

def askArithmeticOrGeometric():
    arithmeticOrGeometric = input("Is your sequence arithmetic or geometric? A/G: ")
    if re.search("a(rithmetic)?", arithmeticOrGeometric, re.IGNORECASE):
        return "arithmetic"
    else:
        return "geometric"

def askToLogOrNot():
    logFileYesOrNo = input("Would you like to save a logfile? ")
    if re.search("y(es)?", logFileYesOrNo, re.IGNORECASE):
        logFileName = input("Logfile filename: ")
    else:
        logFileName = 'n'
    return logFileName

main()
outputAnalysis()
outputLogfile()

