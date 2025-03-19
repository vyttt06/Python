a = input("Nhập một đoạn văn bản: ")
with open("output.txt","w") as file:
          file.write(a)
print("Nội dung đã lưu thành công")
