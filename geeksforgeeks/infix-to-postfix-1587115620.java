// Infix to Postfix
// https://practice.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1
// @author Akash Kumar

// { Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        while(t-->0){
            System.out.println(new Solution().infixToPostfix(br.readLine().trim()));
        }
    }
}// } Driver Code Ends

class Solution{
	public static String infixToPostfix(String exp) {
	    // A HashMap containing the precedence values of the operators
		HashMap<Character, Integer> precedence = new HashMap<Character, Integer> ();
		precedence.put('+', 1);
		precedence.put('-', 1);
		precedence.put('*', 2);
		precedence.put('/', 2);
		precedence.put('^', 3);
		precedence.put('(', -1);
		
		String postfix = new String("");
		Stack<Character> stack = new Stack<> ();
		
		for (int i=0; i < exp.length(); ++i) {
		    char character = exp.charAt(i);
		    
            // add normal characters (operands) to the result
		    if (Character.isLetterOrDigit(character)) 
		        postfix += character;
		        
            // push a starting parenthesis to the stack
		    else if(character == '(') 
		        stack.push('(');
		        
            // if an ending parenthesis is found, pop all the elements
            // till the starting parenthesis is found, and add those values
            // to the result
		    else if(character == ')') {
		        while (!stack.isEmpty() && stack.peek() != '(')
		            postfix += stack.pop();
		        
		        stack.pop();
		    }
		    
            // in case an operator is found, pop all the 
            // higher precedence values (if any) and add them to the result
            // and push the current character then
		    else {
		            while (!stack.isEmpty() && 
		                   precedence.get(stack.peek()) >= precedence.get(character))
		                   postfix += stack.pop();
		            stack.push(character);
		        }
		}
		
        // add the leftover operators to the result
		while(!stack.isEmpty()) 
		    postfix += stack.pop();
		    
		return postfix;
	} 
}