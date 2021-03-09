import os, datetime, time, argparse, re

parser = argparse.ArgumentParser(description="Simulate a sequence of numbers for a given starting point at a given common difference")
parser.add_argument("-l", "--login", help="Name of logfile", nargs=1)
args = parser.parse_args()

print("\nThis is a program that simulates a sequence of numbers of any length for a given starting point at a given common difference")

def main():
    if __name__ == '__main__':
        if args.login == None:
            logFileName = askToLogOrNot()
        elif args.login[0].lower() != 'n' or args.login[0].lower() != 'no':
            loginFileName = args.login[0]

        else:
            logFileName = 'n'


def startingTerm():
    firstTerm = int(input("Enter the first term: ")) 
    return firstTerm

def pattern():
    patternRule = int(input("Enter the pattern rule for your sequence: "))
    return patternRule

def lengthOfSequence():
    sequenceLength = int(input("Enter the length of your sequence: "))   

def NthTerm():
    nthTerm = int(input(""))

def sequence(index):
    firstTerm = firstTerm()
    patternRule = patternRule()
    sequenceLength = lengthOfSequence()

    sequence = [firstTerm]
    prev = firstTerm
    for i in range(sequenceLength):
        sequence.append(prev+patternRule)
        prev += patternRule

    return sequence

def findNthTerm():




def askToLogOrNot():
    logFileYesOrNo = input("Would you like to save a logfile? ")
    if re.search("y(yes)?", logFileYesOrNo, re.IGNORECASE):
        logFileName = input("Logfile filename: ")
    else:
        logFileName = 'n'
    return logFileName

main()




void draw(int h)
{
    // If nothing to draw
    if (h == 0)
    {
        return;
    }

    // Draw pyramid of height h - 1
    draw(h - 1);

    // Draw one more row of width h
    for (int i = 0; i < h; i++)
    {
        printf("#");
    }
    printf("\n");
}


void merge_sort(pair array[], int start, int end)
{
    //base case: 1 || 0 elements
    if (start >= end)
    {
        return;
    }

    //Follow 3 steps
    //1. Divide
    int mid = (start + end) / 2;

    //2. Sort
    merge_sort(array, start, mid);   //Sort left half
    merge_sort(array, mid + 1, end); //Sort right half

    //3. Merge two parts
    merge(array, start, mid, end);
}

