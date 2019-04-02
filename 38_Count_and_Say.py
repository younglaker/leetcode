'''
38. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

'''

def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    # Start from 1
    s = '1'
    # python allows to use _ as variable
    # Here the variable is useless, so use _
    for _ in range(n - 1):
        # At least, it has 1 number
        count = 1
        temp = []
        # print('--')
        # start from 1, prevent from overflow
        for index in range(1, len(s)):
            # print(s[index])
            if s[index] == s[index - 1]:
                count += 1
            else:
                temp.append(str(count))
                temp.append(s[index - 1])
                count = 1
        temp.append(str(count))
        temp.append(s[-1])
        s = ''.join(temp)
        # print(s)
    return s

countAndSay(0,5)