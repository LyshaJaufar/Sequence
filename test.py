mylist = [1, 2, 3, 4, 5]


startValue = int(input("Enter the starting value: "))
lengthofsequence = int(input("Enter the length of the sequence: "))
commonDifference = int(input("Enter the pattern rule: "))
newlist = [startValue]

prev = startValue
for i in range(lengthofsequence):
    newlist.append(prev + commonDifference)
    prev += commonDifference

print(*newlist)


# how to get the nth value
newlist[0] = 5
newlist[nthvalue] = newlist[nthvalue - 1] + commonDifference



# what happens if the nth term doesn't exist yet?
for i in range(n):
    