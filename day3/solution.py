# Advent of Code 2022 - Day 3

# Part 1 - Total priority of common items in compartments within rucksacks
def part_one(rucksacks):
    
    priorities = []

    for rucksack in rucksacks:
        compartment_one = list(rucksack)[:len(list(rucksack))//2]
        compartment_two = list(rucksack)[len(list(rucksack))//2:]
        common_item = list(set(compartment_one).intersection(compartment_two))[0]
        priority = ord(common_item)-38 if common_item.isupper() else ord(common_item)-96
        priorities.append(priority)

    return sum(priorities)

# Part 2 - Total priority of common items in rucksacks within groups
def part_two(rucksacks):

    rucksack_groups = [rucksacks[x:x+3] for x in range(0, len(rucksacks), 3)]
    priorities = []

    for group in rucksack_groups:
        rucksack_one = group[0].strip("\n")
        rucksack_two = group[1].strip("\n")
        rocksack_three = group[2].strip("\n")
        common_item = list(set(list(set(rucksack_one).intersection(rucksack_two))).intersection(rocksack_three))[0]
        priority = ord(common_item)-38 if common_item.isupper() else ord(common_item)-96
        priorities.append(priority)

    return sum(priorities)


if __name__ == "__main__":

    rucksacks = open("input.txt").readlines()

    priority = part_one(rucksacks)
    print("The priority of all common items between compartments in rucksacks is: " + str(priority))

    priority = part_two(rucksacks)
    print("The priority of all common items between groups of rucksacks is" + str(priority))