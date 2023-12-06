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
sum = 0
part_numbers = []
def search_for_symbol(arr, row_ind, start, end):
    symbol = False
    steps = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for i in range(start, end + 1, 1):
        print(f'substring index: {i}')
        for s in steps:
            try:
                step = arr[row_ind + s[0]][i+ s[1]]
                if row_ind + s[0] < 0:
                    continue
                if i + s[1] < 0:
                    continue
                print(f'position checked: {row_ind + s[0]},{i + s[1]}')
                print(f'found: {step}')
                if step != "." and not step.isdigit():
                    symbol = True
                    print("symbol found")
                    break
            except Exception as e:
                print(e)
    return symbol

digit_ss = []                
for i in range(len(inputs)):
    current_sub_str = ""
    for j in range(len(inputs[i])):
        if inputs[i][j].isdigit():
           current_sub_str += inputs[i][j]
        else:
            if len(current_sub_str) > 0:
                start = inputs[i].find(current_sub_str,0)
                sub_string_info = {"value":current_sub_str,
                                   "row": i,
                                   "range": [start, start + len(current_sub_str)-1]
                               }
                digit_ss.append(sub_string_info)
                current_sub_str = ""
                symbol_found = search_for_symbol(inputs, sub_string_info["row"], sub_string_info["range"][0], sub_string_info["range"][1])
                if symbol_found:
                    sum += int(sub_string_info["value"])
                    part_numbers.append(sub_string_info["value"])

for line in inputs:
    print(line)
#print(digit_ss)
print(part_numbers)
print(sum)
#guesses 536795,532672,
