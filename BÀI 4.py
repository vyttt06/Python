def kiem_tra_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5)+ 1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập n:"))
tong = 0
for i in range(1, n+1, 2):
    tong+= i
if tong > 1000:
    print("Tổng quá lớn")
elif kiem_tra_nguyen_to(tong):
    print("Tổng là số nguyên tố")
elif tong % 7 == 0:
    print("Tổng chia hết cho 7")
print(f"Tổng các số lẻ từ 1 đến {n} là: {tong}")
