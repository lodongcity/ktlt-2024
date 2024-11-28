print ("lovandong")
print ("235752021610070")


def tim_so_co_tong_uoc_lon_hon(n):
  
  print("Các số nguyên dương nhỏ hơn", n, "có tổng các ước số lớn hơn chính nó:")

  for i in range(1, n):
    tong_uoc = 1  
    for j in range(2, i//2 + 1):
      if i % j == 0:
        tong_uoc += j + i // j
    if tong_uoc > i:
      print(i)

n = int(input("Nhập số nguyên dương n: "))

tim_so_co_tong_uoc_lon_hon(n)
