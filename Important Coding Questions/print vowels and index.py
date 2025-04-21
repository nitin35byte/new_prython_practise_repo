cha = "Hi Nitin how are you?"
vowels = "aeiouAEIOU"

for index, char in enumerate(cha):  # Iterate over characters with their index
    if char in vowels:
        print(f"Vowel '{char}' found at index {index}")