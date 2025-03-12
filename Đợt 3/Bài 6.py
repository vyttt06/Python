DS = list(map(int, input("Nhập danh sách các số nguyên:").split()))
Sap_xep = sorted(set(DS),reverse = True)
if len(Sap_xep) < 2:
    print("Không đủ số để tìm số lớn thứ hai")
else:
    print("Số lớn thứ hai là:", Sap_xep[1])
