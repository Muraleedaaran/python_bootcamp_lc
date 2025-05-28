from typing import List

"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

 

Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.


"""

class MaxConsecutiveOnes:
    @staticmethod
    def duplicateZeros(nums: List[int]) -> int:
        '''
        1. initialize max_recur_one and count as 0
        2. iterate list
            a. incr count if 1 is present
            b. else check if count > max_recur_one and store it accordingly if true.
            c. reset count and continue iteration
        3. return max_recur_one
        '''

        max_recur_one, count = 0, 0

        for each_num in nums:
            if each_num == 1:
                count += 1
            else:
                if count > max_recur_one:
                    max_recur_one = count
                count = 0

        return max(max_recur_one, count)

def test_findNumbers():
    assert MaxConsecutiveOnes.duplicateZeros([1,1,0,1,1,1]) == 3
    assert MaxConsecutiveOnes.duplicateZeros([1,0,1,1,0,1]) == 2