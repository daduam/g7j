class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        relpos = dict()
        for i, val in enumerate(arr2):
            relpos[val] = i
        return sorted(arr1, key=lambda val: relpos[val] if val in relpos else val + 1000)
        