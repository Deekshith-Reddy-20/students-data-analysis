nums=[1,2,3,4,5,7]
target=7
for i in range(len(nums)):
    for j in range(i+1, len(nums)):

        if nums[i] + nums[j] == target:
            print([nums[i],nums[j]])