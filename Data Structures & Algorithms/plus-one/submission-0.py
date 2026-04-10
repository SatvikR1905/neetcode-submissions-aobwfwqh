class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
            strings = []
            for d in digits:
                strings.append(str(d))
            number = ''.join(strings)
            new = int(number) + 1
            res = []
            for d in str(new):
                res.append(d)
            return res

        