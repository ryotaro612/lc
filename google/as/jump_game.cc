#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

class Solution {
  public:
    bool canJump(vector<int> &nums) {

        vector<bool> used(nums.size(), false);
        return reachable(0, nums, used);
    }

    bool reachable(int index, vector<int> &nums, vector<bool> &used) {
        used[index] = true;
        if(index == nums.size() - 1)
            return true;

        for(int i = 1; i <= nums[index]; i++) {
            int backward = index - i, forward = index + i;
            if(backward >= 0 && !used[backward]) {
                if(reachable(backward, nums, used))
                    return true;
            }
            if(forward < nums.size() && !used[forward]) {
                if(reachable(forward, nums, used)) {
                    return true;
                }
            }
        }

        return false;
    }
};