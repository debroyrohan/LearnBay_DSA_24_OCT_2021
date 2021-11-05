class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        #Code:
        max_distance = 0
        
        left_ptr = 0
        
        right_ptr = left_ptr + 1
        
        max_left_ptr = 0
        
        max_right_ptr = max_left_ptr + 1
        
        num_of_zeros = 0
        
        mid = 0
        
        flag = False
        
        while(right_ptr <= len(seats)-1):

            if(left_ptr == 0 and seats[left_ptr] == 0 and flag == False):
                num_of_zeros += 1
                flag = True
            
            if(seats[right_ptr] == 1):
                if(seats[left_ptr] == 1):
                    mid = right_ptr - (right_ptr - left_ptr)//2
                    if(num_of_zeros % 2 == 0):
                        if((mid - left_ptr -1) > (right_ptr - mid -1)):
                            if(max_distance < (mid - left_ptr - 1)):
                                max_distance = mid - left_ptr - 1
                                max_left_ptr = left_ptr
                                max_right_ptr = right_ptr
                        else:
                            if(max_distance < (right_ptr - mid - 1)):
                                max_distance = right_ptr - mid - 1
                                max_left_ptr = left_ptr
                                max_right_ptr = right_ptr
                                
                    else:
                        if(max_distance < (right_ptr - mid)):
                            max_distance = right_ptr - mid
                            max_left_ptr = left_ptr
                            max_right_ptr = right_ptr
                        
                else:
                    if(max_distance < num_of_zeros):
                        max_distance = num_of_zeros
                        max_left_ptr = left_ptr
                        max_right_ptr = right_ptr
        
                left_ptr = right_ptr
                right_ptr += 1
                num_of_zeros = 0
                mid = 0
            
            elif(right_ptr == len(seats)-1 and seats[right_ptr] == 0):
                num_of_zeros += 1
                if(max_distance < num_of_zeros):
                    max_distance = num_of_zeros
                    max_left_ptr = left_ptr
                    max_right_ptr = right_ptr

                left_ptr = right_ptr
                right_ptr += 1
                num_of_zeros = 0
                mid = 0
            else:
                right_ptr += 1
                num_of_zeros += 1
                mid = 0
        
        return max_distance
