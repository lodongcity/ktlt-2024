import tiden

def main():
  numbers = []
  n = int(input("Nhập số lượng phần tử: "))
  for i in range(n):
    num = int(input("Nhập phần tử thứ {}: ".format(i+1)))
    numbers.append(num)

  sorted_numbers = tiden.selection_sort(numbers)
  max_num, min_num = tiden.find_max_min(sorted_numbers)

  print("Danh sách đã sắp xếp:", sorted_numbers)
  print("Phần tử lớn nhất:", max_num)
  print("Phần tử nhỏ nhất:", min_num)

if __name__ == "__main__":
  main()
