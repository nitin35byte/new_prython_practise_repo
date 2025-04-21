class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])


obj = Solution()

s = "hello World My Nane is Nit"

result = obj.lengthOfLastWord(s)
print(result)

s = "   Hello   World!    "




## Captilizing first word of string
word = s.strip().split()

last_word = word[-1]
lenth= len(last_word)
print("lenth of thw word is:",lenth)

text = input("Enter text: ")

words = text.split()
for i in range(len(words)):
    words[i] = words[i][0].upper() + words[i][1:].lower()

modified_text = ' '.join(words)
print(modified_text)