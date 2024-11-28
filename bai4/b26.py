def tinh_so_tien_thuc(sodu_ban_dau, giao_dich):
   
    sodu_thuc_te = sodu_ban_dau
    
    for gd in giao_dich:
        sodu_thuc_te += gd
    
    return sodu_thuc_te


def main():
    sodu_ban_dau = float(input("Nhập số dư ban đầu của tài khoản: "))
    
    giao_dich = []
    print("Nhập các giao dịch (nhập 'x' để kết thúc):")
    
    while True:
        giao_dich_input = input("Nhập giao dịch: ")
        
        if giao_dich_input.lower() == 'x':
            break
        
        try:
            giao_dich.append(float(giao_dich_input))
        except ValueError:
            print("Lỗi: Vui lòng nhập một số hợp lệ!")
    
    so_tien_thuc = tinh_so_tien_thuc(sodu_ban_dau, giao_dich)
    
    print(f"Số tiền thực tế trong tài khoản là: {so_tien_thuc:.2f} VND")

if __name__ == "__main__":
    main()
