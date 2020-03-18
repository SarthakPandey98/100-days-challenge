def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)

number = int(input())
if number < 0:
    print("wrong choice")
elif number == 0:
    print("Factorial is one")
else:
    print("Factorial is",fact(number))
    number1 = fact(number)
sum = 0
print("Number is",number1)
while number1 > 0 :
    rem = int(number1 % 10)
    sum = sum + rem
    number1 = number1 / 10
print("Sum is",sum)
    
