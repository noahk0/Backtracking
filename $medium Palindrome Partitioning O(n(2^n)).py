def partition(self, s: str) -> List[List[str]]:
    palindrome = []

    for i in range(1, len(s) + 1):
        if s[:i] == s[:i][::-1]:
            for rest in self.partition(s[i:]):
                palindrome.append([s[:i]] + rest)

    return palindrome if s else [[]]
