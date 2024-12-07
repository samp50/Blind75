class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # create a hashmap to store index and values of needed target
        for index, item in enumerate(nums):
            diff = target - item
            if diff in prevMap:
                return [prevMap[diff], index] # add 
            prevMap[item] = index # notice it is stored as item, index