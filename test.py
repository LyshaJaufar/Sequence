def function(input):
    global startValue, commonDifference
    if input == 1:
        return startValue

    else:
        return commonDifference + function(input-1)

startValue = int(input("Enter the starting value: "))
lengthofsequence = int(input("Enter the length of the sequence: "))
commonDifference = int(input("Enter the pattern rule: "))
x=function(3)
print(x)
