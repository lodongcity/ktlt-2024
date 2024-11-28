print ("lovandong")
print ("235752021610070")

def tim_so_chan_toan_chu_so(a, b):

  ket_qua = []
  for num in range(a, b+1):
    so_chuoi = str(num)
    if all(int(chu_so) % 2 == 0 for chu_so in so_chuoi):
      ket_qua.append(num)

  return ', '.join(map(str, ket_qua))

ket_qua = tim_so_chan_toan_chu_so(1000, 3000)
print(ket_qua)
