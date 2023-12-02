#PART 1
with open('.\inputs\day_1.txt', 'r') as inputs:
    inputs = inputs.readlines()
 
#test_strings = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

result_list = []
for line in inputs:
    digits = []
    for ch in line:
        if ch.isdigit():
            digits.append(ch)
    if len(digits) > 0:
        num = ""
        num += str(digits[0])
        num += str(digits[-1])
        result_list.append(num)

sum = 0
for n in result_list:
    sum += int(n)

print(sum)

#PART 2
#test_strings = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
number_map = {"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
num_from_str = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

result_list = []

for line in inputs:
    digits = []
    for ch in line:
        if ch.isdigit():
            line = line.replace(ch, number_map[ch])
    sub_string_order = []
    for i in number_map:
        if number_map[i] in line:
            subs_count = line.count(number_map[i])
            last_ind = 0
            for s in range(subs_count):
                sub_start = line.find(number_map[i],last_ind)
                sub_end = sub_start + len(number_map[i])
                #print(f'{sub_start}, {sub_end}')
                sub_string_order.append([sub_start, number_map[i]])
                last_ind = sub_end
    if len(sub_string_order) > 1:
        sub_string_order.sort()
        #print(sub_string_order)
    for i in sub_string_order:
        digits.append(num_from_str[i[1]])
    #print(line)
    #print(digits)
    if len(digits) > 0:
        num = ""
        num += str(digits[0])
        num += str(digits[-1])
        result_list.append(num)
sum = 0
for n in result_list:
    sum += int(n)
print(sum)
