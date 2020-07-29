# 1. Sum the numbers
# nums = [1, 2, 3, 4, 5]
# count = 0
# for num in nums:
#     count += num
# print(count)


# 2. Largest Number
# nums = [1, 2, 12, 2, 3]
# larger_number = 0
# for num in nums:
#     if num >= larger_number:
#         larger_number = num
# print(larger_number)


# # 3. Smallest Number
# nums = [1, 2, 12, 2, 3]
# small_number = nums[0]
# for num in nums:
#     if num <= small_number:
#         small_number = num
# print(small_number)


# 4. Even Numbers
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums = []
# for num in nums:
#     if num % 2 == 0:
#         even_nums.append(num)
# print(even_nums)


# # 5. Positive Numbers
# nums = [-1, 5, 9, -45, -36, 0]
# greater_than_zero = []
# for num in nums:
#     if num > 0:
#         greater_than_zero.append(num)
# print(greater_than_zero)


# 6. Positive Numbers II
nums = [-1, 5, 9, -45, -36, 0]
positive_nums = []
for num in nums:
    if num >= 0:
        positive_nums.append(num)
print(positive_nums)
