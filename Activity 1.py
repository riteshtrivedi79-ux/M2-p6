def total(bill,tip_percentage):
    return(bill+((tip_percentage/100)*bill))
a=int(input("enter the bill amount - "))
b=int(input("enter the tip percentage you would like to leave - "))
print("total bill amount including tip would be - ", total(a,b))
    