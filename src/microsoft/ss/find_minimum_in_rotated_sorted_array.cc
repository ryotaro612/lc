#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    int findMin(vector<int> &nums) {
        int lb = 0, ub = nums.size() - 1;
        while(ub - lb > 1) {
            int mid = (ub + lb) / 2;
            if(nums[lb] < nums[mid]) {
                lb = mid;
            } else
                ub = mid;
        }
        return min(nums[0], nums[ub]);
        return -1;
    }
};