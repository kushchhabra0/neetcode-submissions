from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # Monotonic Stack stores pairs: (start_index, height)

        # Step 1: Histogram bars ko iterate karo
        for i, h in enumerate(heights):
            start = i  # Current bar kis index tak piche extend ho sakta hai
            
            # Jab tak current height 'h' stack ke top bar se choti hai, 
            # monotonic increasing property preserve karne ke liye stack pop karo
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Popped bar ka max area calculate karo (width = current_index - popped_bar_start_index)
                maxArea = max(maxArea, height * (i - index))
                # Current bar ko popped bar ke index tak piche stretch kiya ja sakta hai
                start = index
                
            # Stack mein current bar (updated start_index, height) push karo
            stack.append((start, h))

        # Step 2: Stack mein bache huye bars histogram ke end (len(heights)) tak extend ho sakte hain
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea