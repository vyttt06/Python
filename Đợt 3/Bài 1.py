DS = list(map(int, input("NHập danh sách các số nguyên:").split()))
tong = sum(DS)
trungbinh = tong/len(DS)
print(f"Tổng các số nguyên =",tong)
print(f"Trung bình các số nguyên =",trungbinh)
