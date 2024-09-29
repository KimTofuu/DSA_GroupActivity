def commonCharDel(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    str1 = str1.replace(' ','')
    str2 = str2.replace(' ','')

    set1 = set(str1)
    set2 = set(str2)

    sameChars = set1.intersection(set2)

    uniqueCharsStr1 = (''.join([char for char in str1 if char not in sameChars]))
    uniqueCharsStr2 = (''.join([char for char in str2 if char not in sameChars]))

    return uniqueCharsStr1, uniqueCharsStr2

def determiner(UnCharStr1, UnCharStr2):

    categ = ['F', 'L', 'A', 'M', 'E', 'S']

    lenOfUnStr1 = int(len(UnCharStr1))
    lenOfUnStr2 = int(len(UnCharStr2))

    iterationCount = lenOfUnStr1 + lenOfUnStr2

    loc = (iterationCount - 1) % len(categ)


    return categ[loc]

name1 = input('Enter the name of the first person: ')
name2 = input('Enter the name of the second person: ')

newStr1, newStr2 = commonCharDel(name1, name2)
outcome = determiner(newStr1, newStr2)

print(f"\n\nRemaining characters from {name1}: {newStr1} = {len(newStr1)}")
print(f"Remaining characters from {name2}: {newStr2} = {len(newStr2)}")
print(f"\nTotal remaining characters: {len(newStr1) + len(newStr2)}")
print(f"\nFLAMES result: {outcome}")


if (outcome == 'F'):
    print('Friends')
elif (outcome == 'L'):
    print('LDR')
elif (outcome == 'A'):
    print('Acquaintances')
elif (outcome == 'M'):
    print('Married')
elif (outcome == 'E'):
    print('Enemies')
elif (outcome == 'S'):
    print('Strangers')

