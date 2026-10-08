class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        
        s1_freq = Counter(s1)
        len_window = len(s1)

        for right in range(len(s2)):
            if s1_freq == Counter(s2[right:right+len_window]):
                return True

        return False