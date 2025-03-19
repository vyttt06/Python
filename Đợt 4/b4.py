try:
    with open("multiline.txt","r") as file:
        So_dong = 0
        So_tu = 0
        So_ky_tu = 0
        for dong in file:
            So_dong +=1
            So_tu += len(dong.split())
            So_ky_tu += len(dong)
        print(f"Số dòng:",So_dong)
        print(f"Số từ:",So_tu)
        print(f"Số ký tự:",So_ky_tu)
except FileNotFoundError:
    print("Lỗi: File không tồn tại.")
