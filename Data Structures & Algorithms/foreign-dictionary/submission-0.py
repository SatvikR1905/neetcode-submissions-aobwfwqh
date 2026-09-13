from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Collect all unique letters
        graph = defaultdict(set)
        all_letters = set()
        for word in words:
            for c in word:
                all_letters.add(c)

        # Step 2: Build the graph
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    graph[c1].add(c2)
                    break
            else:
                if len(word1) > len(word2):
                    return ""

        # Step 3: Create states for DFS
        WHITE, GRAY, BLACK = 0, 1, 2
        state = {letter: WHITE for letter in all_letters}
        order = []
        has_cycle = False

        # Step 4: DFS
        def dfs(letter):
            nonlocal has_cycle
            state[letter] = GRAY
            for neighbor in graph[letter]:
                if state[neighbor] == GRAY:
                    has_cycle = True
                    return
                if state[neighbor] == WHITE:
                    dfs(neighbor)
            state[letter] = BLACK
            order.append(letter)

        # Step 5: Run DFS for every letter
        for letter in all_letters:
            if state[letter] == WHITE:
                dfs(letter)
            if has_cycle:
                break

        # Step 6: Check for cycle
        if has_cycle:
            return ""
        return "".join(order[::-1])