class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = iter(vec)
        lst = next(self.vec, None)
        if lst is None:    
            self.lst = None
            self.next_val = None
        else:
            self.lst = iter(lst)
            self.next_val = self.fetch()
            
    def next(self) -> int:
        v = self.next_val
        self.next_val = self.fetch()
        return v
        
    def hasNext(self) -> bool:
        return self.next_val is not None
    
    def fetch(self):
        v = next(self.lst, None)
        if v is None:
            while True:
                lst = next(self.vec, None)
                if lst is None:
                    return
                self.lst = iter(lst)
                v = next(self.lst, None)
                if v is not None:
                    return v
        else:
            return v
