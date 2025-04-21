from collections import Counter


# 1. Merge Two Dictionaries and Sum Values of Common Keys
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'a': 5, 'b': 15, 'd': 25}
result= dict(Counter(dict1) + Counter(dict2))
print(result)
dict1.update(dict2)
print(f"shasasajsas{dict1}")
#Find the Key with the Maximum Value
max_key=max(dict1,key=dict1.get)
print(max_key)

data = {'A': 50, 'B': 20, 'C': 100, 'D': 80}
#Sort a Dictionary by Values

sort_data=dict(sorted(data.items() , key=lambda item:item[0]))
print(sort_data)

#Convert Two Lists into a Dictionary
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
result = dict(zip(keys, values))
print(result)
result={key:dict1.get(key, 0) + dict2.get(key , 0) for key in set(dict1) |set(dict2)}
print(f"pass pass{result}")

#sort dictionary
d = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_dict)

#find common key in both the dictionary

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 40}

common_keys = set(dict1.keys()) & set(dict2.keys())
print(common_keys)
