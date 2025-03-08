def fib_generator(n):
  if n==0 or n==1:
    return n
  else:
    return fib_generator(n-1)+fib_generator(n-2)

fib_num = int(input("Enter the number for Fibonacci Sequence: "))

print("Fibonacci Sequence: ")
for i in range(fib_num):
  print(fib_generator(i), end = " ")
