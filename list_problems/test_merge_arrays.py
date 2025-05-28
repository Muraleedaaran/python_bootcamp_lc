from typing import List


class MergeArrays:
    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1, pointer2 = m - 1, n - 1
        index = m + n - 1

        while pointer2 >=0:
            if pointer1 >= 0 and nums1[pointer1] > nums2[pointer2]:
                nums1[index] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[index] = nums2[pointer2]
                pointer2 -= 1
            index -= 1

        return nums1

def test_findNumbers():
    assert MergeArrays.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3) == [1,2,2,3,5,6]
    assert MergeArrays.merge(nums1 = [1], m = 1, nums2 = [], n = 0) == [1]
    assert MergeArrays.merge(nums1 = [0], m = 0, nums2 = [1], n = 1) == [1]
    assert MergeArrays.merge(nums1=[-1,0,0,3,3,3,0,0,0], m=6, nums2=[1,2,2], n=3) == [-1,0,0,1,2,2,3,3,3]