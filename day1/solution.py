# Advent of Code 2022 - Day 1

# Function to sort, count and split calories between each elves inventory
def get_sorted_inventories(inventories):
    elves = []
    calories = 0

    for snack in inventories:
        if(snack != "\n"):
            calories += int(snack)
        else:
            elves.append(calories)
            calories = 0
    
    elves.sort()
    elves.reverse()

    return elves

# Part 1 - Find the elf carrying the most calories
def part_one(inventories):
    return max(get_sorted_inventories(inventories))

# Part 2 - Find the sum of the callaries the top 3 elves are carrying
def part_two(inventories):
    return sum(get_sorted_inventories(inventories)[:3])


if __name__ == "__main__":

    inventories = open("input.txt").readlines()

    callories = part_one(inventories)
    print("The elf carrying the most calories is carrying " + str(callories) + " calories.")

    top_three_callories = part_two(inventories)
    print("The 3 elves carrying the most calories are carrying " + str(top_three_callories) + " calories in total.")