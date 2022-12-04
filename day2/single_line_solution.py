# Advent of Code 2022 - Day 2

# Single line solutions

# Part 1 - Total score if column 2 is my move
print(sum([{"A": { "X": 4, "Y": 8, "Z": 3 }, "B": { "X": 1, "Y": 5, "Z": 9 }, "C": { "X": 7, "Y": 2, "Z": 6 }}[game.split()[0]][game.split()[1]] for game in open('input.txt', 'r').readlines()]))

# Part 2 - Total score if column 2 is the result
print(sum([{"A": { "X": 3, "Y": 4, "Z": 8 }, "B": { "X": 1, "Y": 5, "Z": 9 }, "C": { "X": 2, "Y": 6, "Z": 7 }}[game.split()[0]][game.split()[1]] for game in open('input.txt', 'r').readlines()]))
