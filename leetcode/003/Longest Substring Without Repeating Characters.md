### Longest Substring Without Repeating Characters

String 이 주어지면, 그 중 가장 긴 substring을 찾아라. 단, 중복된 character가 없어야한다.

**Example 1:**

```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```

**Example 2:**

```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```



**내생각**

1. LIS(Longest Increasing Subsequence)로 풀면 되지 않을까?(nlogn)
   - 아니였다.
2. 완탐을 해야하나?
   - 가능하나 , n^3 알고리즘이라 별로였다.
3. 가장 큰 크기부터 Window를 잡아두고 확인하기?
   - unique를 사용해서 확인하려고 했으나 먼가 이상했다.



**Solution**

1. Sliding Window

   지금까지 window 내 범위는 내가 이미 확인한 것에서 기반하여 체크한다.

   1. General
      - window 크기를 1로 하고 늘려가고 줄여가면서 답을 찾아가기
      - set을 활용하여 알파벳이 존재하는지만 체크한다.
      - 즉, 겹치는 경우를 바로 제거하고 가지 못한다.
   2. Optimized
      - 중복되는 알파벳의 위치를 기억하여, 이번 위치에서 가장 긴 크기를 찾아낸다.
      - 겹치는 경우를 바로 제거하고 간다.
      - map의 값보다 start가 뒤인 경우가 존재한다. 조심!

 



