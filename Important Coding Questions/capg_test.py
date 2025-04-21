a='hcl technologies'
b=a.split()
word =[]
for i in range(len(b)-1 , -1 , -1):
	word.append(b[i])
print(word)
a = 'hcl technologies'
b = a.split()
word = []

# Reverse each word individually
for i in range(len(b)):
    word.append(b[i][::-1])  # Reverse each word

# Join the reversed words back into a string
result = " ".join(word)
print(result)

vowels='aeiouAEIOU'
a = 'hcl technologies'
for i in a:
	if i in vowels:
		b=a.replace(i,'z')
	print(b)

if b==b[::-1]:
	print("palindrome")
else:
	print("not apalindrome")
	# a = hcl
	# technologies
	# 1.
	# reverse
	# text
	#
	# 2.
	# replace
	# vowels
	# with z
	# 	3.
	# 	identify
	# 	duplicate
	# 	letter
	#
	# 1.
	# a = 'hcl technologies'
	# b = a
	# word = []
	# for i in range(len(b) - 1, -1, -1):
	# 	word.append(b[i])
	# print(word)
	# lch
	# se
	#
	# vowels = [a, e, i, o, u, A, E, I, O, U]
	#
	# for i in a:
	# 	if vowels in i:
	# 		i.replace(vowels, 'z')
	#
	# d = {}
	# for i in a:
	# 	if i in d:
	# 		d[i] += 1
	# else:
	# 	d[i] = 1
	#
	# seen = set()
	# for i, char in enumerate(s):
	# 	if char in seen:
	# 		return s[:i] + s[i + 1]
	# seen.add(char)
	#
	#
	#
