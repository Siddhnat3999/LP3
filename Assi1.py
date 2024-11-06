def recursive(n,steps):
    steps[0]+=1
    if n<=1:
        return n
    else:
        return recursive(n-1,steps)+recursive(n-2,steps)
def iterative(n,steps):
    a=0
    b=1
    if n<=1:
        return n
    else:
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
            steps[0]+=1
        return c
n=int(input("Enter a number:"))
steps_resursive=[0]
steps_iterative=[0]
res_recursive=recursive(n,steps_resursive)
res_iterative=iterative(n,steps_iterative)
print(f"Fibonnaci number of {n} is {res_recursive} by recursion")
print(f"Steps for recursion {steps_resursive[0]}")
print(f"Fibonnaci number of {n} is {res_iterative} by Iteration")
print(f"Steps for iteration {steps_iterative[0]}")