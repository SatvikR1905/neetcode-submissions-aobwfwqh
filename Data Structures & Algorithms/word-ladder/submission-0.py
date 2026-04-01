class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
            
        queue = deque([beginWord])
        visited = set([beginWord])
        count = 1

        while queue:
            count += 1
            for i in range(len(queue)):
                word = queue.popleft()

                for j in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:j] + c + word[j+1:]

                        if newWord == endWord:
                            return count

                        if newWord in wordset and newWord not in visited:
                            visited.add(newWord)
                            queue.append(newWord)
        return 0

        