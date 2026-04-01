class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i , h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                idx , ht = stack.pop()
                area = ht * (i-idx)
                max_area = max(max_area , area)
                start = idx
            stack.append((start,h))
        for idx , ht in stack:
            max_area = max(max_area, ht*(len(heights) - idx))
        return max_area
