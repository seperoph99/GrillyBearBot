file = open("test.txt", "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()
file = open('test.txt','r')
content = file.read().splitlines()
start = 0
for i in range(line_count):
    print(content[start])
    start += 1
    input("press a key")
    

