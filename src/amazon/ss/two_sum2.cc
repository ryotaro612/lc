#include <bits/stdc++.h>
using namespace std;
/*
[2,7,11,15]
9

[2,3,4]
6

[-1,0]
-1

*/
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        for(int i = 0; i < n - 1; i++) {
            vector<int>::iterator iter = lower_bound(
                numbers.begin() + i + 1, numbers.end(), target - numbers[i]);
            if(iter != numbers.end() && numbers[i] + *iter == target) {
                return {i+1, (int)(iter - numbers.begin()) + 1};
            }
        }
        throw runtime_error("unreachable");
    }
};
