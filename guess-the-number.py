#guess what is the number I have hidden
#letus start

n=34
m=0
guesses = 5
win=0

while(m != n and guesses>0):
    m=int(input('write any number you think is the solution '))
    guesses=guesses-1
    if(m<n):
        print('your number is small, guess again, guesses left = '+str(guesses))
        continue
    elif(m>n):
        print('your number is big, guess again ')
        continue
    else:
        win=1
        print("correct guess! you won the game, congratulations! ")
        break

if(win==0):
    print('sorry! you have lost the game!')


