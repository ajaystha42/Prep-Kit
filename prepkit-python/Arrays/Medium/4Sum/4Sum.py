# 18. 4Sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    fourSum = nums[i] + nums[j] + nums[l] + nums[r]
                    if fourSum > target:
                        r -= 1
                    elif fourSum < target:
                        l += 1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
        return ans

        # Other Solution
        # nums.sort()
        # n = len(nums)
        # ans = set()
        # for p1 in range(n):
        #     for p2 in range(p1 + 1, n):
        #         p3 = p2 + 1
        #         p4 = n - 1
        #         while p3 < p4:
        #             sum = nums[p1] + nums[p2] + nums[p3] + nums[p4]
        #             if sum > target:
        #                 p4 -= 1
        #             elif sum < target:
        #                 p3 += 1
        #             else:
        #                 ans.add((nums[p1], nums[p2], nums[p3], nums[p4]))
        #                 p4 -= 1
        #                 p3 += 1
        # return ans
