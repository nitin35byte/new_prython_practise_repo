# class Protiviti:
#
#     def __init__(self,director_name,country_head):
#         self.__director_name=director_name
#         self.__country_head=country_head
#
#     def location(self,location):
#         self.__location=location
#
#     def get_info(self):
#         return f"Director: {self.__director_name}, Country Head: {self.__country_head}"
# class RobertHuf(Protiviti):
#
#     def __init__(self,director_name, country_head,state):
#         super().__init__(director_name,country_head)
#
#         self.state=state
#
# r=RobertHuf("puneet","tejasvi","delhi")
# r.location("delhi")
# class Protein:
#
#     def protein_bdm(self,name):
#         self.name=name
#
#     def __str__(self):
#         return f"{self.name}"
# class Proteinn(Protein):
#
#     def protein_bdm(self,weigth):
#         self.weigth=weigth
#
#     def __str__(self):
#         return f"{self.weigth}"
#
# p=Proteinn()
# p.protein_bdm("test_1")
# print(p)
# arr=[2,3,4,5,6,7]
# left=0
# right=len(arr)-1
# while left < right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left +=1
#     right-=1
#
# print(arr)

p="nitin"
c="nishant"
find="i"
for index,char in enumerate(c):
    if find==char:
        print(index)
        break 