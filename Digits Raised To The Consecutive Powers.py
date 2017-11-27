def sum_dig_pow(a, b):
    c,res,sum1=1,list(),0
    for i in range(a,b+1):
        sum1,c=0,1
        for j in str(i):
            sum1=sum1+(int(j)**c)
            c+=1
        if(sum1==int(i)):
            res.append(int(i))
    return(res)
print(sum_dig_pow(89, 135))