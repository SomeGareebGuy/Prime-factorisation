# Prime factorisation
Var = int(input("Insert the number you want to factorise: "))
factors = []
for i in range(1, Var):
        x = Var%i
        if x==0:
            factors.append(i)
print("The Prime factors are :", factors)
input()
