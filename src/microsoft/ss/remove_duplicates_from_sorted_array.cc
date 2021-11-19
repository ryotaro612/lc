#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    int removeDuplicates(vector<int> &nums) {
        int n = nums.size();
        if(n == 0)
            return 0;
        int cursor = 1;
        for(int i = 1; i < n; i++) {
            if(nums[cursor - 1] == nums[i])
                continue;
            nums[cursor++] = nums[i];
        }
        return cursor;
    }
};