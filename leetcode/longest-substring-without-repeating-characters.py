# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# @author Akash Kumar

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        maximum_length = 1 
        
        substring_elements = set() 
        substring_start = 0 
        substring_end = 0 
        
        while substring_end < len(s):
            
            # add new elements to the sliding window (substring_elements)
            if s[substring_end] not in substring_elements:
                substring_elements.add(s[substring_end])
                
                current_length = substring_end - substring_start + 1
                if maximum_length < current_length:
                    maximum_length = current_length
                    
                substring_end += 1
            
            # if the current element already exists in the sliding window, remove them
            # and increase the start and end index of the sliding window
            else:
                while True:
                    if s[substring_start] == s[substring_end]:
                        substring_start += 1
                        substring_end += 1
                        break
                        
                    else:
                        substring_elements.remove(s[substring_start])
                        substring_start += 1
                    
        return maximum_length

    def test_lengthOfLongestSubstring(self):
        """
        Method to test the code with a few sample cases
        """

        assert self.lengthOfLongestSubstring("abcabcbb") == 3
        assert self.lengthOfLongestSubstring("bbbbb") == 1
        assert self.lengthOfLongestSubstring("pwwkew") == 3
        assert self.lengthOfLongestSubstring("") == 0
        print("All test cases ran successfully")

Solution().test_lengthOfLongestSubstring()