# Prime factorisation
Var = int(input("Insert the number you want to factorise: "))
factors = []
for i in range(2, Var-1):
    for a in range(2, i):
        if i % a == 0:
            break
    else:
        while Var > 1:
            if Var % i == 0:
                Var = Var/i
                factors.append(i)
            else:
                break
if len(factors)==0:
    factors.append(Var)
    
print("The Prime factors are :", factors)
input()
