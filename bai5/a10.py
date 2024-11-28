print("lô văn đồng")
print("235752021610070")
import bubble_sort

n = int(input("Nhập số lượng phần tử: "))
nlist = []
for i in range(n):
  element = int(input(f"Nhập phần tử thứ {i+1}: "))
  nlist.append(element)

bubble_sort.bubble_sort(nlist)

print("Danh sách sau khi sắp xếp:", nlist)
