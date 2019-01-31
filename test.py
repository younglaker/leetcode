class Solution:
    def multiply(self, num1, num2):
        """
    :type num1: str
    :type num2: str
    :rtype: str
    """
        # 把两个字符串反转
        num1 = num1[::-1]
        num2 = num2[::-1]
        # 将每位互乘的结果用一维数组存储，先填充该数组
        arr = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i + j] += int(num1[i]) * int(num2[j])
        a = []
        for i in range(len(arr)):
            digit = arr[i] % 10  # digit表示这一位的数字
            carry = arr[i] / 10  # carry表示加给下一位的数
            if i < len(arr) - 1:
                arr[i + 1] += carry  # 下一位加上
            a.insert(0, str(digit))  # 更新a
        while a[0] == '0' and len(a) > 1:  # 去除首位为0的情况
            del a[0]

        print(''.join(a))
        return ''.join(a)  # 连接成字符串

a =Solution()
a.multiply('123','456')