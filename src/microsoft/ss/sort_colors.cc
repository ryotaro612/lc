#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    void sortColors(vector<int> &nums) {
        map<int, int> counter;
        for(auto num : nums)
            counter[num]++;
        int cursor = 0;
        for(auto color_count : counter) {
            for(int i = 0; i < color_count.second; i++)
                nums[cursor++] = color_count.first;
        }
    }
};