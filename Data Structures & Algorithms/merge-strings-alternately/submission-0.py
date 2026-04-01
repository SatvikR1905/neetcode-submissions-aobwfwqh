class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mer=[]
        left1, left2=0, 0
        right_one, right_two=len(word1), len(word2)
        while left1 < right_one and left2 < right_two:
            mer.append(word1[left1])
            mer.append(word2[left2])
            left1 += 1
            left2 += 1
        mer.append(word1[left1:])
        mer.append(word2[left2:])
        return ''.join(mer)
        