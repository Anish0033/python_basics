# while loops
print('enter the number')
number=int(input())

while(number>6):
    print("yes")
    number=int(input())
    if(number<6):
        break
    if number==12:
        continue
    print('loop ended')
