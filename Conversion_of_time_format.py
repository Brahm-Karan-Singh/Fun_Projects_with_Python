s=input()
time=int(s[:2])
no='00'
for x in range(0,1):
    if s[8:10]=='PM':
        if time==12 and int(s[3:5])>0:
            time=12
        else:
            time = time + 12
    elif s[8:10]=='AM':
        if time<12:
            time=s[:2]
        else:
            time=no
    else:
        print('wrong statement')
print(str(time)+s[2:8])