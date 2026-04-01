class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        boats=0

        while left <= right:
            if people[left]+people[right] <= limit: # we pair the heaviest with the smallest
                boats += 1
                left += 1
                right -= 1
            else:
                boats += 1
                right -= 1
        return boats


        
        