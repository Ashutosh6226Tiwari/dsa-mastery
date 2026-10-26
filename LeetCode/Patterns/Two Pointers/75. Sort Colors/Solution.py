class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # left,right = 0 , len(nums)-1
        # curr=0

        # while curr<=right :
        #     if nums[curr]==2:
        #         nums[curr] ,nums[right] = nums[right] , nums [curr]
        #         right-=1
 

        #     elif nums[curr]==0:
        #         nums[left], nums[curr]=nums[curr],nums[left]
        #         left +=1
        #         curr=curr+1

        #     else:
        #         curr+=1


# time complexitiy =O(n)
        left, right = 0, len(nums) - 1
        curr = 0

        while curr <= right:
            if nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
                
                

            elif nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr+=1
    
            else:
                curr += 1


        

           