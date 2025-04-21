f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())

# f=open("test.txt", 'a')
# f.write("i have a test plan to do thsi")
#
# f.close()
#
# f=open("test.txt","r")
# print(f.read())

with open('demofile2.txt' , 'r') as f:
    content = f.read()
    print(content)