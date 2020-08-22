#Faulty calculations are:
# 56+7=77 , 45*4=528 , 112/6=5
x='y'
while x=='y':         #Running the loop while the condition is true

    #Taking inputs
    a=int(input('Enter first number:'))
    o=input('Which operation you want to do- (+,-,*,/):')
    b=int (input('Enter second number:'))

    #Conditions
    if a==56 and b==7 and o=='+':
        print('77')
    elif a==45 and b==4 and o=='*':
        print('528')
    elif a==112 and b==6 and o=='/':
        print('5')
    elif o=='+':
        print(a+b)
    elif o=='-':
        print(a-b)
    elif o=='/':
        print(a/b)
    elif o=='*':
        print(a*b)
    else:
        print('Please check whether you have entered inputs correctly or not')
    x=input('Do you want to make one more opeation- y/n: ')