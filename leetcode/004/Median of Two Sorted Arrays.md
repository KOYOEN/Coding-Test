## Median of Two Sorted Arrays

두개의 정렬된 배열을 받아 이 두 배열의 median(중앙값)을 찾는 알고리즘.

시간복잡도를 O(log(m+n))으로 하시오.

**Example 1:**

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

**Example 2:**

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

**Example 3:**

```
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
```

**Example 4:**

```
Input: nums1 = [], nums2 = [1]
Output: 1.00000
```

**Example 5:**

```
Input: nums1 = [2], nums2 = []
Output: 2.00000
```

 

**Constraints:**

- `nums1,length == m`
- `nums2,length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`



**내 생각**

- 도저히 생각해봐도 방법을 모르겠다.



**solution**

- 재귀

  - A[i-1] <= B[j] && A[i] > B[j-1] 인 경우를 찾아야한다.

  - 긴 배열이 m이라고 한 경우, imin=0, imax=m
    $$
    i = {{imin+imax} \over 2}, j={{m+n+1}\over 2}-i
    $$
    

이렇게 값을 정하면 len(left_part) = len(right_part)에 해당한다.
만약 B[j-1] > A[i] 인 경우, i를 증가시켜야한다. 



원리는 알았으나, 구현 부분이나 내 생각이 적게 들어간 듯 하다. 보강이 필요함.