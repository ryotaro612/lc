#include <bits/stdc++.h>
using namespace std;

/*
[-1,2,1,-4]
1
= 2
[0,0,0]
1
= 0
*/
class Solution {
  public:
    int threeSumClosest(vector<int> &nums, int target) {
        sort(nums.begin(), nums.end());
        int res = 10000000, n = nums.size();
        for(int i = 0; i < n - 2; i++) {
            for(int j = i + 1; j < n - 1; j++) {
                auto found = lower_bound(nums.begin() + j + 1, nums.end(),
                                         target - nums[i] - nums[j]);
                if(found != nums.end()) {
                    if(abs(*found + nums[i] + nums[j] - target) <
                       abs(res - target))
                        res = *found + nums[i] + nums[j];
                }
                if(found > nums.begin() + j + 1) {
                    if(abs(*(found - 1) + nums[i] + nums[j] - target) <
                       abs(res - target))
                        res = *(found - 1) + nums[i] + nums[j];
                }
            }
        }
        return res;
    }
};