#Function for calculating the Factorial of a number 

def Fact(x):
    fact=1
    for i in range(x):
        fact=fact*(i+1)
    return fact

#Function for calculating if a number is a factorial or not, returns root if it is a factorial.

def IsFact(y):
    fact=1
    count=1
    while fact < y:
        fact=fact*count
        count=count+1
    if fact==y:
        return count-1
    else:
        return "-1"

