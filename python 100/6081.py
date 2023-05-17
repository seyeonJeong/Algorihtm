
n = input()
n = int(n,16)

for i in range(1,16):
    calc = n*i
    calc = format(calc,'x').upper()
    print(format(n,'x').upper(),'*',format(i,'x').upper(),'=',calc,sep='')