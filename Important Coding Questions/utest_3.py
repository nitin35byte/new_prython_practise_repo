# from selenium import webdriver
#
#
# driver = webdriver.Chrome()
# driver=driver.get("")
# select=Select(driver)
# select= driver.find_element(By.Xpath , "")
# select.by_visisble_text("apple")
# select.b
#

a = 'nitin'
b = []
print(len(a))
for i in range(len(a)-1 , -1 , -1):
    b.append(a[i])
print(''.join(b))

if a ==a[::-1]:
    print("reversed")
else:
    print("no revr")

a="hcl technoogy limited"
word=a.split()

stack=[]
for i in word:
    stack.append(i)

print(stack)
char=[]
while stack:
    char.append(stack.pop())

print(char)
p=[]
for i in range(len(word)):
    print(p.append(word[i][::-1]))
print(p)
b="".join(h for h in word if h.isalnum())
t={}
for i in b:
    if i in t:
        t[i]+=1
    else:
        t[i]=1
print(t)
r="".join(f"{count}{value}" for count, value in t.items())
print(r)


def test_pass(a,b, result):
    return a+b==result


def test_pp():
    assert test_pass(1,2,3)
