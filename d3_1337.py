lines = open('rucksack.txt', 'rt').read().split('\n')
dupes = [list(set(line[:len(line)//2]).intersection(set(line[len(line)//2:])))[0] for line in lines]
print(sum([ord(c) - (ord('A')-27 if c < 'a' else ord('a')-1) for c in dupes]))
