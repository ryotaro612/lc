#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<int> searchRange(vector<int> &nums, int target) {
        if(nums.size() == 0)
            return {-1, -1};
        int n = nums.size();
        int lb = -1, ub = n;
        while(ub - lb > 1) {
            int mid = (ub + lb) / 2;

            if(nums[mid] >= target)
                ub = mid;
            else
                lb = mid;
        }
        if(ub == n || nums[ub] != target)
            return {-1, -1};
        int left = ub;
        lb = -1, ub = n;
        while(ub - lb > 1) {
            int mid = (ub + lb) / 2;
            if(target < nums[mid])
                ub = mid;
            else
                lb = mid;
        }
        int right = lb;

        return {left, right};
    }
};