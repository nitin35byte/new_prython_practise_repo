# a = "My Name is Nitin"
#
# # for i in range(len(a)-1 , -1,-1):
# #    # print(a[i])
# #
#
# b = a.lower().split()
# word = []
# for i in range(len(b)-1 , -1,-1):
#     word.append(b[i])
#
# print(word)

# import openpyxl
# workbook=openpyxl.load_workbook("testdata.xlxs")
# seet= workbook["sheet1"]
#
# max_row=sheet.max_row
# max_column = sheet.max_column
#
# for i in range(2 , max_row+1):
#     print(i.value)

a = "My Name is Nitin".split()
b =list(a)
left =0
right = len(a)-1

while left <right:
    b[left] , b[right]=b[right] , b[left]
    left +=1
    right-=1

print(b)




def missnumber(arr):
    miss_no=[]
    for i in range(arr[0] , arr[-1] +1):
        if  i not in arr:
            if i%2!=0:
                miss_no.append(i)
    return  miss_no

arr=[1,3,5,6,9]
print(missnumber(arr))

p="my name is nitin".split()
o=[]
for i in range(len(p)):
    o.append(p[i][::-1])

print(" ".join(o))

for i in range(len(p)-1,-1,-1):
    print(p[i])
