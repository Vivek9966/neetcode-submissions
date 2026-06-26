class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r= 0,len(nums)-1

        while l<r:
            mid = (l+r)//2
            if nums[mid]>=nums[r]:
                l=mid+1
            else:
                r=mid
        pivot_index = l
        l,r=0,len(nums)-1
        if target >= nums[pivot_index] and target <= nums[r]:
            l=pivot_index
        else:
            r=pivot_index-1
        if target == nums[pivot_index]:
            return pivot_index
        while l<=r:
            mid=(l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                r= mid-1
            else:
                l=mid+1
        return -1

