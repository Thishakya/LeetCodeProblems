class Solution(object):
    def twoSum(self, nums, target):
        retArry = []
        for idx_i, i in enumerate(nums):
            for idx_j, j in enumerate(nums):
                if ((i+j) == target) and (idx_i != idx_j):
                    retArry.insert(0, idx_i)
                    retArry.insert(1, idx_j)
                    return retArry


ans = Solution()
print(ans.twoSum([3, 3], 6))

# print(ans.twoSum([2, 7, 11, 15], 9))

# print(ans.twoSum([3, 2, 4], 6))


"""
This program doest work because the function "index()" always gets the index of the first occurence of an element in the list
if there are multiple occurences of an element.

class Solution(object):
    def twoSum(self, nums, target):
        retArry = []
        for i in nums:
            for j in nums:
                if ((i+j) == target) and (nums.index(i) != nums.index(j)):
                    retArry.insert(0, nums.index(i))
                    retArry.insert(1, nums.index(j))
                    return retArry


ans = Solution()
print(ans.twoSum([3, 3], 6))


"""
