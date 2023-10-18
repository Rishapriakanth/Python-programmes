import random
snake={40:3,27:5,43:18,54:31,66:45,76:68,89:53,95:84,99:41}
ladder={4:25,8:29,33:49,50:69,42:63,62:81,67:86,65:97}
x=0
y=0
flag=1
while(x!=100 and y!=100):
    x1=random.randint(1,6)
    if flag==1:
        if(x+x1>100):
            flag=0
            print("Player 1:",x)
        else:
            x=x+x1
            if x in snake.keys():
                x=snake[x]
                print("OOPS! , a snake")
            if x in ladder.keys():
                x=ladder[x]
                print("WHOO! , a ladder")
            print("Player 1:",x)
            flag=0
    else:
        if(y+x1 > 100):
            flag=1
            print("Player 2:",y)
        else:
            y=y+x1
            if y in snake.keys():
                y=snake[y]
                print("OOPS! , a snake")
            if y in ladder.keys():
                y=ladder[y]
                print("WHOO! , a ladder")
            print("Player2:",y)
            flag=1
if x==100:
    print('Player 1 is the winner')
else:
    print('Player 2 is the winner')