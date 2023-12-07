test_engine = ["467..114..",
               "...*......",
               "..35..633.",
               "......#...",
               "617*......",
               ".....+.58.",
               "..592.....",
               "......755.",
               "...$.*....",
               ".664.598.."]

with open('inputs/day_3.txt', 'r') as inputs:
    inputs = inputs.readlines()

#add a . border around the grid so boundaries aren't needed when searching
for i in range(len(inputs)):
    inputs[i] = inputs[i].replace("\n", ".")

dot_row = "".join(["." for i in inputs[0]])
inputs.append(dot_row)
inputs.insert(0, dot_row)

for i in range(len(inputs)):
    inputs[i] += "."
    inputs[i] = "." + inputs[i]

#PART ONE
sum = 0
part_numbers = []
gears = {} 

def search(arr, row, num, start_ind):
    symbol = False
    start_col = start_ind - 1
    start_row = row - 1
    star_found = False
    star_location = None

    for r in range(3): 
        for c in range(len(num) + 2):
            try:
                check_row = start_row + r
                check_col = start_col + c
                check_cell = arr[check_row][check_col]
                if check_cell != "." and check_cell != "\n" and not check_cell.isdigit():
                    symbol = True
                    part_numbers.append(num)
                    if check_cell == "*":
                        star_found = True 
                        star_location = [check_row, check_col]
            except:
                pass
    if star_found:
        gear_keys = list(gears.keys())
        star_location = str(star_location)
        if star_location not in gear_keys:    
            gears[star_location] = []
        gears[star_location].append(num)

for i in range(len(inputs)):
    current_sub_str = ""
    for j in range(len(inputs[i])):
        if inputs[i][j].isdigit():
            current_sub_str += inputs[i][j]
        else:
            if len(current_sub_str) > 0:
                search(inputs, i, current_sub_str, j-len(current_sub_str))
                current_sub_str = ""

for n in part_numbers:
    sum += int(n)
print(sum)
#guesses 536795,532672,530799,530812,530806, 529618
#error rows
# ....16....371........*.....-........*...........=..........202..........373.....6.749............28................*....675.....529............


#PART 2
gear_partnums = []
gear_sum = 0

for gear in gears:
    if len(gears[gear]) == 2:
        gear_partnums.append(int(gears[gear][0]) * int(gears[gear][1]))

for g in gear_partnums:
    gear_sum += g
print(gear_sum)
