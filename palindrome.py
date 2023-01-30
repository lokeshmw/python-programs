# number
n = 545
temp = n
rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if temp == rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

# string
name = "madam"
reverse = ""
for i in name:
    reverse = i + reverse  # concatenation
if name == reverse:
    print('The number is a palindrome!')
else:
    print("The number isn't a palindrome!")
