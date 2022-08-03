class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        

        nums = [str(n) for n in nums]

        def compare(x: str, y: str) -> int:
            return int(x + y) - int(y + x)

        nums.sort(key=cmp_to_key(compare), reverse=True)

        # if all are zero iff highest is zero, then need to return zero
        if nums[0] == '0':
            return '0'

        return ''.join(nums)