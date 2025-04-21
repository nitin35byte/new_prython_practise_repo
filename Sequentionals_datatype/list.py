# Lists are used to store multiple items in a single variable.
#List items are ordered, changeable, and allow duplicate values.

#List items are indexed, the first item has index [0], the second item has index [1] etc.
#List is a collection which is ordered and changeable. Allows duplicate members.
#lists are mutale
list1 = ["abc", 34, True, 40, "male"]

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


##TUPLE

#Tuple is immutable
# Tuples are used to store multiple items in a single variable.

#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple , 34 , 12.5")
print(type(thistuple))
print(thistuple)
