DS = list(map(int, input("Nhập danh sách các số nguyên:").split()))
so_can_xoa = int(input("Nhập số cần xóa:"))
if so_can_xoa in DS:
    DS.remove(so_can_xoa)
    print(F"Danh sách sau khi xóa:",DS)
else:
    print(f"Số {so_can_xoa} không có trong danh sách")
