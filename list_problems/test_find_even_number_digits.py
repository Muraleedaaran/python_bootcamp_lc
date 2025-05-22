from typing import List


# def findNumbers(nums: List[int]) -> int:
#     '''
#     1. Iterate each number
#     2. For each number recursively iterate it by 10 till the quotient is 0  and incr count
#     3. if the count is even (divisible by 2) then incr the even_counter
#     '''
#     even_counter = 0
#     for each_num in nums:
#         count = findDigitCount(each_num, 0)
#         if (count % 2) == 0:
#             even_counter += 1
#     return even_counter
#
#
# def findDigitCount(num: int, count: int) -> int:
#
#     q = num // 10
#     count += 1
#     if q == 0:
#         return count
#     return findDigitCount(q, count)

class FindEvenNumberDigits:
    @staticmethod
    def hasEvenDigits(num: int) -> bool:
        digit_count = 0
        while num:
            digit_count += 1
            num //= 10
        return digit_count & 1 == 0

    @staticmethod
    def findNumbers(nums: List[int]) -> int:
        even_count = 0
        for num in nums:
            if FindEvenNumberDigits.hasEvenDigits(num):
                even_count += 1
        return even_count

# Test function
def test_findNumbers():
    assert FindEvenNumberDigits.findNumbers([12, 345, 2, 6, 7896]) == 2
    assert FindEvenNumberDigits.findNumbers([555, 901, 482, 1771]) == 1
