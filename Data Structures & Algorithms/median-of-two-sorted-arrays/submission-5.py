class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B): # we want to perform binary search only on small array
            A , B = B , A

        m , n = len(A) , len(B)
        total = m + n
        half = (total + 1) // 2 # we need to round it off caz we need to find the midpoint

        left, right = 0, m # this is on small array A

        while left <= right:
            i = (left + right) // 2 # its not the index but we are taking no of elements from A
            j = half - i

            A_left = A[i-1] if i > 0 else float("-inf") #the last elemnt of left side of Array A
            B_left = B[j-1] if j > 0 else float("-inf") #the last elemnt of left side of Array B
            A_right = A[i] if i < m else float("inf")#the first element of right side of Array A
            B_right = B[j] if j < n else float("inf") #the last elemnt of right side of Array B

            if A_left <= B_right and B_left <= A_right: # when the partion is right 
                if total % 2 == 1:
                    return float(max(A_left,B_left))
                return(max(A_left, B_left) + min(A_right, B_right)) / 2.0 # here we are actually dividing 
            elif A_left > B_right:
                right = i - 1
            else:
                left = i + 1
        return 0.0

            


        