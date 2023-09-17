from sys import stdin

operations = ['+', '-', '*', '/']

def Value(i1, i2, i3):
    minimum = None
    for op in operations:
        res1 = Evaluate(i1, i2, op)
        if res1 is not None:
            for op in operations:
                res2 = Evaluate(res1, i3, op)
                if res2 is not None and res2 >= 0:
                    minimum = res2 if (minimum is None or res2 < minimum) else minimum
    return minimum

def Evaluate(i1, i2, op):
    if op == '+':
        return i1 + i2
    elif op == '-':
        return i1 - i2
    elif op == '*':
        return i1 * i2
    elif i1 % i2 == 0:
        return i1 / i2
    return None

nums = [int(x) for x in stdin.readline().split(' ')]

print(Value(nums[0], nums[1], nums[2]))