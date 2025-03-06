def kiem_tra_chan_le(n):
    if n % 2 ==0 :
        return(f"{n} là số chẵn")
    else:
        return(f"{n} là số lẻ")
def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            return False
        return True
def kiem_tra_hoan_hao(n):
    if n <= 1:
        return False
    tong_uoc_so = 0
    for i in range (1, n):
        if n % i == 0:
            tong_uoc_so += i
    if tong_uoc_so == n:
        return True
    return False
n = int(input("Nhập n:"))
print(kiem_tra_chan_le(n))
if kiem_tra_nguyen_to(n):
    print("Số nguyên tố")
else:
    print("Không phải là số nguyên tố")
if kiem_tra_hoan_hao(n):
    print("Số hoàn hảo")
else:
    print("Không phải số hoàn hảo")
    
    
