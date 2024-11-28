print ("lô văn đồng")
print ("235752021610070")

import math

def Tinh(R):

  if R <= 0:
    return "Bán kính phải là số dương"

  chu_vi = 2 * math.pi * R
  dien_tich = math.pi * R**2
  return chu_vi, dien_tich

R = float(input("Nhập bán kính hình tròn: "))

ket_qua = Tinh(R)
if isinstance(ket_qua, str):
  print(ket_qua)
else:
  print("Chu vi:", ket_qua[0])
  print("Diện tích:", ket_qua[1])
