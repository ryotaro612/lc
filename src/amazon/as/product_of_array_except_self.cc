#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        vector<int> result(n, 1);
        for(int i = 0;i<n;i++) {
            if(i == 0)
                result[i] = nums[i];
            else
                result[i] = result[i-1] * nums[i];
        }
        int acc = 1;
        for(int i=n-1;0<=i;i--) {
            if(i == 0) {
                result[i] = acc;
            } else {
                result[i] = result[i-1] * acc;
            }
            acc *= nums[i];
        }
        return result;
    }
};
