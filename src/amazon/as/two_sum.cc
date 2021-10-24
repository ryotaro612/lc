#include <bits/stdc++.h>
using namespace std;
/*

[2,5,5,11]
10
-> 1, 2

*/

class Solution {
  public:
    vector<int> twoSum(vector<int> &nums, int target) {
        vector<int> origin(nums);
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for(int i = 0; i < n; i++) {
            int other = target - nums[i];
            auto iter = lower_bound(nums.begin(), nums.end(), other);
            if(iter != nums.end() && *iter == other) {
                vector<int> res(2);
                vector<int> vals = {min(nums[i], *iter), max(nums[i], *iter)};
                for(int j = 0; j < n; j++) {
                    if(origin[j] == vals[0]) {

                        res[0] = j;
                        break;
                    }
                }
                for(int j = n - 1; j >= 0; j--) {
                    if(origin[j] == vals[1]) {
                        res[1] = j;
                        break;
                    }
                }
                return res;
            }
        }
        return {};
    }
};