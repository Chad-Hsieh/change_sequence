class Solution:
    def changeSequence(self, arr):
        l = len(arr)
        for i in range(l):
            if i + 1 > l - 1:
                break
            else:
                if arr[i] > arr[i+1]:
                    return i

        return -1
    
print(Solution().changeSequence([1, 2, 4, 8, 4, 2]))