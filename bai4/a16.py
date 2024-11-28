print ("lovandong")
print ("235752021610070")

def in_va_xuat_so_nhi_phan():
  chuoi_nhap = input("Nhập chuỗi các số nhị phân (cách nhau bởi dấu phẩy): ")

  danh_sach_so_nhi_phan = chuoi_nhap.split(",")

  print("Các số nhị phân bạn đã nhập là:")
  for so_nhi_phan in danh_sach_so_nhi_phan:
      print(so_nhi_phan)

in_va_xuat_so_nhi_phan()
