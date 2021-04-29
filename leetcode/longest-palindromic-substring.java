// Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/
// @author Akash Kumar

class Solution {
    /**
     2D Dynamic programming approach to the Longest Palindromic 
     Substring problem. All characters are palindromes. All two
     letter words are palindromes if they are equal. For strings
     of length greater than 2, they are palindromes if their 
     outermost characters are equal and the string without the
     outermost characters is also a palindrome.
     */
    public String longestPalindrome(String s) {
        
        boolean[][] lps = new boolean[s.length()][s.length()];
        
        for(int i=0; i<s.length(); ++i) {
            for(int j=0; j<s.length()-i; ++j) {
                
                // Base case 1: All single characters are palindromes
                if(i==0) {
                    lps[j][j] = true;
                    continue;
                }
                
                // Base case 2: All two chacracter strings are palindromes
                // if they are equal
                if(i==1) {
                    lps[j][j+1] = s.charAt(j) == s.charAt(j+1);
                    continue;
                }
                
                else {
                    lps[j][j+i] = (s.charAt(j) == s.charAt(j+i) && 
                                   lps[j+1][j+i-1]);
                }
                
            }
        }
        
        // System.out.println(Arrays.deepToString(lps));
        
        int max = 0;
        int maxStartIndex = 0;
        int maxEndIndex = 0;
        
        // traverse the DP array to find the longest palindromic substring
        for(int i=0; i<s.length(); ++i) {
            for(int j=i; j<s.length(); ++j) {
                if(lps[i][j]) {
                    if(j-i+1 > max) {
                        max = j-i+1;
                        maxStartIndex = i;
                        maxEndIndex = j;
                    }
                }
                    
            }
        }
        
        return s.substring(maxStartIndex, maxEndIndex+1);
        
    }
    
}