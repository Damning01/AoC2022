# make sure you can read from rucksack.txt
rucksack = open('rucksack.txt', 'r').readlines()
# remove the newlines
rucksack = [i.replace('\n', '') for i in rucksack]

# check the length of every item, split it in two (equal parts)
compartments = [[item[:(len(item) // 2)], item[(len(item) // 2):]] for item in rucksack]
# print(compartments)
# grab the letter that lives in the first and second compartment, put it in a string in a list
compartments = [''.join(set(duplicate for duplicate in item[0] if duplicate in item[1])) for item in compartments]
print(compartments)

# Return an integer representing the Unicode code point of that character(order func).
# Figure out the character integers
print(ord('a'))
print(ord('A'))
print(ord('z'))
print(ord('Z'))

# a=97, A=65, z=122, Z=90
# example: A: 65 % 64 - 26 = -25
# example: a: 97 % 64 - 32 = 1
def score(duplicate):
    return ord(duplicate) % 64 - (32 if duplicate.islower() else -26)


# Add all the integers together to get the sum
print(sum([score(duplicate) for duplicate in compartments]))
