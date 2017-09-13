def persistence(n):
    c=0
    if(n>9):
        while(n>9):
            pre=1
            for i in str(n):
                pre = pre * int(i)
            c += 1
            if(pre>9):
                n=pre
            else:
                break
        return(c)
    else:
        return(0)

print(persistence(39))
