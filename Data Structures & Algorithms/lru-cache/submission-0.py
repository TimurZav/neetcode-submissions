class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # head.next — most recently used node
        # tail.prev — least recently used node
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: Node) -> None:
        # Удалить node из двусвязного списка.
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_after_head(self, node: Node) -> None:
        # Вставить node сразу после head: он становится most recently used.
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        # Вернуть значение и сделать найденный узел most recently used.
        cache_node = self.cache.get(key)
        if not cache_node:
            return -1
        self._remove(cache_node)
        self._insert_after_head(cache_node)
        return cache_node.value

    def put(self, key: int, value: int) -> None:
        # Добавить/обновить ключ и удалить least recently used при переполнении.
        cache_node = self.cache.get(key)
        if cache_node:
            # Ключ уже существует, обновляем значение и делаем его most recently used.
            cache_node.value = value
            self._remove(cache_node)
            self._insert_after_head(cache_node)
        else:
            # Ключ не существует, создаём новый узел.
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._insert_after_head(new_node)

            if len(self.cache) > self.capacity:
                # Удаляем least recently used узел.
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
