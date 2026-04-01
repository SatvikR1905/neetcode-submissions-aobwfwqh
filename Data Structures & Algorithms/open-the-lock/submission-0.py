class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0

        queue = deque(['0000'])
        visited = set(['0000'])
        turn = 0

        while queue:
            turn += 1
            for i in range(len(queue)):
                state = queue.popleft()

                for j in range(4):
                    digit = int(state[j])

                    for direction in [-1,1]:
                        new_digit = (digit + direction) % 10
                        new_state = state[:j] + str(new_digit) + state[j+1:]

                        if new_state == target:
                            return turn

                        if new_state not in visited and new_state not in dead:
                            visited.add(new_state)
                            queue.append(new_state)
        return -1
        