DS = list(map(int, input("Nhập danh sách các số nguyên:").split()))
so_chan = [so for so in DS if so % 2 == 0]
print(f"Danh sách các số chẵn:",so_chan)
