class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 1
        end = len(arr) - 1
        
        while(start <= end):
            mid = end - ((end - start)//2)
            
            if(arr[mid] > arr[mid-1] and arr[mid + 1] < arr[mid]):
                return mid
            elif(arr[mid] <= arr[mid-1]):
                end = mid - 1
            else:
                start = mid + 1
        