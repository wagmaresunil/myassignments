# 1 automorphic
def automorphic(num):
    square = num * num
    temp = num
    while temp>0:
        if square %10 != temp%10:
            return False
        square//=10
        temp//=10
    return True
num = int(input("enter a number:"))
if automorphic(num):
    print(f'{num} is an automorphic number.')
else:
    print(f'{num} is not an automorphic number')

def automorphic(num):
    return str(num* num).endswith(str(num))
num =int(input("enter a number: "))
if automorphic(num):
    print(f'{num} is an automorphic number. ')
else:
    print(f'{num} is not an automorphic number')

#2 Armstrong
def armstrong(num):
    temp = num
    count = 0
    while temp != 0:
        count+=1
        temp//=10
    temp =num
    total =0
    while temp>0:
        digit = temp %10
        total +=digit ** count
        temp //= 10
    return total == num
num = int(input("enter a number:"))
if armstrong(num):
    print(f'{num} is an armstrong number.')
else:
    print(f'{num} is not an armstrong number. ')