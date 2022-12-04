# Advent of Code 2022 - Day 1

# Single line solutions

# Part 1 - Find the elf carrying the most calories
print(max([sum(map(int,inventory.split("\n"))) for inventory in open("input.txt", "r").read().split("\n\n")]))

# Part 2 - Find the sum of the callaries the top 3 elves are carrying
print(sum(sorted([sum(map(int,inventory.split("\n"))) for inventory in open("input.txt", "r").read().split("\n\n")])[-3:]))