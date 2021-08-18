with  open("qqwry gbk.dat","rb") as file:
        a =file.read()
print(a)

with open("1.txt","w") as file:
    file.write(str(a))
