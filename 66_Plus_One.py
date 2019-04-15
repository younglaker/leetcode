def plusOne(digits):
    carry = 1
    # range(start, stop, step)
    for i in range(len(digits) - 1, -1, -1):
        # divmod(): takes two numbers and returns a pair of numbers consisting of their quotient and remainder, (x / y , x % y)

        # carry = int( digits[i] + carry / 10 )
        # digits[i] = int( digits[i] + carry % 10 )
        carry, digits[i] = divmod(digits[i] + carry, 10)
        if carry == 0:
            return digits

    result = []
    # wrong: result[0] = 1
    result.append(1)
    for i in range(1, len(digits)+1 ):
        result.append(digits[i-1])

    return result

def plusOne2(digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        carry, digits[i] = divmod(digits[i] + carry, 10)
        if carry == 0:
            return digits

    # or: digits.insert(0,1)
    return [1] + digits

def plusOne3(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # max: 1+9=10, only 0
        digits[i] = 0
    return [1] + digits

print(plusOne2([9,9,9]))