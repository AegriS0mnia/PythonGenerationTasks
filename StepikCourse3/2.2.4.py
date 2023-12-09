nums = [i for i in input().split()]
filtered_nums = ' '.join(sorted(set(filter(lambda num: nums.count(num) > 1, nums)), key=int))

print(filtered_nums)