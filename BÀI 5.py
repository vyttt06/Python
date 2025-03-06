so_nguyen = list(map(int, input("Nhập danh sách số nguyên:").split()))
print("Danh sách ban đầu:", so_nguyen)
Sap_xep = sorted(so_nguyen)
print("Danh sách sau khi sắp xếp tăng dần:", Sap_xep)
Sap_xep = sorted(so_nguyen, reverse = True)
print("Danh sách sắp xếp sau khi giảm dần:", Sap_xep)
lon_nhat = max(so_nguyen)
nho_nhat = min(so_nguyen)
print("SỐ lớn nhất trong danh sách:", lon_nhat)
print("SỐ nhỏ nhất trong danh sách:", nho_nhat)


