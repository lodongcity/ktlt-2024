print ("lovandong")
print ("235752021610070")

def fibonacci(n):

  fib = [0, 1]
  while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])
  return fib[:-1]

n = int(input("Nhập số nguyên dương n: "))

ket_qua = fibonacci(n)
print("Các số Fibonacci nhỏ hơn", n, "là:", ket_qua)
