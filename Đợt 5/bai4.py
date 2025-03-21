d = ["LAN", "CÂY", "NHỎ"]
print("DANH SÁCH KÝ TỰ TRƯỚC KHI SẮP XẾP: ", d)
for i in range(len(d)):
    for j in range(len(d) - 1):
        if d[j] > d[j + 1]:
            d[j], d[j + 1] = d[j + 1], d[j]
print("DANH SÁCH KÝ TỰ SAU KHI SẮP XẾP: ", d)
