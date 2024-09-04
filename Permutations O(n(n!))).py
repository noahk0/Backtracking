def permute(self, nums: List[int]) -> List[List[int]]:
    permutes = [[nums[0]]]

    for num in nums[1:]:
        new = []

        for permute in permutes:
            new.extend([permute[:i] + [num] + permute[i:] for i in range(len(permute) + 1)])

        permutes = new

    return permutes
