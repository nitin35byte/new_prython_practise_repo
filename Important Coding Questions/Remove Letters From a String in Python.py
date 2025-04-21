test_str ="Nitin"
str_tes=" "

for i in range(len(test_str)):
    if i !=2:
        str_tes = str_tes + test_str[i]
print(str_tes)

l = [1 , 2 , 3 ,1 , 4 , 5 ,1 , 5 , 1]

x = [i for i in l if i!=1] +[i for i in l if i==1]
print(x)
#
# for i in test_str:
#     if i!=2:
#         str_tes += test_str[i]
#         print(str_tes)

###INTERVIEW ASKED QUESTION
a = 'infosys private limited'
replace_word = 'public'

# Split the string into words
words = a.split()

# Initialize an empty list to hold the modified words
result = []

# Iterate through each word
for word in words:
    if word == 'private':
        result.append(replace_word)  # Replace the word
    else:
        result.append(word)  # Keep the word unchanged

# Join the words back into a single string
new_string = ' '.join(result)

print(new_string)
