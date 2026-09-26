class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        count = len(parent)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for u, v in edges:
            if find(u) != find(v):
                parent[find(u)] = find(v)
                count -= 1

        return count