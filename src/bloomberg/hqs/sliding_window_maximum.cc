#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    vector<int> maxSlidingWindow(vector<int> &nums, int k) {
        multiset<int> window;
        for(int i = 0; i < k; i++) {
            window.insert(nums[i]);
        }
        vector<int> res = {*prev(window.end())};
        for(int i = k; i < nums.size(); i++) {
            window.erase(window.find(nums[i - k]));
            window.insert(nums[i]);
            res.push_back(*prev(window.end()));
        }
        return res;
    }
};