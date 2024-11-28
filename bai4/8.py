print ("lovandong")
print ("235752021610070")

def tim_tu_dai_nhat(danh_sach_tu):
    do_dai_lon_nhat = len(max(danh_sach_tu, key=len))
    cac_tu_dai_nhat = [tu for tu in danh_sach_tu if len(tu) == do_dai_lon_nhat]
    print("các từ dài nhất:", cac_tu_dai_nhat)

day_tu = input("nhập dãy từ (cách nhau bởi dấu cách): ").split()
tim_tu_dai_nhat(day_tu)
