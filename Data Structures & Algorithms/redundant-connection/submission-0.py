class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))  # каждый — сам себе родитель
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        
        for u, v in edges:
            if find(u) == find(v):   # уже соединены → цикл!
                return [u, v]
            parent[find(u)] = find(v)          # иначе объединяем