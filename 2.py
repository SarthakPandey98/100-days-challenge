# Day 2
# Poblem 2
# Fibonacci Even Sum
# Easy Peasy Lemon Squeezy

# Function for fibonacci series
def fib(n):

    if n <= 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

# Storing in list
result = []
terms = int(input("Number of terms"))
if terms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(terms):  
       print(fib(i))
       result.append(fib(i))

# Printing
print("list is")
for i in range(len(result)):
    print(result[i])

 #Accessing list
sum = 0
for i in range(len(result)):
    if result[i] % 2 == 0:
        sum = sum + result[i]
    else:
        i = i + 1
print("sum is")
print(sum)
