class Solution:
    def changeSequence(self, arr):
        l = len(arr)

        # check first 2 numbers to decide if increasing or decreasing
        # increase
        if arr[0] < arr[1]: 
            for i in range(l):
                if i + 1 > l - 1:
                    break
                else:
                    if arr[i] > arr[i+1]:
                        return i
        # decrease
        else:
            for i in range(l):
                if i + 1 > l - 1:
                    break
                else:
                    if arr[i] < arr[i+1]:
                        return i

        return -1


print(Solution().changeSequence([1, 2, 4, 8, 4, 2]))
print(Solution().changeSequence([1, 2, 4, 8, 10, 12]))
print(Solution().changeSequence([12, 10, 8, 4, 8, 12]))
print(Solution().changeSequence([12, 11, 13, 14, 15, 16]))