print ("lo van dong")
print ("235752021610070")

import math

def benefit(t, n, k):
  interest_rate = t / 100

  total_amount = n * math.pow(1 + interest_rate, k)

  return total_amount

t = float(input("Nhập lãi suất hàng tháng (t%): "))
n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi: "))

result = benefit(t, n, k)
print("Số tiền nhận được sau", k, "tháng là:", result)
