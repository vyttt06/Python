try:
    with open("multiline.txt","r") as a:
        nd = a.read()
    with open("copy.txt","w") as b:
        b.write(nd)
    print("Sao chép nội dung thành công")
except FileNotFoundError:
    print("Lỗi: File không tồn tại.")
