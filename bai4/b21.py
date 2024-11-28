print ("lovandong")
print ("235752021610070")

def kiem_tra_chia_het_cho_5(chuoi_nhiphan):
 
  so_nhiphan_list = chuoi_nhiphan.split(',')

  ket_qua = []
  for so in so_nhiphan_list:
    so_nguyen = int(so, 2)  
    if so_nguyen % 5 == 0:
      ket_qua.append(so)

  return ', '.join(ket_qua)

chuoi_nhap = input("Nhập chuỗi các số nhị phân 4 chữ số (cách nhau bởi dấu phẩy): ")

ket_qua = kiem_tra_chia_het_cho_5(chuoi_nhap)
print("Các số nhị phân chia hết cho 5 là:", ket_qua)
