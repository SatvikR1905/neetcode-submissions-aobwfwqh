class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            nums1.append(num)
        nums1.sort()
        left = 0
        right = len(nums1) - 1
        while left < right:
            if len(nums1) % 2 == 0:
                mid = (left + right) // 2
                return float((nums1[mid] + nums1[mid + 1]) / 2)
            else:
                mid = (left + right) // 2
                return float(nums1[mid])
        return float(nums1[0])
                
        


        