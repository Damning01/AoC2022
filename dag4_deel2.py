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

# Now see if there is SOME overlap between a section of a pair of elves,
# This means that this time the first section of the first elf is still SMALLER or the same as the first section of the second elf in the pair
# but this time: the SECOND section of the first elf has to be bigger or equal to the FIRST section of the second elf
# then: return true
def overlap(Elf1, Elf2):
    if (Elf1[0] <= Elf2[0]) & (Elf1[1] >= Elf2[0]):
        return True

# and the other way around:
# This means that this time the first section of the first elf is still BIGGER or the same as the first section of the second elf in the pair
# but this time: the SECOND section of the first elf has to be smaller or equal to the FIRST section of the second elf
#then: return true

    elif (Elf1[0] >= Elf2[0]) & (Elf1[0] <= Elf2[1]):
        return True

# Else; if there is no overlap whatsoever, return false
    else:
        return False

print('Sum of the overlapping sections: ',(sum([overlap(*pair) for pair in pairs])))
