'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''

'''
По сути разворачиваем строку и все и сравниваем с исходной
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        if x_str == x_str[::-1]: 
            return(True)
        else:
            return(False)




        
