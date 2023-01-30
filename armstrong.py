# abc = a**n + b**n = c**n
# n = 3 here because abc is of 3 size
# find armstrong number
num = 153
n = 0
for i in str(num):
    n += 1
# n = len(str(num))# len(num)
summ = 0
temp = num
while temp > 0:
    a = temp % 10
    summ += a ** n
    temp = temp // 10

if num == summ:
    print("its arms-tong")
else:
    print('not a armstrong')
