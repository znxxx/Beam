def twoSum(nums, target):
    #use dict to prevent there is duplicate different
    ans = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        #when the first answer is already in the dict, the current diff must be other answer
        if diff in ans:
            return [ans[diff],i]
        #if the diff not in nums since the beginning, return empty set
        elif diff not in ans and diff not in nums:
            return []
        else:
            #insert first answer and it's index to ans dict
            ans[nums[i]] = i

