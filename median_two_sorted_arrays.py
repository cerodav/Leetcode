import heapq

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left, lCount, right, rCount = [], 0, [], 0
        allNumbers = nums1 + nums2
        for ele in allNumbers:
            heapq.heappush(left, -(ele))
            heapq.heappush(right, -(heapq.heappop(left)))
            rCount += 1
            if rCount > lCount:
                heapq.heappush(left, -(heapq.heappop(right)))
                rCount -= 1
                lCount += 1

        if rCount == lCount:
            return (right[0] - left[0]) / 2
        else:
            return -left[0]