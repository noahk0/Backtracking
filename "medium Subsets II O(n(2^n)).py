def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    subset = [[]]

    for num, freq in Counter(nums).items():
        for i in range(len(subset)):
            subset.extend([subset[i] + [num] * (j + 1) for j in range(freq)])

    return subset
