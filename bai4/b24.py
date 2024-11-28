print ("lovandong")
print ("235752021610070")

def dem_chu_hoa_thuong(cau):

  so_chu_hoa = 0
  so_chu_thuong = 0

  for ky_tu in cau:
    if ky_tu.isupper():
      so_chu_hoa += 1
    elif ky_tu.islower():
      so_chu_thuong += 1

  print("Chữ hoa:", so_chu_hoa)
  print("Chữ thường:", so_chu_thuong)

cau = input("Nhập một câu: ")

dem_chu_hoa_thuong(cau)
