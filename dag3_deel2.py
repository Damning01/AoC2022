# make sure you can read from rucksack.txt
rucksack = open('rucksack.txt', 'r').readlines()
# remove the newlines
rucksack = [item.replace('\n', '') for item in rucksack]

# Group the input from rucksack.txt together so that the first three lines are in one group(list),
# the next three in the second enz
groups = [rucksack[item:item + 3] for item in range(0, len(rucksack), 3)]
print(groups)

# Look for an item type that is in all three of the groups rucksacks, those will be the identifiable badges.
# Put the letter in a list, but only if the letter is in all three rucksacks of elves in one group.
badges = [''.join(set(letter for letter in item[0] if ((letter in item[1]) & (letter in item[2])))) for item in groups]
print(badges)

# Get a number for that item, and sum all those items for all those grouped rucksacks together
# Use the magic from part one again, to get unicode integers representing the letters
def score(badges):
    return ord(badges) % 64 - (32 if badges.islower() else -26)

#Print the sum of all integers
print(sum([score(letter) for letter in badges]))
