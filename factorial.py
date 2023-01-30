num = 3
factorial = 1
if num == 0:
    print("please enter positive numbers")
else:
    for i in range(1, num+1):
        factorial = factorial * i
print(factorial)