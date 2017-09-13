def divisors(integer):
    res=list()
    c=0
    for i in range(2,integer):
        if(integer%i==0):
            res.append(i)
            c=1
    if(c!=1):
        x= str(integer) + " is prime"
        return(x)
    else:
        return(res)
print(divisors(13))