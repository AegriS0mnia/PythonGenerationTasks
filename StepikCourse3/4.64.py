number = int(input())
victim = int(input())
nums = [i for i in range(1, number + 1)]

while len(nums) > 1:
    for i in range(0, victim - 1):
        nums.append(nums[i])
    del nums[:victim]

print(*nums)
