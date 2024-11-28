print ("lovandong")
print ("235752021610070")

def loai_bo_chu_so(chuoi):

  chuoi_moi = ""
  for ky_tu in chuoi:
    if not ky_tu.isdigit():
      chuoi_moi += ky_tu
  return chuoi_moi

chuoi_nhap = input("Nhập một chuỗi: ")

chuoi_ket_qua = loai_bo_chu_so(chuoi_nhap)
print("Chuỗi sau khi loại bỏ chữ số:", chuoi_ket_qua)
  
