test_engine = ["467..114..",
               "...*......",
               "..35..633.",
               "......#..."
               "617*......",
               ".....+.58.",
               "..592.....",
               "......755.",
               "...$.*....",
               ".664.598.."]

with open('inputs/day_3.txt', 'r') as inputs:
    inputs = inputs.readlines()

for i in range(len(test_engine)):
        
    for j in range(len(test_engine[i])):
        #i is the row
        #j is the column
        #need to determine the length and position of a number that occurs
        #search the previous, current, and next row at the position(all indices of the number), position -1 and position +1(diagonals)
        #if any of them are not a number or a '.', then the number is part of the code
        #print(test_engine[i][j])

