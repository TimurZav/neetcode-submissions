class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
    
        for pos, sp in sorted(zip(position, speed), reverse=True):
            time = (target - pos) / sp
            if not stack or time > stack[-1]:
                stack.append(time)  # новый флот
            # иначе догоняет предыдущий — не добавляем
        
        return len(stack)