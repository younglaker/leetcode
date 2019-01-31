def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    s = '1'
    # python允许下划线作为变量。因为这里没用到这个变量，所以用一个符号就可以了
    for _ in range(n - 1):
        count = 1
        temp = []
        print('--')
        for index in range(1, len(s)):
            print(s[index])
            if s[index] == s[index - 1]:
                count += 1
            else:
                temp.append(str(count))
                temp.append(s[index - 1])
                count = 1
        temp.append(str(count))
        temp.append(s[-1])
        s = ''.join(temp)
        print(s)
    return s

countAndSay(0,5)