nums = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9,]
unique_nums = []

for num in nums:
    if nums.count(num) == 1:
        unique_nums.append(num)
        print(unique_nums)