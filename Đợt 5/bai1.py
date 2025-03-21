a = [23, 56, 99, 31, 76]
print("Danh sách trước khi sắp xếp: ", a)
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j +1], a[j]
print("Danh sách sau khi sắp xếp: ", a)

        
    

