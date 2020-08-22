import random
n=int( random.random()*50 )                   #Generating a random no.
print('Enter any guess between 1 and 50')
print('You are having only 5 guesses so choose smartly:')
x=4                                            #No.of guesses left
while(x>=0):
    inp=int(input())                          #Taking input
    i=0

   #Checking conditions
    if inp<n:
        if x>0:
            print('The number chosen is lesser', '(',x,'guesses are left )')
        else:
            print('The number chosen is lesser')
    elif inp>n:
        if x>0:
             print('The number chosen is greater', '(', x, 'guesses are left )')
        else:
            print('The number chosen is greater')
    else:
        print('Congratulations you guessed correct number with', x ,'guesses left')
        i=i+1
        break
    x=x-1

if(i==0):
    print('Game over :(')
    print('The number was',n)

