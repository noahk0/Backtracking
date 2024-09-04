def subsets(self, nums: List[int]) -> List[List[int]]:
    subset = [[]]

    for num in nums:
        subset.extend([subset[i] + [num] for i in range(len(subset))])

    return subset
