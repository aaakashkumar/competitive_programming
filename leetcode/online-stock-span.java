// Online Stock Span
// https://leetcode.com/problems/online-stock-span/
// @author Akash Kumar


import java.util.Stack;

class StockSpanner {
    
    public class StackObject {
        public int price;
        public int span;
        
        public StackObject(int price, int span) {
            this.price = price;
            this.span = span;
        }
    }
    
    public Stack<StackObject> stack;
    
    public StockSpanner() {
        this.stack = new Stack<StackObject> ();
    }
    
    public int next(int price) {
        if (this.stack.isEmpty()) {
            
            StackObject stackVal = new StackObject(price, 1);
            
            this.stack.push(stackVal);
            return 1;
        }
        
        // pop all the elements before the current element in the stack which are 
        // smaller than it. add their span values to the current span. 
        // the later elements can then use the current elements span value.
        int span = 1;
        while(!this.stack.isEmpty() && this.stack.peek().price <= price) {
            span += this.stack.pop().span;
        }
        this.stack.push(new StackObject(price, span));
        return span;
        
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */