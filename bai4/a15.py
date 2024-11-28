print ("lovandong")
print ("235752021610070")

def sap_xep_tu_theo_tu_dien():
  
  chuoi_nhap = input("Nhập các từ tiếng Anh (cách nhau bởi dấu cách): ")

  cac_tu = chuoi_nhap.split()

  cac_tu.sort()

  print("Các từ sau khi sắp xếp:")
  for tu in cac_tu:
    print(tu)

sap_xep_tu_theo_tu_dien()
