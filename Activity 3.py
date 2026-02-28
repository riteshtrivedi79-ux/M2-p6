def factorial(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    return(f"the factorial of {a} is {f}")
num=int(input("enter the number - ")) 
print(factorial(num))