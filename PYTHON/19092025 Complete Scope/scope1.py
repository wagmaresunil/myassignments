# 3 Palindrome number
def palindrome(num):
    temp = num
    rev = 0
    while temp>0:
        rev = rev*10 + (temp% 10)
        temp//=10
    return rev == num
num = int(input("enter a number: "))
if palindrome(num):
    print(f'{num} is a palindrome number')
else:
    print(f'{num} is not a palindrome number. ')

# # 4 Neon number
def neon(num):
    square = num*num
    total = 0
    while square>0:
        total += square %10
        square //=10
    return total == num
num = int(input("enter a number: "))
if neon (num):
    print(f'{num} is a neon number. ')
else:
    print(f'{num} is not an neon number')

# 5 perfect number
def perfect(num):
    total = 0
    for i in range(1,num):
        if num %i == 0:
            total += i
        return total == num
num = int(input("enter a number:"))
if perfect(num):
    print(f'{num} is an perfect number')
else:
    print(f'{num} is not an perfect number')