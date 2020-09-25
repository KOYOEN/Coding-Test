//
//  main.cpp
//  004
//
//  Created by KoYo on 2020/08/25.
//  Copyright © 2020 koyolab. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        double answer = 0.0;
        int m = nums1.size();
        int n = nums2.size();
        if(m>n){
            vector<int> temp = nums1; nums1=nums2; nums2=temp;
            int tmp = m; m=n; n=tmp;
        }
        int imin = 0, imax = m, halfLen = (m+n+1)/2;
        while(true) {
            int i = (imin+imax)/2;
            int j = halfLen-i;
            if(i<imax && nums2[j-1] > nums1[i]){
                //i too small
                imin = i+1;
            }
            else if(i>imin && nums1[i-1] > nums2[j]){
                //i too big
                imax = i-1;
            }else {
                //i perfect
                int maxLeft = 0, minRight = 0;
                if(i==0) { maxLeft = nums2[j-1]; }
                else if(j==0) { maxLeft = nums1[i-1];}
                else { maxLeft = max(nums1[i-1], nums2[j-1]); }
                if ((m+n)%2 == 1){
                    //전체 수가 홀수이면
                    answer = maxLeft;
                    break;
                }
                if(i == m) { minRight = nums2[j]; }
                else if(j == n){ minRight = nums1[i]; }
                else {
                    minRight = min(nums1[i], nums2[j]);
                }
                answer = (maxLeft + minRight) / 2.0;
                break;
            }
        }
        return answer;
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
