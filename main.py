import os, datetime, time, argparse, re

parser = argparse.ArgumentParser(description="Simulate a sequence of numbers for a given starting point at a given common difference")
parser.add_argument("-l", "--login", help="Name of logfile", nargs=1)
parser.add_argument("-d", "--defineSequence", help="Would you like the program to define a given sequence? ")
parser.add_argument("-t", "--firstTerm", help="First term of sequence", nargs=1)
parser.add_argument("-p", "--patternRule", help="Pattern rule for sequence", nargs=1)
parser.add_argument("-s", "--sequenceLength", help="Length of the sequence", nargs=1)
parser.add_argument("-n", "--nthTerm", help="nth term to find in the sequence", nargs=1)
args = parser.parse_args()

print("\nThis is a program that simulates a sequence of numbers of any length for a given starting point at a given common difference")

def main():
    global firstTerm, sequenceLength, patternRule, nthTerm, sequenceOfNumbers, defineSequenceOrNot
    if __name__ == '__main__':
        if args.defineSequence == None:
            defineSequenceOrNot = askToDefineSequenceOrNot()
        elif args.defineSequence[0].lower() != 'n' or args.defineSequence[0].lower() != 'no':
            defineSequenceOrNot = True
            sequenceOfNumbers = list(input("Enter your arithmetic sequence: ").rstrip().split())
        else:
            defineSequenceOrNot = False

        if defineSequenceOrNot == False:
            if args.firstTerm == None:
                firstTerm = startingTerm()
            else:
                firstTerm = int(args.firstTerm)

            if args.patternRule == None:
                patternRule = pattern()
            else:
                patternRule = int(args.patternRule)

            if args.sequenceLength == None:
                sequenceLength = lengthOfSequence()
            else:
                sequenceLength = int(args.sequenceLength)

        else:
            firstTerm = sequenceOfNumbers[0]
            patternRule = findPatternRule()

        if args.nthTerm == None:
            nthTerm = NthTerm()
        else:
            nthTerm = int(args.nthTerm)

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
    sequenceLength = int(input("Enter the length of your sequence: "))   
    return sequenceLength

def NthTerm():
    nthTerm = int(input("Enter nth term that you wish to find: "))
    return nthTerm



def evaluateSequence():
    sequence = []
    i = 1
    while i != (sequenceLength + 1):
        nextTerm = findNthTerm(i)
        sequence.append(nextTerm)
        i += 1
    return sequence

def findNthTerm(n):
    if n == 1:
        return firstTerm

    else:
        return patternRule + findNthTerm(n-1)

def findPatternRule(sequenceOfNumbers):
    patternRule = sequenceOfNumbers[1] - sequenceOfNumbers[0]
    return patternRule

def outputAnalysis():
    valueOfNthTerm = findNthTerm(nthTerm)
    sequence = evaluateSequence()

    print("\n\nFind f(n) in the sequence given by:") 
    print("\tf(1) = ", firstTerm)
    print("\tf(n) = f(n - 1) -", patternRule,"\n")
    print(f"Therefore, f({nthTerm}) =", valueOfNthTerm)

    if defineSequenceOrNot == False: 
        print(f"Evaluate the given arithmetic sequence from its first term upto its {sequenceLength}th term: ", end="")
        print(*sequence)



def askToDefineSequenceOrNot():
    defineSequenceYesOrNo = input("Would you like the program to construct a recursive formula for a given sequence? ")
    if re.search("y(es)?", defineSequenceYesOrNo, re.IGNORECASE):
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