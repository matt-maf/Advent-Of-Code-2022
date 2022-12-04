# Advent of Code 2022 - Day 4

# Part 1 - Find total elves that are within the other elves in pairs
def part_one(sections):
    counter = 0

    for elf_pair in sections:
        elf_one = elf_pair.strip('\n').split(',')[0].split('-')
        elf_two = elf_pair.strip('\n').split(',')[1].split('-')

        if(int(elf_one[0]) >= int(elf_two[0]) and int(elf_one[1]) <= int(elf_two[1])):
            counter+=1
        elif (int(elf_one[0]) <= int(elf_two[0]) and int(elf_one[1]) >= int(elf_two[1])):
            counter+=1

    return counter

# Part 2 - Find total elves that overlap with the other elves in pairs
def part_two(sections):
    counter = 0

    for elf_pair in sections:
        elf_one = elf_pair.strip('\n').split(',')[0].split('-')
        elf_two = elf_pair.strip('\n').split(',')[1].split('-')

        if(int(elf_one[0]) >= int(elf_two[0]) and int(elf_one[0]) <= int(elf_two[1])):
            counter+=1
        elif(int(elf_one[1]) <= int(elf_two[1]) and int(elf_one[1]) >= int(elf_two[0])):
            counter+=1
        elif(int(elf_two[0]) >= int(elf_one[0]) and int(elf_two[0]) <= int(elf_one[1])):
            counter+=1
        elif(int(elf_two[1]) <= int(elf_one[1]) and int(elf_two[1]) >= int(elf_one[0])):
            counter+=1

    return counter


if __name__ == "__main__":

    sections = open("input.txt").readlines()

    contains = part_one(sections)
    print("There are " + str(contains) + " pairs of evles that contain each other")

    overlaps = part_two(sections)
    print("There are " + str(overlaps) + " pairs of evles that overlap each other")