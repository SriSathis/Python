from random import randint

min = 1

roll_again = 'y'

while roll_again is 'y':
    max_num = input('How many sides should be on the dice?')
    max=int(max_num)
    dice = int(input('How many dice should we roll?'))
    print('''OK then, rolling...
    ...and your numbers are:''')
    for number in range(0,dice):
        number_current=randint(min,max)
        print(number_current)
    roll_again=input('Would you like to roll again?')