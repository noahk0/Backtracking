def partition(self, s: str) -> List[List[str]]:
    return [[s[:i]] + rest for i in range(1, len(s) + 1) if s[:i] == s[:i][::-1] for rest in self.partition(s[i:])] if s else [[]]
