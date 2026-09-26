# LeetCode 15. 3Sum


class Solution(object):
    def threeSum(self, nums):
        result = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):

                    if nums[i] + nums[j] + nums[k] == 0:

                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort()

                        if triplet not in result:
                            result.append(triplet)

        return result
