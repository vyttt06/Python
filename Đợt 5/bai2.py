b = [ 34, 21, 67, 24, 9, 16, 67]
print("DANH SÁCH TRƯỚC KHI SẮP XẾP: ", b)
for i in range(len(b)):
    for j in range(len(b) - 1):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]
print("SỐ LỚN NHẤT: ", b[-1])
print("SỐ BÉ NHẤT: ", b[0])
