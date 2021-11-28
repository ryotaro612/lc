#include <bits/stdc++.h>
using namespace std;
/*
[1,3,5] -> 1
[2,2,2,0,1] -> 0
*/
class Solution {
  public:
    int findMin(vector<int> &nums) {
        // left > mid => min is in left side
        // left < mid => min is in right side
        return min(nums[0], rec(0, (int)nums.size(), nums));
    }
    int rec(int left, int right, vector<int> &nums) {
        cout << left << " " << right << endl;
        if(right - left == 1)
            return nums[left];
        int mid = (left + right) / 2;
        if(nums[left] == nums[mid]) {
            return min(rec(left, mid, nums), rec(mid, right, nums));
        } else if(nums[left] < nums[mid]) {
            return rec(mid, right, nums);
        } else { // left > mid
            return min(nums[mid], rec(left, mid, nums));
        }
    }
};