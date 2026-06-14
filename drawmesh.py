import matplotlib.pyplot as plt
def adjustFigAspect(fig,aspect=1):
    '''
    Adjust the subplot parameters so that the figure has the correct
    aspect ratio.
    '''
    xsize,ysize = fig.get_size_inches()
    minsize = min(xsize,ysize)
    xlim = .4*minsize/xsize
    ylim = .4*minsize/ysize
    if aspect < 1:
        xlim *= aspect
    else:
        ylim /= aspect
    fig.subplots_adjust(left=.5-xlim,
                        right=.5+xlim,
                        bottom=.5-ylim,
                        top=.5+ylim)

with open("yunomi1.msh", "r") as f:
	lines = f.readlines()
lines_rstrip = [line.rstrip("\n") for line in lines]
#print(len(lines_rstrip))
#print(lines_rstrip[0])
a=lines_rstrip[0].split(" ")
b=[int(a[0]),int(a[1]),int(a[2])]
#print(int(a[0])+int(a[1])+int(a[2])+1)
#print(b)
c=lines_rstrip[1:b[0]+1]
d=lines_rstrip[b[0]+1:b[0]+b[1]+1]
e=lines_rstrip[b[0]+b[1]+1:b[0]+b[1]+b[2]+1]
#print(len(c))
#print(c[0]);print(c[len(c)-1])
#print(len(d))
#print(d[0]);print(d[len(d)-1])
#print(len(e))
#print(e[0]);print(e[len(e)-1])
p=[]
for i in range(0,len(c)):
  temp=c[i].split(" ")
  p.append([float(temp[0]),float(temp[1])])
tr=[]
for i in range(0,len(d)):
  temp=d[i].split(" ")
  tr.append([int(temp[0]),int(temp[1]),int(temp[2]),int(temp[0])])
#print(tr)
vt=[]
for i in range(0,len(e)):
  temp=e[i].split(" ")
  vt.append([int(temp[0]),int(temp[1]),int(temp[2])])
#print(vt)
#p2=[]
#for i in range(0,len(tr)):
#  p2.append([p[tr[i][0]],p[tr[i][1]],p[tr[i][2]],p[tr[i][3]]])
x=[];y=[]
for i in range(0,len(p)):
  x.append(p[i][0])
  y.append(p[i][1])
fig = plt.figure()
adjustFigAspect(fig,aspect=.25)
plt.scatter(x,y,s=.1)
plt.show()  
