class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            b = int(i[11:13])
            if b > 60:
                count += 1
        return count