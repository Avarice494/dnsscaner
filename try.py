k = 0
# def int3(data, offset):
#     global k
#     print(data)
#     # k +=1
#     return data[offset] + (data[offset+1] << 8) + \
#            (data[offset+2] << 16)

def int4(data, offset):
    print("no1:"+str((data[offset])))
    print((data[offset]))

    print("no2:"+str((data[offset+1])))
    print((data[offset+1]) << 8)

    print("no3:"+str((data[offset+2])))
    print((data[offset+2]) << 16)

    print("no4:"+str((data[offset+3])))
    print((data[offset+3]) << 24)

    return data[offset] + (data[offset+1] << 8) + \
           (data[offset+2] << 16) + (data[offset+3] << 24)


with open("qqwry gbk.dat","rb") as file:
    buffer=file.read()

index_begin = int4(buffer, 8)
# print("begin:"+str(index_begin))
index_end = int4(buffer,16)
# print("end:"+str(index_end))
# for i in range(0,888):
#     ip_begin = int4(buffer, index_begin + i * 7)
#     offset = int3(buffer, index_begin + i * 7 + 4)
#     print(int4(buffer, index_begin + i * 7))