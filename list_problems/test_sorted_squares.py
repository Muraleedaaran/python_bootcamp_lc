from typing import List


class SortedSquares:
    @staticmethod
    def sortedSquares(nums: List[int]) -> List[int]:
        '''
        1. Iterate the List and store the square of each number in a new list
        2. sort the list
        '''
        square_list = []
        for each_num in nums:
            square_list.append(each_num * each_num)

        square_list.sort()
        return square_list

def test_findNumbers():
    assert SortedSquares.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert SortedSquares.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]