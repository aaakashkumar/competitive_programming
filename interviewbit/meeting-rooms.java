// Meeting Rooms
// https://www.interviewbit.com/problems/meeting-rooms/
// @author Akash Kumar

public class Solution {
    /**
    Interval objects store how many intervals
    start at a given timestamp and how many
    intervals end at a given timestamp
     */
    public class Interval {
        int start;
        int end;
        
        Interval(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
    
    public int solve(int[][] A) {
        
        HashMap<Integer, Interval> map = new HashMap<>();
        ArrayList<Integer> intervalTimestamps = new ArrayList<> ();
        
        // create a HashMap of timestamp to (start,end) count mappings
        // as well as a list containing the unique timestamps
        for(int i=0; i<A.length; ++i) {
            
            if(!map.containsKey(A[i][0])){
                map.put(A[i][0], new Interval(0,0));
                intervalTimestamps.add(A[i][0]);
            }
            
            if(!map.containsKey(A[i][1])){
                map.put(A[i][1], new Interval(0,0));
                intervalTimestamps.add(A[i][1]);
            }
            
        }
        
        Collections.sort(intervalTimestamps);
        // System.out.println(intervalTimestamps);
        
        // fill in the correct start, end count values for the timestamps
        for(int[] interval: A) {
            map.put(interval[0], new Interval(map.get(interval[0]).start+1,
                                              map.get(interval[0]).end));
            map.put(interval[1], new Interval(map.get(interval[1]).start,
                                              map.get(interval[1]).end+1));
        }
        
        // find the max number of overlapping intervals
        int sum = 0, maxSum = 0;
        for(int intervalTimestamp: intervalTimestamps) {
            sum += map.get(intervalTimestamp).start;
            maxSum = Math.max(sum, maxSum);
            sum -= map.get(intervalTimestamp).end;
            maxSum = Math.max(sum, maxSum);
        }
        
        return maxSum;
        
    }
}
