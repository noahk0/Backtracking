def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    sums = []

    def dfs(i, total, combination):
        if total == target:
            sums.append(combination)
        elif total < target and i < len(candidates):
            dfs(i + 1, total, combination)
            dfs(i, total + candidates[i], combination + [candidates[i]])
                        
    dfs(0, 0, [])

    return sums
