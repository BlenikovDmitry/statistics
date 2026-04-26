from collections import deque
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

'''
реализуем через deque и поэтому сложность O(1)
если встречаем открывающуюся скобку - просто кладем в стек
если встречаем закрывающуюся скобку - смотрим, есть ли на вершине стека открывающаяся такого же вида(выталкиваем послений попавший в стек элемент)
если нет - то False
если при этом стек пуст, то False
если после всех манипуляций стек пустой - значит True - последовательность корректная
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        str_ = s
        for i in str_:
            if i == '(':
                stack.append(i)
            if i == ')':
                if not stack:
                    return False
                if stack and stack.pop() != '(':
                    return False

            if i == '{':
                stack.append(i)
            if i == '}':
                if not stack:
                    return False
                if stack and stack.pop() != '{':
                    return False

            if i == '[':
                stack.append(i)
            if i == ']':
                if not stack:
                    return False
                if stack and stack.pop() != '[':
                    return False
        if stack:
            return False
        else:
            return True
