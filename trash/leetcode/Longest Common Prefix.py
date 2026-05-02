'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
'''
Сортируем список по возрастанию и делаем срез в каждой строке от 0 элемента до длины самой короткой строки(первой)
Загоняем в список tmp
Преобразуем список в множество, если множество состоит из 1 элемента - решение найдено
Если нет - уменьшаем длину на 1 элемент
Если длина уже стала 0 - значит наибольшей общей подстроки нет.
'''
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        tmp = []
        counter = len(strs[0])
        while counter > 0:
            for i in strs:
                #tmp.append(i[0:len(strs[0])-4])
                tmp.append(i[0:counter])

            if len(set(tmp)) == 1:
                return tmp[0]
            else:
                tmp = []
                counter -= 1
        if counter == 0:
            return ''

'''
Проверочные тесты
'''
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))
print(sol.longestCommonPrefix(["flower","flow","f"]))

