class MyHashMap:

    def __init__(self):
        self.a = dict()        

    def put(self, key: int, value: int) -> None:
        self.a[key] = value

    def get(self, key: int) -> int:
        return self.a.get(key, -1)

    def remove(self, key: int) -> None:
        if key in self.a:
            del self.a[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
