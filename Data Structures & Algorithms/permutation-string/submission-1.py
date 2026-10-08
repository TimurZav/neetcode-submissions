class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if not s1 or not s2:
        #     return False
        
        # s1_freq = Counter(s1)
        # len_window = len(s1)

        # for right in range(len(s2)):
        #     if s1_freq == Counter(s2[right:right+len_window]):
        #         return True

        # return False
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])
        
        if s1_count == window:
            return True
        
        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1          # добавляем правый
            window[s2[i - len(s1)]] -= 1  # убираем левый
            if window[s2[i - len(s1)]] == 0:
                del window[s2[i - len(s1)]]
            if window == s1_count:
                return True
        
        return False