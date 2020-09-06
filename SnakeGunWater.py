import random
l=["Snake","Water","Gun"]
comp=0;mard=0
i=0
while(i<5):
    man=input('Enter your choice-"S for snake" "G for gun" "W for water"').lower()
    computer=random.choice(l)
    print('Your choice is',man,'and computers choice is',computer )
    if man=='s' or man=='w' or man=='g':
        if man!=computer:
            if man=='s' and computer=='Water':
                mard+=1
            elif man=='s' and computer=='Gun':
                comp+=1
            elif man=='g' and computer=='Snake':
                mard+=1
            elif man=='g' and computer=='Water':
                comp+=1
            elif man=='w' and computer=='Snake':
                comp+=1
            elif man=='w' and computer=='Gun':
                mard+=1
        else:
            mard=mard;comp=comp

    else:
        print('Please check if your input is correct or not')
        i-=1
    i+=1
if mard>comp:
    print("Winner is man","Scores are- Man=",mard,"Computer=",comp)
elif mard<comp:
    print("Winner is computer", "Scores are- Man=", mard, "Computer=", comp)
else:
    print("It is a draw")

