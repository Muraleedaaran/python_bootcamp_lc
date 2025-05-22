from typing import List


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