//
//  main.cpp
//  003
//
//  Created by KoYo on 2020/08/24.
//  Copyright © 2020 koyolab. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s){
        int max = 1;
        s = '0'+s;
        for(int i=1; i<s.length(); i++){
            auto start = find(s.begin(), s.begin()+i, s[i]);
            int tmp = i;
            while(start != s.begin()+i){
                tmp = (int)(s.begin()+i - start);
                start = find(start+1, s.begin()+i, s[i]);
            }
            if(max<tmp) max = tmp;
        }
        return max;
    }
};
int main() {
    // insert code here...
    Solution sol = *new Solution();
    cout << sol.lengthOfLongestSubstring("pwwkew");
    return 0;
}
