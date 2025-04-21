s = "infoys private limiteed"
old_word = "private"
new_word = "public"

# Manual replacement
result = ""
i = 0
while i < len(s):
    # Check if the substring starting from current index matches old_word
    if s[i:i+len(old_word)] == old_word:
        result += new_word  # Add new_word to result
        i += len(old_word)  # Skip the length of old_word
    else:
        result += s[i]  # Add the current character to result
        i += 1

print("Modified string:", result)
