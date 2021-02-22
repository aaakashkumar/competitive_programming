# Subarray Sums Divisible by K

##  Solution

> From jjfchen's [comment](https://leetcode.com/problems/subarray-sums-divisible-by-k/solution/725727)

Unless you already understand the solution it is impossible to understand what's described. So here is my attempt to explain how it works.

The first intuition is to do this via brute force. You need to find all the combinations of contiguous subarrays and for each of those combinations you need to add them up and try mod each by K. If the result is 0 you add 1 to the answer and return the answer at the end. If you do this the complexity is O(N<sup>3</sup>). Basically for each element in array A, you need to combine it with every other element of array A then finally another loop for all the possible combinations and add them up.

If you convert A to prefix sums array P, then you will reduce the complexity of having to add up every possible combinations of subarrays to a O(1) complexity. This is because if you make P[0] = A[0], P[1] = A[0] + A[1], P[2] = A[0] + A[1] + A[2] and so on, then if you need to know the running sum from A[0] to A[100], you just need P[99] + A[100] then save it to P[100] = P[99] + A[100]. If you need to know the running sum from A[80] to A[88], then you calculate it as P[88] - P[79]. This means you can calculate any running sum of any combinations of contiguous subarray between starting index i to end index j as P[j] - P[i-1].

However, having prefix sums to reduce calculating running sums complexity does NOT reduce the other O(N<sup>2</sup>) complexity because you still need to loop through every element in A against every other elements in A to find out all the possible combinations of subarrays. So if you do brute force using prefix sums, you still get O(N<sup>2</sup>) complexity.

The solution provided here is a couple of Math trick to reduce the entire complexity to O(N). Basically you don't need to find all the possible subarray combinations and here is how it works:

1. If 2 numbers both mod K returns the same value, then the subtraction of the 2 numbers results a value that will mod K and = 0. For example, if K = 5, then 7 mod K = 2, and 12 mod K = 2. So 12 - 7 = 5 which if mod K will = 0. This is because when you substract them, since both mod K remainder = same value, the subtraction will cancel it out to 0 result the rest of the value mod K to = 0.

    If you generalize this to a formula, then

  $$a\space\text{mod}\space{K} = d \implies a = x + d$$ and $$x\space\text{mod}\space K = 0$$ (.e.g. 7 % K = 2, so 7 = 5 + 2 and 5 % K = 0)

  $$b\space\text{mod}\space K = d \implies b = y + d$$ and $$y \space \text{mod} \space K = 0$$ (.e.g. 12 % K = 2, so 12 = 10 + 2 and 10 % K = 0)

  $$\implies b - a = (y + d) - (x + d) = y - x$$ (.e.g. (10 + 2) - (5 + 2) = 10 - 5
  because $$x \space \text{mod} \space K = 0$$ and $$y \space \text{mod} \space K = 0$$ this means (y - x) mod K = 0 (.e.g. 10 - 5 = 5 and 5 % K = 0)
  $$\implies (a - b) \space \text{mod} \space K = 0$$

2. So if we loop through every prefix sum in array P and found out say both P[3] and P[1] mod K == to same value, then we know (P[3] - [P1]) mod K = 0. Because P[3] - P[1] = running some of subarray A[2] to A[3], then we know the subarray A[2] to A[3]'s running sum is divisible by K.

3. If we find say 5 different P values has same mod K value, then we need to find all the unique 2 pair combinations of 5 different P values so that we know all those pairs' subtraction are divisible by K. To find all the combinations we use this [Math formula](https://stackoverflow.com/a/18860862/6722799) $$(v \times (v - 1)) / 2$$. For example if there are 5 values, then all possible unique pairs = 5 ✕ (5 - 1) / 2 = 10. This means there are 10 possible combinations of contiguous subarrays in A that are divisible by K.

4. Usually prefix sums starts at A[0], i.e. P[0] = A[0]. The solution provided here starts at P[0] = 0 and P[1] = A[0]. This is because if we have P[x] mod K = 0, then we know P[x] which = A[0] + A[1] + ... + A[x] is also another possible divisible by K solution. However, if we use formula $$(v \times (v - 1)) / 2$$ and if $$v = 1$$, we get 0 as the answer. This is why we start at P[0] = 0 because 0 mod K always = 0. P[x] - P[0] = running sum of A[0] to A[x]. So if we have P[x] mod K = 0, then we knew there are at least another P[0] that also mod K to 0. If we do NOT start P[0] at 0, then the code has to consider P[x] mod K = 0 as special cases and calculate all the P mod K = 0 combinations differently.

5. Normally we want to use a HashMap and add each possible mod K value as a key and number of P that mod to same value as the value. However, because any number mod K are always < K, the solution used another trick to save space by saving those counts in an array of size K, i.e. `int[] count = new int[K];`. Say if 5 different P mod K all = 1, then we just set count[1] = 5. If 3 different P mod K = 0, then count[0] = 3. It impossible to have any thing mod K = something > K, so count[] is exactly enough space we need to use to store these counts. However, since A may contain negative element, the mod K result may be negative and we CANNOT use negative index in count[] array, the solution used yet another hashing trick to hash negative numbers to positive. So instead of P mod K, the solution uses (P mod K + K) mod K again. This way the result will always be positive. Note: if you use a HashMap instead, you don't need to use (P % K + K) % K trick because you can store negative integer as key too.

6. Finally the answer is to just add all the values in count[] array by using answer += v ✕ (v - 1) /2 formula. This will result a O(N) complexity.

##### Better explanation for point 1:

> Let there be a subarray (i, j) whose sum is divisible by k
> 		sum(i, j) = sum(0, j) - sum(0, i-1)
>
> Sum for any subarray can be written as q*k + rem where q is a quotient and rem is remainder.
>
> Thus,     
> 		sum(i, j) = (q1 * k + rem1) - (q2 * k + rem2)
> 		sum(i, j) = (q1 - q2)k + rem1-rem2
>      
> We see, for sum(i, j) i.e. for sum of any subarray to be divisible by k, the RHS should also be divisible by k. (q1 - q2)k is obviously divisible by k, for (rem1-rem2) to  follow the same, rem1 = rem2 where
> 		rem1 = Sum of subarray (0, j) % k
> 		rem2 = Sum of subarray (0, i-1) % k 

[GeeksForGeeks]: https://www.geeksforgeeks.org/count-sub-arrays-sum-divisible-k/	"Count all sub-arrays having sum divisible by k"

## Code

Java:

```java
class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int N = A.length;
        int[] P = new int[N+1];
        for (int i = 0; i < N; ++i)
            P[i+1] = P[i] + A[i];

        int[] count = new int[K];
        for (int x: P)
            count[(x % K + K) % K]++;

        int ans = 0;
        for (int v: count)
            ans += v * (v - 1) / 2;
        return ans;
    }
}
```

Python:

```python
class Solution(object):
    def subarraysDivByK(self, A, K):
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)

        count = collections.Counter(P)
        return sum(v*(v-1)/2 for v in count.values())
```