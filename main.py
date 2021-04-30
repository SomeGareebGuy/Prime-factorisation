# Prime factorisation
Var = int(input("Insert the number you want to factorise : "))
x = Var-1
factors = []
for i in range(0, Var-1):
    a = Var % x
    if a == 0:
        factors.append(x)
    x -= 1
if len(factors) == 0:
    factors.append(Var)
print("The Prime factors are : ", factors)
input()
