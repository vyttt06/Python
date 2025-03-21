c = [44, 55, 73, 20, 15, 54, 27]
print("DANH SÁCH TRƯỚC KHI SẮP XẾP: ", c)
hoan_doi = 0
for i in range(len(c)):
    for j in range(len(c) - 1):
        if c[j] > c[j + 1]:
            c[j], c[j + 1] = c[j + 1], c[j]
            hoan_doi +=1
print("DANH SÁCH SAU KHI SẮP XẾP: ", c)
print("SỐ LẦN HOÁN ĐỔI TRONG QUÁ TRÌNH SẮP XẾP: ", hoan_doi)

        
