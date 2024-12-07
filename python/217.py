class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {} # create a dictionary to hold key, value pairs 
        #for numbers and instances, respectively
        for num in nums:
            if num in nums_dict:
                return True # when number is encountered, duplicate found
            else:
                nums_dict[num] = +1 # increment value when certain didgit found
        return False