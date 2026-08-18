class Solution:
    def largestInteger(self, a: List[int], k: int) -> int:
        if k==len(a): return max(a)
        z = Counter(a)
        if k==1: return max((v for v in z if z[v]==1),default=-1)
        return max((z[a[0]]==1)*[a[0]]+(z[a[-1]]==1)*[a[-1]]+[-1])