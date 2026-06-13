with open("yunomi1.msh", "r") as f:
	lines = f.readlines()
lines_rstrip = [line.rstrip("\n") for line in lines]
print(lines_rstrip)
print(len(lines_rstrip))
print(lines_rstrip[0])
a=lines_rstrip[0].split(" ")
b=[int(a[0]),int(a[1]),int(a[2])]
print(b)
c=lines_rstrip[1:b[0]+1]
d=lines_rstrip[b[0]+1:b[0]+b[1]+1]
e=lines_rstrip[b[0]+b[1]+1:b[0]+b[1]+b[2]+1]
print(len(c))
print(c[0]);print(c[len(c)-1])
print(len(d))
print(d[0]);print(d[len(d)-1])
print(len(e))
print(e[0]);print(e[len(e)-1])