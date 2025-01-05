# menghitung faktorial

total = 1
num = 4
while num > 0:
    if num == 4:
        print(num, "! =", end=(' '))
    if num != 1:
        print (num ,"x", end=(' '))
    else:
        print("1 = ", end=(''))
    
    total *= num
    num -= 1

print(total)

# num = 4
# total = 1
# for i in range(1, num+1):
    
#     total *= i

# print(total)