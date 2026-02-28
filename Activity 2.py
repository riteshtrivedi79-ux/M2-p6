def cube(a):
    return(a**3)
def divisiblity(a) :
    if a%3==0 :
        return("divisible")
    else :
        return("not divisible")
num=int(input("enter the number - "))
print(f"the cube of {num} is {cube(num)} and it is {divisiblity(num)}")