def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    sums = []
    candidates.sort()

    def dfs(i, total, combination):
        if total == target:
            sums.append(combination)
        elif total < target:
            for j in range(i, len(candidates)):
                if i == j or candidates[j - 1] < candidates[j]:
                    dfs(j + 1, total + candidates[j], combination + [candidates[j]])

    dfs(0, 0, [])

    return sums
