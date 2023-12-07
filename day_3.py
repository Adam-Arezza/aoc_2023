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

for i in range(len(inputs)):
    inputs[i] = inputs[i].replace("\n", ".")

dot_row = "".join(["." for i in inputs[0]])
inputs.append(dot_row)
inputs.insert(0, dot_row)

for i in range(len(inputs)):
    inputs[i] += "."
    inputs[i] = "." + inputs[i]
sum = 0
part_numbers = []
valid_in_row = [[] for i in range(len(inputs))]

def search(arr, row, num):
    symbol = False
    start_ind = arr[row].find(num)
    start_col = start_ind - 1
    start_row = row - 1
   
    for r in range(3): 
        for c in range(len(num) + 2):
            try:
                check_row = start_row + r
                check_col = start_col + c
                #if check_row < 0 or check_col < 0 or check_col > len(arr[0]) - 1 or check_row > len(arr) - 1:
                #    continue
                check_cell = arr[check_row][check_col]
                if check_cell != "." and check_cell != "\n" and not check_cell.isdigit():
                    symbol = True
                    part_numbers.append(num)
                    valid_in_row[row].append(num)
            except:
                print(check_row)
                print(check_col)

for i in range(len(inputs)):
    current_sub_str = ""
    for j in range(len(inputs[i])):
        if inputs[i][j].isdigit():
           current_sub_str += inputs[i][j]
        else:
            if len(current_sub_str) > 0:
                start = inputs[i].find(current_sub_str,0)
                search(inputs, i, current_sub_str)
                current_sub_str = ""

for n in part_numbers:
    sum += int(n)
print(part_numbers)
print(sum)

for i in range(len(valid_in_row)):
    print(valid_in_row[i])
    print(inputs[i-1])
    print(inputs[i])
    print(inputs[i+1])
    print("\n")

#guesses 536795,532672,530799,
#error rows
# ....16....371........*.....-........*...........=..........202..........373.....6.749............28................*....675.....529............
# 
