#read lines from the file

fh= open("lines.txt")
for line in fh.readlines():
    print(line, end="")