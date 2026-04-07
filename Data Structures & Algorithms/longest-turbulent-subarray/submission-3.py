class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        curr_len = 1
        max_len = 1
        prev_sign = ""
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                curr_sign = "up"
            elif arr[i] < arr[i-1]:
                curr_sign = "down"
            else:
                curr_len = 1
                prev_sign = ""
                continue

            if curr_sign != prev_sign:
                curr_len += 1
            else:
                curr_len = 2
            prev_sign = curr_sign
            max_len = max(curr_len,max_len)
        return max_len
        