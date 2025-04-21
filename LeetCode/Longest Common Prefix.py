class Solution(object):
    def longestCommonPrefix(self, strs):
        commonprefix=""
        # if not strs:
        #     return commonprefix

        minstr=min(strs)
        maxstr=max(strs)

        len_of_minstr= len(minstr)
        len_of_maxstr = len(maxstr)

        for i in range(len_of_minstr):
            if minstr[i] == maxstr[i]:
                commonprefix +=minstr[i]
            else:
                break
        return commonprefix

object=Solution()
strs = ["frleower", "frltow", "frleight"]

print(object.longestCommonPrefix(strs))