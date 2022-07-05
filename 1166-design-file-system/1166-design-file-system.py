class FileSystem:

    def __init__(self):
        self.map = defaultdict(list)

    def createPath(self, path: str, value: int) -> bool:
        temp = path.split('/')
        if len(temp)==2 and path not in self.map:
            self.map[path] = value
            return True
            
        parent = '/'.join(temp[:-1])
        if parent not in self.map:
            return False
        
        if path not in self.map:
            self.map[path] = value
            return True
        
        return False

    def get(self, path: str) -> int:
        if path not in self.map:
            return -1
        return self.map[path]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)