# Read from the input text files
sections = open('cleaningsections.txt', 'r').readlines()
print('Sections raw: ',(sections))

# Remove new lines
sections = [section.replace('\n','') for section in sections]
print('Sections without newline seperator: ',(sections))

# Split the sections for the Elven pairs (so on the comma), so you get strings for both elves separately
pairs = []
for section in sections:
    pairs = [[elf for elf in section.split(',')]]
    print('Split with for loop:',(pairs))

# Try again to split, but then without the for loop, so the output is one list with nested lists for every couple
# instead of for every couple's sections a new list
pairs = [[s for s in section.split(',')] for section in sections]
print('Split pairs: ', (pairs))

# Convert to integer values, remove for both sections in the list the '-'
pairs = [[[int(p.split('-')[0]), int(p.split('-')[1])] for p in pair] for pair in pairs]
print('Pairs',(pairs))

# Now see if there is complete overlap between a section of a pair of elves
# example no overlap:
# .234.....  2-4
# .....678.  6-8
# example overlap:
#.2345678.  2-8
#..34567..  3-7
def overlap(Elf1, Elf2):
# See if the first section of the first elf is SMALLER or the same as the first section of the second elf in the pair
# AND if the second section of the first elf is BIGGER or equal to the second section of the second elf, return true
    if (Elf1[0] <= Elf2[0]) & (Elf1[1] >= Elf2[1]):
        return True
# And the other way around:
# See if the first section of the first elf is BIGGER or the same as the first section of the second elf in the pair
# AND if the second section of the first elf is SMALLER or equal to the second section of the second elf, return true
    elif (Elf1[0] >= Elf2[0]) & (Elf1[1] <= Elf2[1]):
        return True

# Else; there is no overlap, so return false
    else:
        return False

print('Sum of the overlapping sections: ',(sum([overlap(*pair) for pair in pairs])))
