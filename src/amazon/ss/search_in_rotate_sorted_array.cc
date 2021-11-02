#include <bits/stdc++.h>
using namespace std;
/*
[1]
0 -> -1
[3,1]
0 -> -1
*/
class Solution {
  public:
    int search(vector<int> &nums, int target) {
        int pivot = lookUpPivot(nums, 0, nums.size());
        if(pivot == -1) {
            auto iter = lower_bound(nums.begin(), nums.end(), target);
            int index = iter - nums.begin();
            if(index == nums.size() || nums[index] != target)
                return -1;
            return index;
        }
        // cout << pivot << endl;
        auto iter = lower_bound(nums.begin(), nums.begin() + pivot + 1, target);
        // cout << *iter << endl;
        if(iter != nums.begin() + pivot + 1 && *iter == target)
            return iter - nums.begin();
        iter = lower_bound(nums.begin() + pivot + 1, nums.end(), target);
        // cout << *iter << endl;
        if(iter == nums.end() || *iter != target)
            return -1;
        return iter - nums.begin();
    }
    int lookUpPivot(vector<int> &nums, int from, int to) {
        if(from == to)
            return -1;
        if(from + 1 == to) {
            if(to == (int)nums.size())
                return -1;
            if(nums[from] > nums[to])
                return from;
            return -1;
        }

        int mid = (from + to) / 2;
        int res = lookUpPivot(nums, from, mid);
        if(res >= 0)
            return res;
        return lookUpPivot(nums, mid, to);
    }
};