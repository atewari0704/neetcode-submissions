class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l = 0
        for r in range(len(arr)):
            if r-l+1 <= k: continue

            if abs(arr[r]-x) < abs(arr[l]-x):
                l=r-k+1

        return arr[l:l+k]

        