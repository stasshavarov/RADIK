import math

with open('text_3_var_14') as file:
    lines = file.readlines()

matrix = list()

for line in lines:
    nums = line.strip().split(',')
    for i in range(len(nums)):
        if nums[i] == 'NA':
            nums[i] = str((int(nums[i-1]) + int(nums[i+1])) / 2)
            
    filtered = list()
    for item in nums:
        num = float(item)
        if num >= 0 and math.sqrt(num) > 64:
            filtered.append(num)

    matrix.append(filtered)

with open('text_3_otvet_var_14', 'w') as file:
    for row in matrix:
        for num in row:
            file.write(str(num) + ',')
        file.write('\n')