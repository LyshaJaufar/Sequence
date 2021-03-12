import os, datetime, time, argparse, re

parser = argparse.ArgumentParser(description="Evaluate a given sequence of numbers and display the results")
parser.add_argument("-l", "--login", help="Name of logfile", nargs=1)
parser.add_argument("-d", "--defineSequence", help="Would you like the program to define a given sequence? ")
parser.add_argument("-t", "--firstTerm", help="First term of sequence", nargs=1)
parser.add_argument("-p", "--patternRule", help="Pattern rule for sequence", nargs=1)
parser.add_argument("-s", "--sequenceLength", help="Length of the sequence", nargs=1)
parser.add_argument("-n", "--nthTerm", help="nth term to find in the sequence", nargs=1)
args = parser.parse_args()

print("\n\nThis is a program that performs the following functions and displays the results: \n")
print("\t1.a Evaluates a sequence of any length by relating to its features (first term of the seequence, pattern rule..)")
print("\t1.b Or predicts the next n terms of a given arithmetic sequence of any length.")
print("\t2. Finds the value of the term a(n) for any positive integer n.")
print("\t3. And represents the sequence in its recursive and explicit notation.\n")

def main():
    global firstTerm, sequenceLength, patternRule, nthTerm, sequenceOfNumbers, defineSequenceOrNot, extendSequence 
    if __name__ == '__main__':
        # 3. Represent a given sequence in its recursive and explicit notation
        # 1.b Ask user if they wish to extend the sequence they already provided
        if args.defineSequence == None:
            defineSequenceOrNot = askToDefineSequenceOrNot()
            extendSequence = askToExtendSequenceOrNot()
        elif args.defineSequence[0].lower() != 'n' or args.defineSequence[0].lower() != 'no':
            defineSequenceOrNot = True
            sequenceOfNumbers = list(input("Enter your arithmetic sequence: ").rstrip().split())
            extendSequence = askToExtendSequenceOrNot()
        else:
            defineSequenceOrNot = False
            extendSequence = True

        # User chooses not to extend sequence they provided
        if extendSequence != False:
            if args.sequenceLength == None:
                sequenceLength = lengthOfSequence()
            else:
                sequenceLength = int(args.sequenceLength)


        # 1.a Evaluates a sequence of any length by relating to its features:
        if defineSequenceOrNot == False:
            # Features: 1.First term
            if args.firstTerm == None:
                firstTerm = startingTerm()
            else:
                firstTerm = int(args.firstTerm)
            # Features: 2. Pattern rule
            if args.patternRule == None:
                patternRule = pattern()
            else:
                patternRule = int(args.patternRule)
        # 3. Find the first term and the pattern rule of a sequence provided by the user
        else:
            firstTerm = int(sequenceOfNumbers[0])
            patternRule = int(findPatternRule(sequenceOfNumbers))


        # Ask user to input a positive integer n.
        if args.nthTerm == None:
            nthTerm = NthTerm()
        else:
            nthTerm = int(args.nthTerm)

        # Save data onto a logfile
        if args.login == None:
            logFileName = askToLogOrNot()
        elif args.login[0].lower() != 'n' or args.login[0].lower() != 'no':
            loginFileName = args.login[0]
        else:
            logFileName = 'n'


# consider making this into a class
def startingTerm():
    firstTerm = int(input("Enter the first term: ")) 
    return firstTerm

def pattern():
    patternRule = int(input("Enter the pattern rule for your sequence: "))
    return patternRule

def lengthOfSequence():
    if defineSequenceOrNot == False:
        sequenceLength = int(input("Enter the length of your sequence: ")) 
    else:
        sequenceLength = int(input("Number of additional terms to your sequence: "))
    return sequenceLength

def NthTerm():
    nthTerm = int(input("Enter nth term that you wish to find: "))
    return nthTerm



def evaluateSequence(counter=1):
    sequence = []
    while counter != (sequenceLength + 1):
        nextTerm = findNthTerm(counter)
        sequence.append(nextTerm)
        counter += 1
    return sequence

def findNthTerm(n):
    if n == 1:
        return firstTerm

    else:
        return patternRule + findNthTerm(n-1)

def findPatternRule(sequenceOfNumbers):
    patternRule = int(sequenceOfNumbers[1]) - int(sequenceOfNumbers[0])
    return patternRule

def outputAnalysis():
    valueOfNthTerm = findNthTerm(nthTerm)

    if defineSequenceOrNot == False: 
        sequence = evaluateSequence()
        print(f"\n\n\nEvaluate the given arithmetic sequence from its first term upto its {sequenceLength}th term: ", end="")
        print(*sequence)

    elif defineSequenceOrNot == True and extendSequence == True:
        sequence = evaluateSequence(len(sequenceOfNumbers) + 1)
        print(f"\n\n\nThe next {sequenceLength} of your arithmetic sequence: ", end="")
        print(*sequence)

    print("\nFind f(n) in the sequence given by:") 
    print("Recursive definition: ")
    print("\ta(1) =", firstTerm)
    print(f"\ta(n) = a(n - 1) + ({patternRule})\n")
    print("Explicit definiton: ")
    print(f"\ta(n) = {firstTerm} + ({patternRule})(n - 1)\n")
    print(f"Therefore, a({nthTerm}) =", valueOfNthTerm,"\n")





def askToDefineSequenceOrNot():
    global sequenceOfNumbers
    defineSequenceYesOrNo = input("Would you like the program to construct a recursive formula for a given sequence? ")
    if re.search("y(es)?", defineSequenceYesOrNo, re.IGNORECASE):
        sequenceOfNumbers = list(input("Enter your arithmetic sequence: ").rstrip().split())
        return True
    else:
        return False

def askToExtendSequenceOrNot():
    extendSequenceYesOrNo = input("Would you like to extend your arithmetic sequence?  ")
    if re.search("y(es)?", extendSequenceYesOrNo, re.IGNORECASE):
        return True
    else:
        return False

def askToLogOrNot():
    logFileYesOrNo = input("Would you like to save a logfile? ")
    if re.search("y(es)?", logFileYesOrNo, re.IGNORECASE):
        logFileName = input("Logfile filename: ")
    else:
        logFileName = 'n'
    return logFileName



main()

outputAnalysis()
#findNthTerm()