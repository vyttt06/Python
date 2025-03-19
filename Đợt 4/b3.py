file = open("multiline.txt","w")
vb_count = 0
while True:
    vb = input("Nhap mot dong hoac Stop(de dung):")
    if vb == "Stop":
        break
    file.write(vb +"\n")
    vb_count +=1
print(f"So vong da ghi vao file: {vb_count}")
file.close()
