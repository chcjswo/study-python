import pickle # (객체, 텍스트) 직렬화, 역직렬화

bfilename = 'C:\\Users\\User\\workspace\\study-python\\section4\\test.bin'
tfilename = 'C:\\Users\\User\\workspace\\study-python\\section4\\test.txt'

data1 = 77
data2 = 'Hello World'
data3 = ["car", "apple", "house"]

# 바이너리 쓰기
with open(bfilename, 'wb') as f:
    pickle.dump(data1, f) # dumpss (문자열 직렬화)
    pickle.dump(data2, f)
    pickle.dump(data3, f)


# 텍스트 쓰기
with open(tfilename, 'wt') as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3))

# 바이너리 읽기
with open(bfilename, 'rb') as f:
    b = pickle.load(f) # loads (문자열 역직렬화)
    print(type(b), 'Binary Read1 | ', b)
    b = pickle.load(f)
    print(type(b), 'Binary Read2 | ', b)
    b = pickle.load(f)
    print(type(b), 'Binary Read3 | ', b)

# 텍스트 읽기
with open(tfilename, 'rt') as f:
    for i, line in enumerate(f, 1):
        print(type(line), 'Text Read' + str(i) + ' | ', line, end='')
