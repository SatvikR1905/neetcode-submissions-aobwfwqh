class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n =len(temperatures)
        result = [0] * n
        for i in range (n):
            while stack and temperatures[i] > stack[-1][-1]:
                prev_index , prev_temp = stack.pop()
                days = i - prev_index
                result[prev_index] = days
            stack.append((i,temperatures[i]))
        return result




                

                 


            

