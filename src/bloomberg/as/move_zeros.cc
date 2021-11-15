#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    void moveZeroes(vector<int> &nums) {
        int assign_pos = 0, count = 0, n = nums.size();
        for(int i = 0; i < n; i++) {
            if(nums[i] == 0) {
                count++;
            } else {
                nums[assign_pos] = nums[i];
                assign_pos++;
            }
        }
        for(int i = 0; i < count; i++) {
            nums[assign_pos++] = 0;
        }
    }
};