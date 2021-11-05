class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Better approach
        max_area = 0

        right_ptr = len(height) - 1

        left_ptr = 0

        while(left_ptr < right_ptr):

            if(height[left_ptr] >= height[right_ptr]):
        
                if(max_area < (height[right_ptr] * abs(right_ptr - left_ptr))):
            
                    max_area = (height[right_ptr] * abs(right_ptr - left_ptr))
        
                right_ptr -= 1
    
            else:

                if(max_area < (height[left_ptr] * abs(right_ptr - left_ptr))):
            
                    max_area = (height[left_ptr] * abs(right_ptr - left_ptr))
        
                left_ptr += 1

        return max_area
