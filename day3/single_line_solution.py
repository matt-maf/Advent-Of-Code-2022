# Advent of Code 2022 - Day 3

# Single line solutions

# Part 1 - Total priority of common items in compartments within rucksacks
print(sum([(ord(list(set(list(line)[:len(list(line))//2]).intersection(list(line)[len(list(line))//2:]))[0])-38) if list(set(list(line)[:len(list(line))//2]).intersection(list(line)[len(list(line))//2:]))[0].isupper() else (ord(list(set(list(line)[:len(list(line))//2]).intersection(list(line)[len(list(line))//2:]))[0])-96) for line in open("input.txt", "r").readlines()]))

# Part 2 - Total priority of common items in rucksacks within groups
print(sum([ord(list(set(list(set(chunk[0]).intersection(chunk[1]))).intersection(chunk[2]))[0])-38 if list(set(list(set(chunk[0]).intersection(chunk[1]))).intersection(chunk[2]))[0].isupper() else ord(list(set(list(set(chunk[0]).intersection(chunk[1]))).intersection(chunk[2]))[0])-96 for chunk in [open("input.txt", "r").read().split('\n')[x:x+3] for x in range(0, len(open("input.txt", "r").read().split('\n')), 3)]]))
