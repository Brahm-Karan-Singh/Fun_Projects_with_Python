import random
l=["Snake","Water","Gun"]
comp=0;you=0
i=0
while(i<5):
    person=input('Enter your choice-"S for snake" "G for gun" "W for water"').lower()
    computer=random.choice(l)
    print('Your choice is',man,'and computers choice is',computer )
    if person=='s' or person=='w' or person=='g':
        if man!=computer:
            if person=='s' and computer=='Water':
                you+=1
            elif person=='s' and computer=='Gun':
                you+=1
            elif person=='g' and computer=='Snake':
                you+=1
            elif person=='g' and computer=='Water':
                you+=1
            elif person=='w' and computer=='Snake':
                you+=1
            elif person=='w' and computer=='Gun':
                you+=1
        else:
            you=you;comp=comp

    else:
        print('Please check if your input is correct or not')
        i-=1
    i+=1
if you>comp:
    print("Winner is man","Scores are- Person=",you,"Computer=",comp)
elif you<comp:
    print("Winner is computer", "Scores are- Person=", you, "Computer=", comp)
else:
    print("It is a draw")

