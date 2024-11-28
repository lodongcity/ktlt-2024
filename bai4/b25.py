print ("lovandong")
print ("235752021610070")

def loc_so_le(danh_sach_so):

  so_le = []
  for so in danh_sach_so:
    if so % 2 != 0:
      so_le.append(so)
  return so_le

chuoi_so = input("Nhập danh sách các số (cách nhau bởi dấu phẩy): ")

danh_sach_so = [int(so) for so in chuoi_so.split(',')]

ket_qua = loc_so_le(danh_sach_so)
print("Các số lẻ là:", ket_qua)
