import matplotlib.pyplot as plt
import math
x=[2,8,7,6,4]
y=[5,4,5,4,9]
clx=[2,5,1]
cly=[10,8,2]
c1x,c2x,c3x=list(),list(),list()
c1y,c2y,c3y=list(),list(),list()
centroids=list()
centroids1=list()
centroids2=list()
j=0
for i in range(len(x)):
    centroids.append(int(math.sqrt(((x[i]-clx[j])**2)+((y[i]-cly[j])**2))))
j+=1
for i in range(len(x)):
    centroids1.append(int(math.sqrt(((x[i]-clx[j])**2)+((y[i]-cly[j])**2))))
j+=1
for i in range(len(x)):
    centroids2.append(int(math.sqrt(((x[i]-clx[j])**2)+((y[i]-cly[j])**2))))
print("",centroids,"\n",centroids1,"\n",centroids2)
for i in range(len(centroids)):
    if((centroids[i]<centroids1[i])&(centroids[i]<centroids2[i])):
        c1x.append(x[i])
        c1y.append(y[i])
    elif((centroids1[i]<centroids[i])&(centroids1[i]<centroids2[i])):
        c2x.append(x[i])
        c2y.append(y[i])
    else:
        c3x.append(x[i])
        c3y.append(y[i])
c1x.append(clx[0])
c1y.append(cly[0])
c2x.append(clx[1])
c2y.append(cly[1])
c3x.append(clx[2])
c3y.append(clx[2])
print(c1x,c1y,c2x,c2y,c3x,c3y)
plt.plot(x, y,'ro')
plt.plot(clx,cly ,'ro',color='green')
plt.axis([0, 12, 0, 12])
plt.show()

nc1x,nc1y,nc2x,nc2y,nc3x,nc3y=0,0,0,0,0,0
if(len(c1x)!=0):
    nc1x=int(sum(c1x)/len(c1x))
    nc1y=int(sum((c1y))/len(c1y))
    plt.plot(c1x, c1y, 'ro', color="red")
if(len(c2x)!=0):
    nc2x=int(sum(c2x)/len(c2x))
    nc2y=int((sum(c2y))/len(c2y))
    plt.plot(c2x, c2y, 'ro', color="green")

if(len(c3x)!=0):
    nc3x=int(sum(c3x)/len(c3x))
    nc3y=int((sum(c3y))/len(c3y))
    plt.plot(c3x, c3y, 'ro', color="black")

plt.axis([0,12,0,12])
plt.show()
print(nc1x,nc1y,nc2x,nc2y,nc3x,nc3y)
plt.plot(nc1x, nc1y, 'ro', color="red")
plt.plot(nc2x,nc2y,'ro', color="green")
plt.plot(nc3x,nc3y,'ro', color="black")

plt.axis([0, 12, 0, 12])
plt.show()
plt.plot(nc1x, nc1y, 'ro', color="red")
plt.plot(nc2x,nc2y,'ro', color="green")
plt.plot(nc3x,nc3y,'ro', color="black")
plt.plot(c1x, c1y, 'ro', color="green")
plt.plot(c2x, c2y, 'ro', color="green")
plt.plot(c3x, c3y, 'ro', color="black")
plt.axis([0, 12, 0, 12])
plt.show()



