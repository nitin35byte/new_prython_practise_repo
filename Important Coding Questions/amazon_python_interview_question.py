emp_list= [('Ankit' , 10000) , ('Nitin',12000) , ('Rahul' , 15000) , ('Sumit' , 14000) , ('Dheeraj' , 21000) , ('Pavan' , 11000) , ('Mohit' , 13000)]
re=sorted(emp_list , key=lambda x: x[1] , reverse=True)
print(re)
def get_avg_salary(x):
    total_salary=0
    for name , salary in emp_list:
        total_salary= total_salary+salary
    return total_salary/len(emp_list)


avg_salary= get_avg_salary(emp_list)
print(avg_salary)

my_list=[]
for name , salary in emp_list:
    if salary > avg_salary:
        my_list.append((name,salary))


## i need to do same task in SQL wit emplyees database


print(my_list)

a = sorted(emp_list , key=lambda x:x[1] , reverse=True)
print(a)