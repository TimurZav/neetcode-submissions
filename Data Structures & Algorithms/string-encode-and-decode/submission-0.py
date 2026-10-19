class Solution:

    def encode(self, strs: list[str]) -> str:
        result = ""
        for word in strs:
            result += f"{len(word)}#{word}"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index('#', i)      # находим #
            length = int(s[i:j])     # длина = число до #
            start_word = j + 1
            result.append(s[j+1:start_word + length])  # берём length символов
            i = start_word + length       # двигаемся дальше
        return result
