class Solution(object):
    def combinationSum(self, candidates, target):
        def backtrack(start, target, path, result):
            if target < 0:
                return
            if target == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path, result)
                path.pop()

        result = []
        candidates.sort()
        backtrack(0, target, [], result)
        return result
        