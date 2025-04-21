class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        boats = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1

        return boats

solution= Solution()
people=[1,2,3,3]
limit=3
obj=solution.numRescueBoats(people,limit)
print(obj)

