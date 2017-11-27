def tickets(people):
    cash=list()
    for i in range(len(people)):
        cash1=people[i]
        change = people[i]-25
        if(change!=0):
            if(change==(25)) &(25 in cash):
                d = cash.index(25)
                del cash[d]
                cash.append(people[i])
                continue
            elif(change==(75)) &(sum(cash)>=75) & (cash.count(25)>0):
                d = cash.index(25)
                del cash[d]
                if(50 in cash):
                    d=cash.index(50)
                    del cash[d]
                    cash.append(people[i])
                    continue
                elif(cash.count(25)>=2):
                    d=cash.index(25)
                    del cash[d]
                    del cash[d]
                    cash.append(people[i])
                    continue
                else:
                    return("NO")
            else:
                return("NO")
        cash.append(people[i])
        continue
    else:
        return("YES")

print(tickets([25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 100, 100, 100, 100]))

