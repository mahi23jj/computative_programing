def factorial(x):
    if x==1:
       # print(x)
        return 1
    else:
        y=factorial(x-1)
        return y+1
    
print(factorial (5))    