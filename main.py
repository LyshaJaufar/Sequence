import os, datetime, time, argparse, re

parser = argparse.ArgumentParser(description="Simulate a sequence of numbers for a given starting point at a given common difference")
parser.add_argument("-l", "--login", help="Name of logfile", nargs=1)
args = parser.parse_args()

print("\nThis is a program that simulates a sequence of numbers for a given starting point at a given common difference")

def main():
    if __name__ == '__main__':
        if args.login == None:
            logFileName = askToLogOrNot()
        elif args.login[0].lower() != 'n' or args.login[0].lower() != 'no':
            loginFileName = args.login[0]

        else:
            logFileName = 'n'

def askToLogOrNot():
    logFileYesOrNo = input("Would you like to save a logfile? ")
    if re.search("y(yes)?", logFileYesOrNo, re.IGNORECASE):
        logFileName = input("Logfile filename: ")
    else:
        logFileName = 'n'
    return logFileName

main()