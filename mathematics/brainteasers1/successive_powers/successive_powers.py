from sympy import isprime
powers = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
basis = [x for x in range(100,1000) if isprime(x)]
#pour chacun des modulo possible
for p in basis:
    #pour chacun des x dans ce modulo
    for x in range(1,p):
        #i est l'index, power est la valeur à l'index
        for i,power in enumerate(powers):
            #si on est a la dernier valeur du tableau, on a trouvé notre solution
            if i==len(powers)-1:
                print('crypto{',p,',',x,'}',sep='')
            elif not (x*power)%p==powers[i+1]: break
