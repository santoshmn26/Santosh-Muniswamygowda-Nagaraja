import csv
f=open("D:\Bro code\FInal AI.txt",'a')
n=1
while(n!=10):
    nick_name=input('Enter the link Nick name: ')
    f.write(nick_name+",")
    path_name=input('Enter the Path for the Nick name: ')
    f.write(path_name+"\n")
    n+=1
f.close()
dict1=dict()
with open("D:\Bro code\FInal AI.txt",'r') as f:

    for row in f:
        print(row)
        if(row is not "\n"):
            row=row.rstrip()
            row=row.split(",")
            dict1.update({row[0]:row[1]})
print(dict1)


