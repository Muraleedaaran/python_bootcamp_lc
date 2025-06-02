from typing import List

"""
Given an array arr of integers, check if there exist two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.

 

Constraints:

    2 <= arr.length <= 500
    -103 <= arr[i] <= 103
"""

class DoubleNNumbers:
    @staticmethod
    def checkIfExist(arr: List[int]) -> bool:
        i = 0
        j = 0

        length = len(arr)

        while i < length:
            if j == i:
                j += 1
                continue
            if j == length:
                break
            if arr[i] == 2 * arr[j]:
                return True
            if j == length - 1:
                j = 0
                i += 1
            else: j += 1

        return False

def test_findNumbers():
    assert DoubleNNumbers.checkIfExist(arr = [-2,0,10,-19,4,6,-8]) == False
    assert DoubleNNumbers.checkIfExist(arr = [0,-2,2]) == False
    assert DoubleNNumbers.checkIfExist(arr = [10,2,5,3]) == True
    assert DoubleNNumbers.checkIfExist(arr = [3,1,7,11]) == False
    assert DoubleNNumbers.checkIfExist(arr= [7,1,14,11]) == True