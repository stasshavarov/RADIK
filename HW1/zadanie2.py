with open('text_2_var_14') as file:
    lines = file.readlines()
    
sum_lines = list()

for line in lines:
    nums = line.split(";")
    sum_line = 0
    for num in nums:
        sum_line += int(num)
        
    sum_lines.append(sum_line)
    
print(sum_lines)

with open('text_2_otvet_var_14', 'w') as file:
    for value in sum_lines:
        file.write(str(value) + '\n')