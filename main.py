import os, datetime, time, argparse, re

parser = argparse.ArgumentParser(description="Evaluate a given sequence of numbers and display the results")
parser.add_argument("-l", "--login", help="Name of logfile", nargs=1)
parser.add_argument("-d", "--defineSequence", help="Would you like the program to define a given sequence? ")
parser.add_argument("-t", "--firstTerm", help="First term of sequence", nargs=1)
parser.add_argument("-p", "--patternRule", help="Pattern rule for sequence", nargs=1)
parser.add_argument("-s", "--sequenceLength", help="Length of the sequence", nargs=1, type=int)
parser.add_argument("-n", "--nthTerm", help="nth term to find in the sequence", nargs=1)
parser.add_argument("-o", '--output', help="Would you like to display the evaluation of each term of the sequence?", nargs=1)
args = parser.parse_args()

print("\n\nThis is a program that performs the following functions and displays the results: \n")
print("\t1.a Evaluates a sequence of any length by relating to its features (first term of the seequence, pattern rule..)")
print("\t1.b Or predicts the next n terms of a given arithmetic sequence of any length.")
print("\t2. Finds the value of the term a(n) for any positive integer n.")
print("\t3. And represents the sequence in its recursive and explicit notation.\n")

def main():
    global firstTerm, sequenceLength, patternRule, nthTerm, sequenceOfNumbers, defineSequenceOrNot, extendSequence, showVisualOutputYesOrNo
    if __name__ == '__main__':
        # 3. Represent a given sequence in its recursive and explicit notation
        # 1.b Ask user if they wish to extend the sequence they already provided
        if args.defineSequence == None:
            defineSequenceOrNot = askToDefineSequenceOrNot()
            extendSequence = askToExtendSequenceOrNot()
        elif args.defineSequence[0].lower() != 'n' or args.defineSequence[0].lower() != 'no':
            defineSequenceOrNot = True
            sequenceOfNumbers = list(input("Enter your arithmetic sequence: ").rstrip().split())
            if args.sequenceLength == None:
                extendSequence = askToExtendSequenceOrNot()
            else:
                extendSequence = True
        else:
            defineSequenceOrNot = False
            extendSequence = True
            sequenceOfNumbers = 0

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
        # 3. Find the first term and the pattern rule of a sequence provided by the user
        else:
            firstTerm = int(sequenceOfNumbers[0])
            patternRule = int(findPatternRule(sequenceOfNumbers))


        # Ask user to input a positive integer n.
        if args.nthTerm == None:
            nthTerm = NthTerm()
        else:
            nthTerm = int(args.nthTerm[0])

        # Display the evaluation of each term
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

# 1.a Simulate a sequence of numbers 
# 1.b Or extend sequence provided by user
def evaluateSequence(counter=1):
    sequence = []
    while counter != (sequenceLength + 1 + len(sequenceOfNumbers)):
        if sequenceType == 'arithmetic':
            nextTerm = findNthTermForArithmetic(counter)
        else:
            nextTerm = findNthTermForGeometric(counter)
        sequence.append(nextTerm)
        counter += 1
    return sequence

def visualOutput():
    print(f"\ta(1) = {firstTerm}")
    for i in range(2, sequenceLength + 1):
        if sequenceType == 'arithmetic':
            prevFunc = int(findNthTermForArithmetic(i - 1))
            print(f"\ta({i}) = a({i - 1}) + ({patternRule}) = {prevFunc} + {patternRule} = {prevFunc + patternRule}")
        else:
            prevFunc = int(findNthTermForGeometric(i - 1))
            print(f"\ta({i}) = a({i - 1}) * ({patternRule}) = {prevFunc} * {patternRule} = {prevFunc * patternRule}")


def outputAnalysis():
    valueOfNthTermForArithmetic = findNthTermForArithmetic(nthTerm)
    valueOfNthTermForGeometric = findNthTermForGeometric(nthTerm)

    # 1.a Evaulate a sequence of numbers by relating its features
    if defineSequenceOrNot == False: 
        sequence = evaluateSequence()
        print(f"\n\n\nEvaluate the given arithmetic sequence from its first term upto its {sequenceLength}th term: ", end="")
        print(*sequence)

    # 1.b Extend a sequence provided by the user
    elif defineSequenceOrNot == True and extendSequence == True:
        sequence = evaluateSequence(len(sequenceOfNumbers) + 1)
        print(f"\n\n\nThe next {sequenceLength} terms of your sequence: ", end="")
        print(*sequence)

    if showVisualOutputYesOrNo == True:
        print("\nEvaluation of each term: ")
        visualOutput()

    if sequenceType == 'arithmetic':
        # 3. Recursive definition 
        print(f"\nFind a({nthTerm}) in the sequence given by:") 
        print("Recursive definition: ")
        print("\ta(1) =", firstTerm)
        print(f"\ta(n) = a(n - 1) + ({patternRule})\n")

        # 3. Explicit definition
        print("Explicit definiton: ")
        print(f"\ta(n) = {firstTerm} + ({patternRule})(n - 1)\n")
        print(f"Therefore, a({nthTerm}) =", valueOfNthTermForArithmetic,"\n")

    else:
        # 3. Recursive definition 
        print(f"\nFind a({nthTerm}) in the sequence given by:") 
        print("Recursive definition: ")
        print("\ta(1) =", firstTerm)
        print(f"\ta(n) = a(n - 1) * ({patternRule})\n")

        # 3. Explicit definition
        print("Explicit definiton: ")
        print(f"\ta(n) = {firstTerm} * ({patternRule})(n - 1)\n")
        print(f"Therefore, a({nthTerm}) =", valueOfNthTermForGeometric,"\n")





# 1.a Ask user to provide the first term of the sequence
def startingTerm():
    firstTerm = int(input("Enter the first term: ")) 
    return firstTerm

# 1.a Ask user to provide the pattern rule of the sequence
def pattern():
    patternRule = int(input("Enter the pattern rule for your sequence: "))
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
    nthTerm = int(input("Enter nth term that you wish to find: "))
    return nthTerm

def lengthOfSequence():
    if extendSequence == False:
        sequenceLength = int(input("Enter the length of your sequence: ")) 
    else:
        sequenceLength = int(input("Number of additional terms to your sequence: "))
    return sequenceLength

def askToDefineSequenceOrNot():
    global sequenceOfNumbers
    defineSequenceYesOrNo = input("Would you like the program to construct a recursive formula for a given sequence? ")
    if re.search("y(es)?", defineSequenceYesOrNo, re.IGNORECASE):
        sequenceOfNumbers = list(input("Enter your arithmetic sequence: ").rstrip().split())
        return True
    else:
        return False

def askToExtendSequenceOrNot():
    extendSequenceYesOrNo = input("Would you like to extend your sequence?  ")
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

def askToLogOrNot():
    logFileYesOrNo = input("Would you like to save a logfile? ")
    if re.search("y(es)?", logFileYesOrNo, re.IGNORECASE):
        logFileName = input("Logfile filename: ")
    else:
        logFileName = 'n'
    return logFileName

main()
outputAnalysis()



# series 996 997