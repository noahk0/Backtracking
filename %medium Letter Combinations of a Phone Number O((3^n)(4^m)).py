def letterCombinations(self, digits: str) -> List[str]:
    if not digits:
        return []

    combination, button = [''], {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    for digit in digits:
        new = []

        for cur in combination:
            new.extend([cur + letter for letter in button[digit]])

        combination = new

    return combination
