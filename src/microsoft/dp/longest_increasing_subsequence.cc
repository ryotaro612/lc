#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    int lengthOfLIS(vector<int> &nums) {
        int mx = 10001, n = nums.size();
        vector<int> dp(nums.size() + 1, mx);
        for(int i = 0; i < n; i++) {
            *lower_bound(dp.begin(), dp.end(), nums[i]) = nums[i];
        }
        /*
        for(auto e: dp) {
            cout << e <<" " << endl;
        }
        */
        return lower_bound(dp.begin(), dp.end(), mx) - dp.begin();
    }
};