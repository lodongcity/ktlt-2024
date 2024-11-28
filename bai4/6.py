print ("lovandong")
print ("235752021610070")

def tach_ho_ten(ten_day_du):
  """Hàm tách họ và tên riêng

  Args:
    ten_day_du: tên đầy đủ của người 

  Returns:
    Một tuple gồm họ và tên riêng
  """

  ho, ten = ten_day_du.split(maxsplit=1)

  return ho, ten

ten = input("nhập tên đầy đủ: ")

ho, ten = tach_ho_ten(ten)
print("Họ:", ho)
print("Tên:", ten)

