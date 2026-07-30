class Solution:
    def findTwoElement(self, arr):
        repeat = -1
        missing = -1

        for num in arr:
            index = abs(num) - 1
            if arr[index] < 0:
                repeat = abs(num)
            else:
                arr[index] *= -1

        for i in range(len(arr)):
            if arr[i] > 0:
                missing = i + 1
                break

        return [repeat, missing]