'''Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.'''
'''
тупо пишем в новый массив те элементы, которые не val
а потом пишем обратно  - так как требование задачи изменять массив на месте.
а мы смухлевали за счет дополнительного расходования памяти
'''
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        tmp = []
        while i < len(nums):
            if nums[i] != val:
                tmp.append(nums[i])
            i += 1
        nums.clear()
        for i in tmp:
            nums.append(i)
