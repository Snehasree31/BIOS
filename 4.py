l=[]
s=[]
g=[]
n=int(input("Enter the number of students:"))
for x in range(n):
    std=input("Enter the Name:")
    grd=float(input("Enter the Grade:"))
    s.append(std)
    s.append(grd)
    l.append(s)
    g.append(grd)
    s=[]
r=max(g)
g.remove(r)
q=max(g)
for x in range(n):
    if l[x][1]==q:
        print(l[x][0]) 