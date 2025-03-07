a = int(input("Nhập số nguyên thứ nhất:"))
b = int(input("Nhập số nguyên thứ hai:"))
tong = a + b
hieu = a - b
tich = a * b
if b != 0:
    thuong = a/b
else:
    thuong = ("Không thể chia")
Luy_thua = pow(a,b) 
print(f"Tổng của a và b = ",tong)
print(f"Hiệu của a và b = ", hieu)
print(f"Tích của a và b = ", tich)
print(f"Thương của a và b = ", thuong)
print(f"Lũy thừa của a mũ b = ", Luy_thua)


