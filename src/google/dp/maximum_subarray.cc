#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int maxSubArray(vector<int> &nums) {
        int n = nums.size();
        vector<int> dp(n + 1, 0);
        for(int i = 0; i < n; i++) {
            dp[i + 1] = max(dp[i] + nums[i], nums[i]);
        }
        return *max_element(dp.begin() + 1, dp.end());
    }
};