class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = [-1]* len(nums1)
        stack = []
        idx_in_num1={num:i for i , num in enumerate (nums1)}

        for num in reversed(nums2):
            while stack and stack[-1]<=num:
                stack.pop()

            if num in idx_in_num1 and stack : 
                res[idx_in_num1[num]]=stack[-1]

            stack.append(num)     

        return res  




        