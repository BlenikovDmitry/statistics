'''
Given a roman numeral, convert it to an integer.
'''
'''
создаем словарь предзаполненный
идем по строке с конца и если текущее число больше или равно предыдущего, то мы его прибавляем
если меньше - отнимаем
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        prev = 0
        for s1 in reversed(s):
            curr = roman_map[s1]
            if curr >= prev:
                total += curr
            else:
                total -= curr
            prev = curr
        return total
        
