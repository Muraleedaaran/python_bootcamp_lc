from typing import List

"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]

 

Constraints:

    1 <= arr.length <= 104
    0 <= arr[i] <= 9
"""

class AddingDuplicateZeros:
    @staticmethod
    def duplicateZeros(nums: List[int]) -> List[int]:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(nums)

        i =0

        while length > 0:
            if (nums[i] == 0):
                nums.insert(i + 1, 0)
                nums.pop()
                length -= 1
                i += 1
            i += 1
            length -= 1

        return nums

def test_findNumbers():
    assert AddingDuplicateZeros.duplicateZeros([1,0,2,3,0,4,5,0]) == [1,0,0,2,3,0,0,4]
    assert AddingDuplicateZeros.duplicateZeros([1,2,3]) == [1,2,3]