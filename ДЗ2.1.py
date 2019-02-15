n=int(input())
if n <=1 or n >100:
    print()
elif n % 2 == 1:
    print('Weird')
elif n % 2 ==0 and n >1 and n <6:
    print("Not Weird")
elif  n % 2 ==0 and n>5 and n < 21:
    print ('Weird')
elif  n % 2 ==0 and n>20:
    print ('Not Weird')
