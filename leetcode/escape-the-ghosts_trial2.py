class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        pdist = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            if pdist >= abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]):
                return False
        return True