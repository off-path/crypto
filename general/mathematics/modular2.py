# a=11
# m=6

a=273246787654**65536
p=65537
notPrime=False

def checkPrime(p,notPrime):
    for i in range(2, p):
        if p % i == 0:
            return False
    return True

checkPrime(p,notPrime)
if a % p != 0:
    #Theoreme de Fermat
    #si p est primaire et a n'est pas divisible par b, alors % = 1
    if a % p == 1:
        print(a%p)