class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        running_result = [0,0,0]

        for triplet in triplets:
            i, j, k = triplet[0], triplet[1], triplet[2]
            if i > target[0] or j > target[1] or k > target[2]:
                continue

            running_result[0] = max(i,running_result[0])
            running_result[1] = max(j,running_result[1])
            running_result[2] = max(k,running_result[2])
        if running_result == target:
            return True
        else:
            return False

        