class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        z=[]
        for i in range(len(arr)):
            arr.remove(arr[0])
            if len(arr)>0: 
                l=max(arr)
                z.append(l)
        z.append(-1)
        return z
