numbers1 = [1,3,1,7,9,3,1,9,7]
numbers2 = [1,2,3]

# Read the list numbers1 and save the numbers that is in list numbers2
contentNumbers = []
for number in numbers1:
    for number2 in numbers2:
        if number == number2:
            contentNumbers.append(number)

print(contentNumbers)


# Read the list numbers1 and save the numbers that is in list numbers2 without repeat numbers
contentNumbers = []
cleanList = list(set(numbers1))
for number in cleanList:
    for number2 in numbers2:
        if number == number2:
            contentNumbers.append(number)

print(contentNumbers)

# Read the list numbers1 and print the number with more repeatition
print("-------")
numbers1 = [1,3,7,7,9,3,1,9,7]
numbers2 = [1,2,3]
counterNumbers = []
listNumbers = []

for index, number in enumerate(numbers1):
    counter = 0
    found = False
    for checkNumber in listNumbers:
        if checkNumber == number:
            found = True
            counter = counter + 1
    if found == False:
        listNumbers.append(number)
        counterNumbers.append(1)
    if found == True:
        newPosition = 0
        for index2, newNumber in enumerate(listNumbers):
            if newNumber == index2:
                newPosition = index2
                break
        counterNumbers[newPosition] = counter

print(listNumbers)
print(counterNumbers)
