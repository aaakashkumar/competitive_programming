// Next Greater Element 
// https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1#
// @author Akash Kumar


// { Driver Code Starts
/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    
	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine().trim());
		while(t-->0){
		    int n = Integer.parseInt(br.readLine().trim());
		    String inputLine[] = br.readLine().trim().split(" ");
		    long[] arr = new long[n];
		    for(int i=0; i<n; i++)arr[i]=Long.parseLong(inputLine[i]);
		    long[] res = new Solution().nextLargerElement(arr, n);
		    for (int i = 0; i < n; i++) 
		        System.out.print(res[i] + " ");
		    System.out.println();
		}
	}
}



// } Driver Code Ends

class Solution{
    public static long[] nextLargerElement(long[] arr, int n) { 
        Stack<Long> stack = new Stack<>();
        long[] nextGreater = new long[n];
        
        for(int i = n-1; i >= 0; --i) {
            
            while(!stack.isEmpty() && stack.peek() <= arr[i])
                stack.pop();
                
            if (stack.isEmpty())
                nextGreater[i] = -1;
            else
                nextGreater[i] = stack.peek();
                
            stack.push(arr[i]);
            
        }
        
        return nextGreater;
    } 
}