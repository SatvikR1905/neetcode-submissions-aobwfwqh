class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {} #creating a hashmap to order the letters of alien language
        for i , c in enumerate(order):
            order_map[c] = i

        for i in range(len(words) - 1): #comparing 2 words at once
            word1 = words[i]
            word2 = words[i+1]

            for j in range(len(word1)):
                if j >= len(word2): # this indicates second word in the list is a prefix
                    return False

                if word1[j] != word2[j]:
                    if order_map[word1[j]] > order_map[word2[j]]:
                        return False
                    break    

        return True
        