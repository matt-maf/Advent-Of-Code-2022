# Advent of Code 2022 - Day 2

# Part 1 - Total score if column 2 is my move
def part_one(strategy_guide):
    myScore = 0

    for game in strategy_guide:
        opponent, me = game.split()

        if me == "X": 
            myScore += 1
            myScore += 3 if opponent == "A" else 0 if opponent == "B" else 6
        elif me == "Y": 
            myScore += 2
            myScore += 6 if opponent == "A" else 3 if opponent == "B" else 0
        elif me == "Z": 
            myScore += 3
            myScore += 0 if opponent == "A" else 6 if opponent == "B" else 3
    
    return myScore

# Part 2 - Total score if column 2 is the result
def part_two(strategy_guide):
    myScore = 0

    for game in strategy_guide:
        opponent, result = game.split()

        if result == "X": 
            myScore += 3 if opponent == "A" else 1 if opponent == "B" else 2
        elif result == "Y": 
            myScore += 3
            myScore += 1 if opponent == "A" else 2 if opponent == "B" else 3
        elif result == "Z": 
            myScore += 6
            myScore += 2 if opponent == "A" else 3 if opponent == "B" else 1
    
    return myScore


if __name__ == "__main__":

    strategy_guide = open("input.txt").readlines()

    score = part_one(strategy_guide)
    print("My score would be " + str(score) + " if column 2 is my move.")

    score = part_two(strategy_guide)
    print("My score would be " + str(score) + " if column 2 is the result.")