loop = 0
while loop < 10:
    n = input('What are you thinking?')

    n = int(n)

    if n % 2 == 0:
        print('That\s an even number! Have another?')
    else:
        print("That's an odd number! Have another?")
    
    loop += 1