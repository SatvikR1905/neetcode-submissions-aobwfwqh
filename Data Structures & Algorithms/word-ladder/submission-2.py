class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList) #creating a set ogf wordlists
        if endWord not in wordset:
            return 0

        queue = deque([beginWord]) #queue to add the words
        visited = set([beginWord])
        count = 1 # its the level which we are in 

        while queue:
            count += 1# after cat we are going to next level to explore more words
            for i in range(len(queue)):
                word = queue.popleft() 

                for j in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:j] + c + word[j+1:] #create a new combination of word to match with endword

                        if newWord == endWord:
                            return count

                        if newWord in wordset and newWord not in visited:
                            visited.add(newWord)
                            queue.append(newWord)
        return 0

        