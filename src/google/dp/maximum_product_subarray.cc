#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int maxProduct(vector<int> &nums) {
        int n = nums.size(), max_so_far = nums[0], min_so_far = nums[0],
            ans = nums[0];

        for(int i = 1; i < n; i++) {
            int max_so_far_cpy = max_so_far;
            max_so_far =
                max(max_so_far * nums[i], max(nums[i], min_so_far * nums[i]));
            min_so_far =
                min(min_so_far * nums[i], min(nums[i], max_so_far_cpy * nums[i]));
            ans = max(ans, max_so_far);
        }

        return ans;
    }
};
