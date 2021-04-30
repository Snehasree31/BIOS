str=input("Enter the alphanumeric string: ")
l_case=[]
u_case=[]
o_num=[]
e_num=[]

s=sorted(str)
for i in s:
    if i .islower():
        l_case.append(i)
    elif i .isupper():
        u_case.append(i)
    elif int(i)%2==0:
        e_num.append(i)
    else:
        o_num.append(i)
l_case=''.join(l_case)
u_case=''.join(u_case)
o_num=''.join(o_num)
e_num=''.join(e_num)
print(l_case+u_case+o_num+e_num)
