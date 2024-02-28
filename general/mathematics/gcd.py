a = int(input('enter a number: '))
b = int(input('another one: '))


def gcd(a,b):
    res = []
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            res.append(i)
    
    return max(res)
res = gcd(a,b)
print('GCD: ', res)