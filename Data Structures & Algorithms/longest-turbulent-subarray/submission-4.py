class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        curr_len = 1 # we intialize the curr_len and Max_len as 1 because when we start our turbulent subarray window there will be minimum of one element starting up
        max_len = 1
        prev_sign = ""
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]: #comparing the values
                curr_sign = "up"
            elif arr[i] < arr[i-1]:
                curr_sign = "down"
            elif arr[i] == arr[i-1]:
                curr_len = 1
                prev_sign = ""
                continue # we move to next iteration

            if curr_sign != prev_sign:
                curr_len += 1
            else:
                curr_len = 2 #if the previous sign is equal to current sign then we start window with 2 elements EX [1,2,3] 1 < 2 and 2 < 3 both are up so we start new window from [2,3..]
            prev_sign = curr_sign
            max_len = max(curr_len,max_len) #return max_len
        return max_len
        