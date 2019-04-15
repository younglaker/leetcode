class Solution:
    def singleNumber(self, s1, s2):
        i=0
        j=0
        count = 0
        while j < len(s2):
            while i < len(s1):
                print(s2[j])
                print(j)
                print(s1[i])
                print(i)
                print('===')
                if s1[i] == s2[j] and i < len(s1)-1 and j < len(s2)-1:
                    i += 1
                    j += 1
                else:
                    i += 1
            # print(s2[j])
            if j < len(s2) and s2[j] not in s1:
                return -1
            elif j < len(s2):
                i = 0
                j += 1
                count += 1
        return count



a =Solution()
b =a.singleNumber('abc', 'acbcba')
print('b=%d' % b)