# modes: r -read, w -write, a -append, r+ - read and write

f = open('test.txt', 'r')

print(f.name)  # test.txt
print(f.mode)  # r

f.close()
