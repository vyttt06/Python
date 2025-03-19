try:
    with open("output.txt","r", encoding="utf-8")as file:
        content = file.read()
    print("Nội dung trong file:")
    print(content)
except FileNotFoundError:
    print("Lỗi: File không tồn tại")
