var1 = input("nhan vao chuoi so ")
print(var1)
a,b,c,d,e='','','','',''
m=0
c=[a,b,c,d]
for i in var1:
    if m == 4:
        break;
    if i!=' ' :
        e=e+i
    if i == ' ' or i == var1[var1.__len__()-1]:
        c[m]=e
        m=m+1
        e=''
print(c)




