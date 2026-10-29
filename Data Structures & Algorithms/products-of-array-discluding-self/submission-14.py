class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post = [1]
        pred = [1]
        l = []
        for i in range(len(nums)):
            if i == 0:
                continue
            pred.append(pred[i-1] * nums[i-1])

        for i in range(len(nums)):
            if i == 0:
                continue
            post.append(post[i-1] * nums[len(nums)-i])
        
        for i in range(len(nums)):
            prod = pred[i]*post[len(nums)-i-1]
            l.append(prod)
        return l