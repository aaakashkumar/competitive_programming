// Nearly Sorted Algorithm
// https://practice.geeksforgeeks.org/problems/nearly-sorted-algorithm/0
// @author Akash Kumar

/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		PriorityQueue<Integer> heap = new PriorityQueue<Integer>();
		
		int testCases;
		Scanner Sc = new Scanner(System.in);
		testCases = Sc.nextInt();
		
		
		for (int tc=0; tc<testCases; ++tc) {
		    // inputs
		    int N = Sc.nextInt();
		    int K = Sc.nextInt();
		    int[] arr = new int[N];
		    for(int i=0; i<N; ++i)
		        arr[i] = Sc.nextInt();
		        
		    // System.out.println(Arrays.toString(arr));
		        
		    // create a heap of size K
		    for(int i=0; i<K; ++i)
		        heap.add(arr[i]);
		        
		    // traverse and sort the array
		    for(int k=K; k<N; ++k) {
		        arr[k-K] = heap.remove();
		        heap.add(arr[k]);
		    }
		    
		    for(int k=N-K; k<N; ++k)
		        arr[k] = heap.remove();
		        
		    for(int element: arr) {
		        System.out.print(element);
		        System.out.print(" ");
		    }
		    
		    System.out.println();
		}
	}
}