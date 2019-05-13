import random
r = random.randint(1, 100)
count = 0
while True:
    count += 1               #count = count + 1
    num = input('plz guess a number: ')
    num = int(num)
    if num == r:
        print('Correct!')
        print ('This is your', count, 'time to take trying')
        break
    elif num > r:
        print('Larger...')
    elif num < r:
        print('Smaller...')
    print ('This is your', count, 'time to take trying')